DROP DATABASE kapperapp;
DROP USER 'kapper'@'localhost';

CREATE DATABASE kapperapp;

USE kapperapp;

CREATE USER 'kapper'@'localhost' IDENTIFIED BY 'K@pp3r';
GRANT ALL PRIVILEGES ON * . * TO 'kapper'@'localhost';


CREATE TABLE afspraak (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    naam VARCHAR (256) NOT NULL,
    email VARCHAR (256) NOT NULL,
    tijdstip DATETIME NOT NULL
    -- To do: kolommen toevoegen
);