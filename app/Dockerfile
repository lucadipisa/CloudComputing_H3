# Utilisez l'image Python officielle en tant que base
FROM python:3.8

# Mettez en place l'environnement
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY . .

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour démarrer l'application
CMD ["python", "app.py"]
