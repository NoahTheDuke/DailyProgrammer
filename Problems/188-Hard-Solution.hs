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

main :: IO ()
main = do
    contents <- readFile "188-Maze.txt"
    let (size, maze) = break (== '\n') contents
        [width, height] = map(\x -> read x :: Int) (words size)
        bd = Board width height maze
    putStrLn $ show bd
    print $ parseBoard bd 0 width

parseBoard :: Num a => Board -> Int -> a -> a
parseBoard board init width = followDirection (inside board init) width

followDirection :: Num a => Char -> a -> a
followDirection arrow width
    | arrow == '<' = -1
    | arrow == '>' = 1
    | arrow == '^' = -1 * width
    | arrow == 'v' = width
    | otherwise = 1

inside :: Board -> Int -> Char
inside x w = getBoard x !! w

getBoard :: Board -> String
getBoard = board
