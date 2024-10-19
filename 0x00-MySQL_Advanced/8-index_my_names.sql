-- Write a SQL script that creates an index idx_name_first
-- `on the table names and the first letter of name.
CREATE INDEX idx_name_first ON names (SELECT SUBSTRING(name, 1, 1) AS first_letter)
