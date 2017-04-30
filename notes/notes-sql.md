## SQL Notes


### Operadores

- "<" : Menor que
- "<=": Menor ou igual a
- "<>=": Diferente de 
- ">": Maior que
- ">=": Maior ou igual a 
- "!=": Diferente de 
- "!<": Não é menor que
- "!>": Não é maior que


### Create Database
Create new database

<code>CREATE DATABASE databasename;</code>

### Drop Database
Delete database

<code>DROP DATABASE databasename;</code>

### Create Table
Create new table

<code>CREATE TABLE table_name ( </code> <br/>
<code> column1 datatype, </code> <br/>
<code> column2 datatype, </code><br/>
<code> column3 datatype, </code><br/>
); </code>

### Drop Table
Delete Table

<code> DROP TABLE table_name; </code>

### Alter Table
The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.

<code>ALTER TABLE table_name </code>  
<code>ADD column_name datatype; </code>

### Insert Into
The INSERT INTO statement is used to insert new records in a table

<code>INSERT INTO table_name (column1, column2, column3, ...)</code><br/>
<code>VALUES (value1, value2, value3, ...); </code>

or <br/>

<code>INSERT INTO table_name</code> <br/>
<code>VALUES (value1, value2, value3, ...); </code>

### Update 
The UPDATE statement is used to modify the existing records in a table

<code>UPDATE table_name </code> <br/>
<code>SET column1 = value1, column2 = value2, ...</code><br/>
<code>WHERE condition; </code>

### Delete From
The UPDATE statement is used to modify the existing records in a table

<code>DELETE FROM table_name</code><br/>
<code>WHERE condition; </code>

## Aggregate Functions
SQL aggregate functions return a single value, calculated from values in a column.


- AVG() 	Returns the average value
- COUNT() 	Returns the number of rows
- FIRST() 	Returns the first value
- LAST() 	Returns the last value
- MAX() 	Returns the largest value
- MIN() 	Returns the smallest value
- ROUND() 	Rounds a numeric field to the number of decimals specified
- SUM() 	Returns the sum

### COUNT(), AVG() and SUM() Functions
The COUNT() function returns the number of rows (linhas) that matches a specified criteria. <br/>
The AVG() function returns the average (média) value of a numeric column. <br/>
The SUM() function returns the total sum (soma) of a numeric column. <br/>

<code>SELECT COUNT(column_name)</code><br/>
<code>FROM table_name</code><br/>
<code>WHERE condition; </code>

<code>SELECT AVG(column_name)</code><br/>
<code>FROM table_name</code><br/>
<code>WHERE condition; </code>

<code>SELECT SUM(column_name)</code><br/>
<code>FROM table_name</code><br/>
<code>WHERE condition; </code>

### MIN() and MAX()
The MIN() function returns the smallest value of the selected column. <br/>
The MAX() function returns the largest value of the selected column. <br/>

<code>SELECT MIN(column_name)</code><br/>
<code>FROM table_name</code><br/>
<code>WHERE condition; </code>

<code>SELECT MAX(column_name)</code><br/>
<code>FROM table_name</code><br/>
<code>WHERE condition; </code>


### Group By
The GROUP BY statement is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.

<code>SELECT column_name(s), aggregate_function(column_name)</code><br/>
<code>FROM table_name</code><br/>
<code>GROUP BY column_name(s); </code>

Ex:
<code>SELECT genre, sum(cost)</code><br/>
<code>FROM Movies</code><br/>
<code>GROUP BY genre; </code>

### Having
The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.

<code>SELECT column_name(s)</code><br/>
<code>FROM table_name</code><br/>
<code>WHERE condition</code><br/>
<code>GROUP BY column_name(s)</code><br/>
<code>HAVING aggregate_function(column_name) operator value; </code>

Sources: <br/>
https://www.w3schools.com/sql/default.asp <br/>
https://msdn.microsoft.com/pt-br/library/ms176020.aspx<br/>
https://www.codeschool.com/courses/try-sql
