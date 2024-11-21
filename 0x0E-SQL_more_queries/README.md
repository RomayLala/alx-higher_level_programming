# SQL - More Queries

This project contains a series of SQL scripts to demonstrate the use of queries, privileges, user management, and relationships in MySQL. Below is the list of tasks and their corresponding SQL files.

## List of SQL Files and Tasks

1. **0-privileges.sql**  
   Script to list all MySQL privileges for a specific user.
   
2. **1-create_user.sql**  
   Script to create a new MySQL user.

3. **2-create_read_user.sql**  
   Script to create a MySQL user with read-only privileges.

4. **3-force_name.sql**  
   Script to create a database with specific naming constraints.

5. **4-never_empty.sql**  
   Script to create a table ensuring a column is never empty.

6. **5-unique_id.sql**  
   Script to create a table with unique constraints on IDs.

7. **6-states.sql**  
   Script to create a `states` table with proper columns.

8. **7-cities.sql**  
   Script to create a `cities` table and establish a relationship with the `states` table.

9. **8-cities_of_california_subquery.sql**  
   Script to find all cities in the state of California using subqueries.

10. **9-cities_by_state_join.sql**  
    Script to list cities and their states using a SQL JOIN.

11. **10-genre_id_by_show.sql**  
    Script to list TV shows and their genre IDs from the database.

12. **11-genre_id_all_shows.sql**  
    Script to list all TV shows and their genres, including NULL for shows without a genre.

13. **12-no_genre.sql**  
    Script to list all TV shows that do not have a genre linked.

14. **13-count_shows_by_genre.sql**  
    Script to count the number of TV shows linked to each genre.

15. **14-my_genres.sql**  
    Script to list all genres of the show *Dexter*.

16. **15-comedy_only.sql**  
    Script to list all Comedy shows from the database.

17. **16-shows_by_genre.sql**  
    Script to list all TV shows and their genres, including NULL for shows without a genre.
