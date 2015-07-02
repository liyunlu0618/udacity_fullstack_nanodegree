-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop database tournament;

create database tournament;

\c tournament

create table players (
	id	serial PRIMARY KEY,
	name	varchar(80)
);

create table matches (
	id	serial PRIMARY KEY,
	winner_id	integer,
	loser_id	integer
);
