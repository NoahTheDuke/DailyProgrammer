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
    let strs = insertAt width "\n" $ concatMap (directions !!) $ take (width * height) $ randomRs (0, length directions-1) g
    writeFile (show width ++ "-" ++ show height ++ ".txt") $ text ++ "\n" ++ strs
    putStr strs
