-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa
-- create database
CREATE DATABASE
    IF NOT EXISTS `hbtn_0d_usa`;

-- Create table state inthe database
USE `hbtn_0d_usa`;
CREATE TABLE
    IF NOT EXISTS `states` (
	`id`INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`)
	);
