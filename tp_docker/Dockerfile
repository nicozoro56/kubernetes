# Utilisation de l'image Python officielle comme image de base
#FROM python:3.9

# Copie des fichiers de l'application dans le conteneur
#COPY . /app

# Définition du répertoire de travail
#WORKDIR /app

# Installation des dépendances Python
#RUN pip install -r requirements.txt

# Commande par défaut pour exécuter l'application
#CMD ["python", "app.py"]
FROM python:3.10.14-alpine3.19

VOLUME /tmp

WORKDIR /app

COPY src/requirements.txt ./
RUN pip install -r requirements.txt

# Bundle app source
ADD src /app

CMD [ "python", "main.py" ]