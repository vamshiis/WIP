   2. FORMAT & CASTING Category
      We have the following functions.
       - FORMAT()
       - CONVERT()
       - CAST()
   
   Formatting : 
    - Changing the format of a value from one to another.
    - Changing how the data looks.
   Ex : 
    DATE format's we can do on the dates columns
    - This are the Different Standard Formats on how a DATE can be Formatted into based on requirement 
      1. ISO FORMAT OF DATE : YYYY-MM-DD
      2. USA FORMAT OF DATE : MM-DD-YYYY
      3. European Format    : dd-MM-YYYY

                           Argumment's passable
                          /---> MM/dd/YY --> 06/10/26
    Input   /---> FORMAT()            
      DATE                \---> MMM yyyy --> Jun 2026
      2026-06-10        
                          /---> 6(style_specifers)     --> 10 Jun 26
           \---> CONVERT() 
                          \---> 112(style_specifiers)  --> 20260610

     - we can also apply the formatting on the number datatypes columns 
       where we can convert it into following ways :
     NUMBER                /---> N ---> 1,234,567.89    (It converts a raw number (like an INT, DECIMAL, or FLOAT) into a formatted string containing thousands separators (commas) and decimal points('.00' default))
     1234567.89    ------> |---> C ---> $1,234,567.89   (C - currency in '$' turns value to string)
                           \---> P ---> 123,456,789.00% (P - converts to percentages by keeping % at last turns the value to string)


    Casting : 
    - Changing data type from one to another.  
    - Chnaging HOW it represents in memory is what CASTING does.
     In SQL Server we have 2 types to change data types
     1. CAST()
     2. CONVERT()
     EX : String 123 --> 123 Number
          Date 2026-09-09 --> '2025-09-09' String
          String '2025-09-09' --> 2025-09-09 DATE

    CAST VS CONVERT VS FORMAT
                     CASTING                                      FORMATING
       CAST     - Converts any dtype to Any dtype           - No Formatting
       CONVERT  - Converts any dtype to any dtype           - Formates only Date & Time using stypel specifiers
       FORMAT   - Converts any dtype to only string dtype   - Formates date & time and numbers.    
