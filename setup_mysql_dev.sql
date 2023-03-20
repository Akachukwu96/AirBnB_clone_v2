--  prepares a MySQL server for the project
-- database = hbnb_dev_db
-- A new user hbnb_dev (in localhost)
--  password of hbnb_dev should be set to hbnb_dev_pwd

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_shema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
