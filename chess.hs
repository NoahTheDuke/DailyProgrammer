import Data.List

army_set_up_dict = [
        ("RNBQKBNR", "PPPPPPPP"),
        ("RNBMCBNR", "LLLLLLLL"),
        ("ZYXOCXYZ", "PPPPPPPP"),
        ("GNBACBNG", "PPPPPPPP"),
        ("RNBUWBNR", "PPPPPPPP"),
        ("EHTJCTHE", "PPPPPPPP")]

blackArmy = "rnbqkbnr"
blackPawns = "pppppppp"
whiteArmy = "RNBQKBNR"
whitePawns = "PPPPPPPP"

{-blackArmy = str(army_name_dict[bArmy][0][::-1].lower())-}
{-blackPawns = str(army_name_dict[bArmy][1].lower())-}
{-whiteArmy = str(army_name_dict[wArmy][0])-}
{-whitePawns = str(army_name_dict[wArmy][1])-}

initial = 
        "         \n" ++  --   0 -  9
        "         \n" ++  --  10 - 19
        " "++blackArmy++"\n" ++  --  20 - 29
        " "++blackPawns++"\n" ++  --  30 - 39
        " ........\n" ++  --  40 - 49
        " ........\n" ++  --  50 - 59
        " ........\n" ++  --  60 - 69
        " ........\n" ++  --  70 - 79
        " "++whitePawns++"\n" ++  --  80 - 89
        " "++whiteArmy++"\n" ++  --  90 - 99
        "         \n" ++  -- 100 -109
        "          "   -- 110 -119

main = do
    putStrLn "\nBlack Player, choose an army:"
    putStrLn "1. Classic   2. Nemesis  3. Empowered"
    putStrLn "4. Reaper 5. Two Kings 6. Animals"

    putStrLn "\nBlack Player, choose an army:"
    putStrLn "1. Classic   2. Nemesis  3. Empowered"
    putStrLn "4. Reaper 5. Two Kings 6. Animals"
    {-while True:-}
        {-putStrLn "Type the number, not the name."-}
        {-userInput = getpass.getpass('> ''-}
        {-if userInput in string.digits:-}
            {-if int(userInput) < 7:-}
                {-if int(userInput) > 0:-}
                    {-break-}
            {-print('Please enter only one of the above.')-}
        {-else:-}
            {-print('Please enter only one of the above.')-}
    {-bArmy = int(userInput)-}
    putStrLn $ intersperse ' ' initial
