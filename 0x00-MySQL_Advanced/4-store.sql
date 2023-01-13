-- SQL script that creates a trigger that decreases the
-- quantity of an item after adding a new order
-- Quantity in the table items can be negative.

DROP TRIGGER IF EXISTS store_trig;
CREATE TRIGGER store_trig
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number
WHERE name = New.item_name;
