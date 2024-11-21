# SQL Introduction - Project 0x0D

This project is part of the ALX Higher Level Programming curriculum. It covers basic SQL operations such as database creation, table management, data insertion, and querying.

## Project Overview

In this project, we will be writing several SQL scripts to perform various database operations on a MySQL server. The tasks cover common SQL operations including:
- Creating and removing databases and tables.
- Inserting, updating, and deleting records.
- Querying and filtering records.
- Working with aggregate functions and sorting.

## Tasks

Below is a brief description of each task and what the corresponding SQL script does:

1. **Create a Database**:  
   Creates a database called `hbtn_0c_0` if it does not already exist.
   
2. **Remove a Database**:  
   Deletes the database `hbtn_0c_0` if it exists.

3. **List Tables in a Database**:  
   Lists all tables of a specific database.

4. **Create a Table**:  
   Creates a table `first_table` with columns `id` (INT) and `name` (VARCHAR(256)).

5. **Describe a Table**:  
   Retrieves the full description of the `first_table` (excluding the `DESCRIBE` or `EXPLAIN` commands).

6. **List All Rows in a Table**:  
   Lists all rows of the `first_table`.

7. **Insert a Row into a Table**:  
   Inserts a row into the `first_table` with the values `id = 89` and `name = "Best School"`.

8. **Count Records**:  
   Counts the number of rows in `first_table` where the `id = 89`.

9. **Create Another Table**:  
   Creates a table `second_table` with columns `id`, `name`, and `score`, and inserts multiple rows into the table.

10. **List Records Ordered by Score**:  
    Lists records from `second_table`, showing `score` and `name`, ordered by the `score` in descending order.

11. **Filter Records by Score**:  
    Lists records where the `score >= 10` from `second_table`.

12. **Update Record in Table**:  
    Updates the `score` of Bob to `10` in `second_table` (without using Bob's `id`).

13. **Remove Records from Table**:  
    Removes records from `second_table` where `score <= 5`.

14. **Compute Average Score**:  
    Calculates the average of the `score` values in `second_table`.

15. **Group and Count by Score**:  
    Lists each unique score in `second_table` and the count of records for each score, ordered by the count of records (in descending order).

16. **List Records in Descending Order**:  
    Lists all records from `second_table` ordered by `score` in descending order, ensuring no rows without a name are shown.
