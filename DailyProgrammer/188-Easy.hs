{-iso 8601 standard for dates tells us the proper way to do an extended day is yyyy-mm-dd-}

    {-yyyy = year-}
    {-mm = month-}
    {-dd = day-}

{-A company's database has become polluted with mixed date formats. They could be one of 6 different formats-}

    {-yyyy-mm-dd-}
    {-mm/dd/yy-}
    {-mm#yy#dd-}
    {-dd*mm*yyyy-}
    {-(month word) dd, yy-}
    {-(month word) dd, yyyy-}

{-(month word) can be: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec-}

{-Note if is yyyy it is a full 4 digit year. If it is yy then it is only the last 2 digits of the year. Years only go between 1950-2049.-}

import Data.Monoid
import Data.Foldable
import Data.Time
import System.Locale
import Text.Printf

possibleFormats :: [String]
possibleFormats =
    -- yyyy-mm-dd
    [ "%F"
    -- mm/dd/yy
    , "%x"
    -- mm#yy#dd
    , "%m#%y#%d"
    --dd*mm*yyyy
    , "%d*%m*%Y"
    --(month word) dd, yy
    , "%b %d, %y"
    --(month word) dd, yyyy
    , "%b %d, %Y"
    ]

tryParse :: String -> Maybe Day
tryParse str = do
    parsed <- getFirst $ foldMap (First . parse) possibleFormats
    let (y, m, d) = toGregorian parsed
    return $
        if y > 2049
        then fromGregorian (y - 100) m d
        else parsed
    where
        parse :: String -> Maybe Day
        parse f = parseTime defaultTimeLocale f str

main :: IO ()
main = do
    contents <- lines `fmap` readFile "wrongdates.txt"
    forM_ contents $ \date ->
        case tryParse date of
            Just d -> print d
            Nothing -> do
                printf "Failed to parse: %s" date
