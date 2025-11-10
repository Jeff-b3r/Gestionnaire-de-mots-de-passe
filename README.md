# Gestionnaire-de-mots-de-passe

## Nom du groupe : JR

### Membres : 
- Roland Ung 20231933
- Jeff Bernabeo 20232406

  
## Fonctionnalités indispensables 
### 1 - Initialisation du magasin de mots de passe avec pass
- Création du répertoire local ~/.password-store via pass init.
- Génération ou utilisation d’une clé GPG existante pour le chiffrement.
### 2 - Chiffrement et déchiffrement des mots de passe du fichier
- **dépend de 1**.
- Géré automatiquement par pass via GPG.
- Chaque mot de passe est stocké dans un fichier .gpg chiffré.
- Le déchiffrement est déclenché lors de la lecture avec pass show. 
### 3 - Authentification de l'utilisateur via GPG 
- L’accès aux mots de passe est protégé par la passphrase de la clé GPG.
- Cette passphrase joue le rôle de mot de passe maître.
### 4 - Mémorisation du nom d'utilisateur et du mot de passe donné selon l'url.
- **dépend de 1**.
### 5 - Suppression, l'édition, l'affichage et la recherche d'un mot de passe. 
- **dépend de 1 et 4**.
-   Affiche les mots de passe dans le gestionnaire avec l'identifiant mémorisé et l'url.
-   Suppression et édition d'un mot de passe.
-   Recherche d'un mot de passe à partir du nom du site ou d'un d'url.
  

## Fonctionnalités supplémentaires 
### 6 - Copie du mot de passe dans le presse-papier. 
- **dépend de 1 et 4**.
### 7 - Génération automatique d'un mot de passe sécurisé.
- Permet au gestionnaire de mot de passe de générer un mot de passe robuste.
### 8 - Création d'une date d'ajout 
- **dépend de 4 et 5**.
- Permet de connaitre la date de création ou de mofification d'un mot de passe 
