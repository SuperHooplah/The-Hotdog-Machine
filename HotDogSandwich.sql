BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "HotDog" (
	"dogID"	INTEGER,
	"name"	VARCHAR(255) NOT NULL,
	"bun"	INTEGER NOT NULL,
	"meat"	INTEGER NOT NULL,
	"condiments"	INTEGER NOT NULL,
	"story"	TEXT,
	FOREIGN KEY("meat") REFERENCES "meats"("meatID"),
	FOREIGN KEY("condiments") REFERENCES "condiment"("conID"),
	FOREIGN KEY("bun") REFERENCES "buns"("bunID"),
	PRIMARY KEY("dogID")
);
CREATE TABLE IF NOT EXISTS "buns" (
	"bunID"	INTEGER,
	"calories"	INTEGER NOT NULL,
	"desc"	TEXT,
	PRIMARY KEY("bunID")
);
CREATE TABLE IF NOT EXISTS "meats" (
	"meatID"	INTEGER,
	"calories"	INTEGER NOT NULL,
	"desc"	TEXT,
	PRIMARY KEY("meatID")
);
CREATE TABLE IF NOT EXISTS "condiment" (
	"conID"	INTEGER,
	"calories"	INTEGER NOT NULL,
	"desc"	TEXT,
	PRIMARY KEY("conID")
);
INSERT INTO "buns" VALUES (1,400,'Made from white bread');
INSERT INTO "buns" VALUES (2,350,'Made from wheat bread');
INSERT INTO "meats" VALUES (1,350,'Pork');
INSERT INTO "meats" VALUES (2,300,'Turkey');
INSERT INTO "condiment" VALUES (1,10,'Mustard');
INSERT INTO "condiment" VALUES (2,12,'Ketchup');
COMMIT;
