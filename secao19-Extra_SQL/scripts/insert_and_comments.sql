-- commentary
# commentary
/* commentary */

-- Select the DataBase
USE base_de_dados;

-- Show the tables on DataBase
SHOW tables;
-- Describe the table columns
DESCRIBE users;
-- Insert new registers 
INSERT INTO users (first_name, last_name, email, password_hash) VALUES
("Aurora", "Andrade Garcia", "aurora@email.com", "x_hash"),
("Pedro", "Andrade Garcia", "pedro@email.com", "y_hash");