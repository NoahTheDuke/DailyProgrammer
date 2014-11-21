import System.Random
import Control.Monad

directions :: [String]
directions = ["<", ">", "^", "V"]

width :: Int
width = 45

height :: Int
height = 20

text :: String
text = show width ++ " " ++ show height

main :: IO ()
main = do
    putStrLn text
    g <- newStdGen
    let ns = take width $ randomRs (0, length directions-1) g
        strs = map (directions !!) ns
    putStrLn $ show strs
