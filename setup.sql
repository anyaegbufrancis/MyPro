-- run this file by typing sqlite3 -cmd ".read setup.sql" from your terminal

-- this will be the name of your database
.open project.db
-- for nicer looking output
.mode box


-- drop the tables
DROP TABLE IF EXISTS "nba";
-- create your tables
CREATE TABLE IF NOT EXISTS nba (
	id  INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    points integer NOT NULL,
    assists integer NOT NULL,
    reb integer NOT NULL,
    team TEXT NOT NULL
);

-- add some starter data to your tables using INPUT statemtns
INSERT INTO nba (name, points, assists, reb, team) VALUES
    ("Luka Doncic", 2370, 686, 647, "Dallas Mavericks"),
    ("Jayson Tatum", 1987, 364, 601, "Boston Celtics"),
    ("Steph Curry", 1956, 379, 330, "Golden States Warriors"),
    ("Lebron James", 1822, 589, 518, "Los Angles Lakers");
-- show all the starter data
