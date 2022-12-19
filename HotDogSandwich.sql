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
INSERT INTO "buns" VALUES (1,400,'Made from white Bread');
INSERT INTO "buns" VALUES (2,350,'Made from wheat Bread');
INSERT INTO "meats" VALUES (1,350,'Pork');
INSERT INTO "meats" VALUES (2,300,'Turkey');
INSERT INTO "condiment" VALUES (1,10,'Mustard');
INSERT INTO "condiment" VALUES (2,12,'ketchup');

INSERT INTO "HotDog" ("dogID", "name", "bun", "meat", "condiments", "story")
VALUES (1, 'Classic Hot Dog', 1, 1, 1, 'A classic hot dog with a bun made from white bread, pork meat, and mustard condiment.');

INSERT INTO "HotDog" ("dogID", "name", "bun", "meat", "condiments", "story")
VALUES (2, 'Turkey Hot Dog', 2, 2, 2, 'A hot dog with a bun made from wheat bread, turkey meat, and ketchup condiment.');

COMMIT;
