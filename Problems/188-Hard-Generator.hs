import System.Random
import Control.Monad
import qualified Data.Text as T

directions :: [String]
directions = ["<", ">", "^", "v"]

width :: Int
width = 45

height :: Int
height = 20

text :: String
text = show width ++ " " ++ show height

insertAt :: Int -> [a] -> [a] -> [a]
insertAt i p [] = []
insertAt i p a =
    let splitted = splitAt i a
        first = fst $ splitted
        second = insertAt i p $ snd $ splitted
    in first ++ p ++ second

main :: IO ()
main = do
    putStrLn text
    g <- newStdGen
    let strs = T.unpack $ T.strip $ T.pack $ insertAt width "\n" $ concatMap (directions !!) $ take (width * height) $ randomRs (0, length directions-1) g
    writeFile ("188-Maze.txt") $ text ++ "\n" ++ strs
    putStr strs
