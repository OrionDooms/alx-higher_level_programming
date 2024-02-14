-- A script that create a database if it does not already exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table if it does not already exists in this database.
USE hbtn_0d_usa;
-- A description of cities table.
CREATE TABLE IF NOT EXISTS cities(
        `id` INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
	`state_id` INT NOT NULL,
        `name` VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id));
