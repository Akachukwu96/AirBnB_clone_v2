--  prepares a MySQL server for the project
-- database = hbnb_dev_db
-- A new user hbnb_test (in localhost)
--  password of hbnb_test should be set to hbnb_test_pwd

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_shema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
