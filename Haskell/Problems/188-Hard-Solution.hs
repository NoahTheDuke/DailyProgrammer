import System.IO
import Data.List
import Text.Printf

data Board = Board { width :: Int
                   , height :: Int
                   , maze :: String
                   } deriving (Show)

main :: IO ()
main = do
    contents <- readFile "188-Maze.txt"
    let (size, maze) = break (== '\n') contents
        [width, height] = map(\x -> read x :: Int) (words size)
        arrows = filter (/= '\n') maze
        bd = Board width height arrows
        results =  parseBoard bd 0 [] []
        sorted = sortBy lenCmp results
    pretty arrows width (head sorted)

lenCmp :: [a] -> [a1] -> Ordering
lenCmp a b
    | length a < length b = GT
    | length a > length b = LT
    | otherwise = EQ

pretty :: String -> Int -> [Int] -> IO b0
pretty board width result = printf "%s" formatted
    where
        colored = zipWith (color result) board [0..]
        formatted = concat (zipWith (format width) colored [0..])

format :: Integral a => a -> [Char] -> a -> [Char]
format width s i
    | mod (i + 1) width == 0 = s ++ "\n"
    | otherwise = s

color :: Eq a => [a] -> Char -> a -> [Char]
color visited c i
    | elem i visited = "|" ++ [c] -- ++ "|"
    | otherwise = [c]

parseBoard :: Board -> Int -> [Int] -> [[Int]] -> [[Int]]
parseBoard board start visited results
    | start < size board = parseBoard board (start + 1) visited newResults
    | otherwise = results
        where
            newResults = result:results
            result = logPath board start visited

followMaze :: Num a => Char -> a -> a -> a
followMaze arrow previous width
    | arrow == '<' = previous - 1
    | arrow == '>' = previous + 1
    | arrow == '^' = previous - width
    | arrow == 'v' = previous + width

logPath :: Board -> Int -> [Int] -> [Int]
logPath board start visited
    | elem start visited = dropWhile (/= start) visited
    | otherwise = logPath board nextStart newVisited
        where
            nextStart = wrap (followMaze c start (width board)) (size board)
            newVisited = visited ++ [start]
            c = inside board start

size :: Board -> Int
size (Board w h _) = w * h

wrap :: (Num a, Ord a) => a -> a -> a
wrap p l
    | p >= l = p - l
    | p < 0 = p + l
    | otherwise = p

inside :: Board -> Int -> Char
inside x w = maze x !! w
