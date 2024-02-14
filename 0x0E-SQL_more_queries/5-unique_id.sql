-- Creates a table on the MySQL server and gives unique_id description.
CREATE TABLE IF NOT EXISTS unique_id(
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256));
