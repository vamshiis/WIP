/* NUMERIC FUNCTIONS
   - ROUND()
   -ABS() 
 
   # ROUND ()
   Syntax : ROUND(value,round_value)
   Rules:
   From decimal[round_value+1] to decimal[length] digits all turns 0 when positive 'round_value'  is given.
   If decimal[round_value + 1] >= 5 round's up. so the decimal(round_value) gets +1(rounds up by adding 1)
   If decimal[round_value + 1] < 5 round's downs. so the decimal(round_value) gets nothing stays the same.
   Ex : 3.516 
        ROUND(3.516,2) -> decimal[2+1] = decimal[3] = 6
                          6 >= 5 so the .51 turns to .52
                          turn the decimal[3] till its length all digits to '0'
                          final result '3.520'
        ROUND(3.516,1) -> decimal[1+1] = decimal[2] = 1
                          1 < 5 so the .5 stays  .5
                          turn from decimal[2] to decimal[3]  all digits to '0'
                          final result '3.500'
        ROUND(3.516,0) -> decimal[0+1] = decimal[1] = 5
                          5 >= 5 so the 3 turns to 4
                          turn from decimal[1] to decimal[3]  all digits to '0'
                          final result '4.000'
*/
SELECT
3.516, 
ROUND(3.516,2) as round_2,
ROUND(3.516,1) as round_1,
ROUND(3.516,0) as round_0

/* # ABS() 
   - Used to convert a negative numbers to positive numbers
*/
SELECT
-10,
ABS(-10),
ABS(10)