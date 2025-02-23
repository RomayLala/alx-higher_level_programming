-- Script to create the user user_0d_1 and grant all privileges

-- Create the user only if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user on the MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply the changes immediately
FLUSH PRIVILEGES;
