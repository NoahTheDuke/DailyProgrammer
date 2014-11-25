{-Read file. Parse W and H. Remove \n from the map, creating a string.
- Walk the string:
- * Recursively Walk the string + 1. At each character, Follow the
- character's path until -}
import System.IO
import Control.Monad

data Board = Board { width :: Int
                   , height :: Int
                   , board :: String
                   } deriving (Show)

{-walkboard board start =-}

{-main :: IO ()-}
main = do
        contents <- readFile "test.txt"
        print . map readInt . words $ contents

readInt :: String -> Int
readInt = read
