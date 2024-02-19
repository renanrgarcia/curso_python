-- Select all columns from tables
SELECT * FROM users AS u;
-- Select one or more columns
SELECT 
u.email AS uemail, u.id AS uid, u.first_name AS ufirst_name
FROM users u;