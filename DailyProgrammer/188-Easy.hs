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

{-
- open file. map over the lines the change the date and 
-}
