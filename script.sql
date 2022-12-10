-- create the taco_base table
CREATE TABLE taco_base (
  id INTEGER PRIMARY KEY,
  base TEXT NOT NULL,
  filling TEXT NOT NULL,
  topping TEXT NOT NULL
);

-- create the taco_condiments table
CREATE TABLE taco_condiments (
  id INTEGER PRIMARY KEY,
  condiment TEXT NOT NULL,
  shell TEXT NOT NULL,
  filling TEXT NOT NULL
);