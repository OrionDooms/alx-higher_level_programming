-- Create a database hbtn_0d_2 only if it does not already exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create a user user_0d_2 only if it does not already exists and SET a password.
CREATE USER IF NOT EXISTS `user_0d_2`@`localhost` IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT privilege on the database to the user.
GRANT SELECT ON hbtn_0d_2.* TO `user_0d_2`@`localhost`;
