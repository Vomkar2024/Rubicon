-- Create and select your database
CREATE DATABASE IF NOT EXISTS Rubicon;
USE Rubicon;

-- Create table
CREATE TABLE demo (
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    address VARCHAR(20),
    city VARCHAR(20),
    idnumber INT
);


SELECT * FROM demo;

-- Alter table structure
ALTER TABLE demo
ADD salary NUMERIC;

-- Update data
UPDATE demo
SET salary = 2000000
WHERE firstname = 'John';