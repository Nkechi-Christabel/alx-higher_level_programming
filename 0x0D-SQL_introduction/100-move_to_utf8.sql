-- Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
-- You need to convert all of the following to UTF8:
    -- Database hbtn_0c_0
    -- Table first_table
    -- Field name in first_table

-- Select the database
USE hbtn_0c_0;

-- Convert the database to UTF-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table to UTF-8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
