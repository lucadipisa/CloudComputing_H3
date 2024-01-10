# Utilisez l'image MySQL officielle en tant que base
FROM mysql:latest

# Variables d'environnement pour la configuration MySQL
ENV MYSQL_DATABASE projet_db
ENV MYSQL_ROOT_USER root
ENV MYSQL_PASSWORD root
ENV MYSQL_ROOT_PASSWORD root

# Copiez le script d'initialisation SQL
COPY init.sql /docker-entrypoint-initdb.d/
