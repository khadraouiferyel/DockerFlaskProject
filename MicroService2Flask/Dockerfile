# Étape 1 : Utiliser une image de base légère avec Python
FROM python:3.9-slim

# Étape 2 : Définir le répertoire de travail
WORKDIR /app

# Étape 3 : Copier les fichiers du projet dans le conteneur
COPY . /app

# Étape 4 : Installer les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Exposer le port 5001 pour accéder à l'API
EXPOSE 5002

# Étape 6 : Lancer l'application Flask
CMD ["python", "vgg_service.py"]
