-- a SQL script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed.
CREATE TRIGGER reset_email
AFTER UPDATE ON users
FOR EACH ROW
IF NEW.email <> OLD.email THEN
UPDATE users SET valid_email = 0
WHERE id = NEW.id
END IF;
