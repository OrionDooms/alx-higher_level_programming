--creates the table force_name on the MySQL serve.
CREATE TABLE IF NOT EXISTS `force_name`(
	`id` INT NOT NULL, `name` VARCHAR(256) NOT NULL, PRIMARY KEY (id));
