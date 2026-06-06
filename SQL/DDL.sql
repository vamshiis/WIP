
/* DDL - (DATA DEFINATION LANGUAGE) 
   - The DDL commands are used to Creating Tables , Altering them and Deleting them.
   - We have this commands in DDL
   1.CREATE
     • Can Create a table with proper schema defination for all columns.
   2.ALTER 
     • Can Add a column (At end)
	 • Can Delete a column
   3.DROP
     • Deletes whole table completely.
*/

/* CREATE 
  - Create a new Table with all the columns
  Create a new table called persons with columns : 
  id, person_name, birth_date and phone.
*/
CREATE TABLE persons (
	id INT NOT NULL,
	person_name VARCHAR(50) NOT NULL,
	birth_date DATE,
	phone VARCHAR(15) NOT NULL,
	CONSTRAINT pk_persons PRIMARY KEY (id)
)

/* ALTER 
     Adding column
   - Can Add the columns to the already existing Table
   - By Default Adds the column at the end of table.
   NOTE : 
     If wanted to insert this new column in between we need to drop everything 
     and create whole table again.
   • Create a new Column called email to the persons table.
*/
ALTER TABLE persons 
ADD email VARCHAR(50) NOT NULL

-- Dropping the column
-- Remove the column phone from the persons table
ALTER TABLE persons
DROP COLUMN phone

SELECT * FROM persons

/* DROP 
     Deleting table 
   - DELETE's the table completely from the database.
   - Also all Data is lost the Table contains.
*/
DROP TABLE persons