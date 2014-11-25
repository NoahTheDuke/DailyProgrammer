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
        contents <- readFile "188-Maze.txt"
        let (size, maze) = break (== '\n') contents
            [width, height] = map(\x -> read x :: Int) (words size)
            board = Board width height (filter (/= '\n') maze)
        putStrLn $ show board

parseBoard b i = print
