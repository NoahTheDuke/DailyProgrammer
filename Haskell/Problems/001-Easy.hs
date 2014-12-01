main = do
    putStrLn "What is your name?"
    name <- getLine
    putStrLn "What is your age?"
    age <- getLine
    putStrLn "What is your username?"
    username <- getLine
    putStrLn ("Hello " ++ name ++ "!" ++
             " You are " ++ age ++ " years old," ++
             " and your username is " ++ username ++ ".")

