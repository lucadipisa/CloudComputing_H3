-- Création de la base de données
CREATE DATABASE IF NOT EXISTS projet_db;
USE projet_db;

-- Création de la table chaussures
CREATE TABLE IF NOT EXISTS chaussures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prix DECIMAL(10, 2) NOT NULL
);

-- Insertion de quelques exemples de chaussures chères
INSERT INTO chaussures (nom, prix) VALUES
    ('Chaussure de luxe 1', 599.99),
    ('Chaussure de sport haut de gamme', 449.99),
    ('Chaussure élégante en cuir italien', 699.99),
    ('Baskets édition limitée', 799.99),
    ('Chaussure de créateur', 999.99);
