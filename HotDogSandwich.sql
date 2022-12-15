BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "HotDog" (
	"Bun"	INTEGER,
	"Condiments"	INTEGER,
	"Toppings"	INTEGER,
	"Meat"	INTEGER
);
CREATE TABLE IF NOT EXISTS "Sandwich" (
	"Bread"	INTEGER,
	"Meat"	INTEGER,
	"Condiments"	INTEGER,
	"Toppings"	INTEGER
);
INSERT INTO "HotDog" VALUES ('Classic hot dog bun','Mustard','Onion','Chicken hot dog');
INSERT INTO "HotDog" VALUES ('Pretzel bun','Ketchup','Sauerkraut','Vegetarian hot dog');
INSERT INTO "HotDog" VALUES ('Wheat hot dog bun','Relish','Pickle slices','Turkey hot dog');
INSERT INTO "HotDog" VALUES ('Bagel bun','Mayonnaise','Jalapeno peppers','Pork hot dog');
INSERT INTO "HotDog" VALUES ('Poppyseed bun','Barbecue Sauce','Cheese','Beef hot dog');
INSERT INTO "Sandwich" VALUES ('White Bread','Turkey','Mayonnaise','Lettus');
INSERT INTO "Sandwich" VALUES ('Whole wheat bread','Ham','Mustard','Cheese');
INSERT INTO "Sandwich" VALUES ('Rye bread','Roast beef','Ketchup','Tomato');
INSERT INTO "Sandwich" VALUES ('Pita bread','Tuna','Relish','Avocodo');
INSERT INTO "Sandwich" VALUES ('Flatbread','Chicken','Olive oil','Onion');
COMMIT;
