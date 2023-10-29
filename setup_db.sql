-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS boardly;
CREATE USER IF NOT EXISTS 'boardly_dev'@'localhost' IDENTIFIED BY 'boardly_dev_pwd';
GRANT ALL PRIVILEGES ON `boardly`.* TO 'boardly_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'boardly_dev'@'localhost';
FLUSH PRIVILEGES;
