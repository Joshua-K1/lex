CREATE DATABASE IF NOT EXISTS `unfiltered`;
CREATE DATABASE IF NOT EXISTS `logs`;
CREATE DATABASE IF NOT EXISTS `filtered`;

GRANT ALL ON `unfiltered`.* to 'user'@'%';
GRANT ALL ON `logs`.* to 'user'@'%';
GRANT ALL ON `filtered`.* to 'user'@'%';
