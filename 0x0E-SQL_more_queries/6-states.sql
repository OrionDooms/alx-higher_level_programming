-- A script that create a database if it does not already exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table if it does not already exists in this database.
USE hbtn_0d_usa;
-- A description of states table.
CREATE TABLE IF NOT EXISTS states(
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(256) NOT NULL);
