# Gestionnaire-de-mots-de-passe

## Nom du groupe : JR

### Membres : 
- Roland Ung 20231933
- Jeff Bernabeo 20232406

## Fonctionnalités indispensables 
### 1 - Initialisation du magasin de mot de passe
- Création du répertoire local ~/.password-store via init.
- Utilisation d’une clé GPG existante pour le chiffrement.
- `pathlib`: crée le répertoire
- `os`: configure les permissions du dossier
- `gnupg` : génère, stocke et utilise une clé GPG

### 2 - Chiffrement et déchiffrement des mots de passe du fichier
- Chiffrement et déchiffrement des mots de passe avec `gnupg`
- Chaque mot de passe est stocké dans un fichier .gpg chiffré.
- Le déchiffrement est déclenché lors de la lecture avec show et edit. 

### 3 - Authentification de l'utilisateur via GPG 
- L’accès aux mots de passe est protégé par la passphrase de la clé GPG.
- Cette passphrase joue le rôle de mot de passe maître.
- `getpass`: entre le passphrase de manière sécurisé

### 4 - Mémorisation du nom d'utilisateur et du mot de passe donné selon l'url.
- **dépend de 1**.
- `json`: convertit le dictionnaire python en json

### 5 - Ajout d'un mot de passe
- **dépend de 1 et 4**.
- `getpass`: entre le mot de passe
- `os`: configure les permissions du fichier

### 6 - Affichage d'un mot de passe
- **dépend de 1 et 4**.
-   Affiche les mots de passe, avec l'identifiant mémorisé et l'URL associée
- `json`: convertit le json en dictionnaire python

### 7 - Edition d'un mot de passe
- **dépend de 1, 4 et 5**.
-   Modifie un mot de passe dans le gestionnaire
- `json`: convertit le json en dictionnaire python
- `getpass`: entre le nouveau mot de passe
- `os`: reconfigure les permissions du fichier

### 8 - Suppresion d'un mot de passe
- **dépend de 1 et 5**.
- `pathlib`: supprime le fichier

### 9 - Liste et recherche d'un mot de passe
- **dépend de 1 et 4**.
- Liste et recherche d'un mot de passe par le nom de fichier
- `glob`: filtrer les fichiers par l'extension .gpg

## Fonctionnalités supplémentaires 
### 10 - Copie du mot de passe dans le presse-papier.
- **dépend de 1 et 4**.
- `pyperclip` : copie le mot de passe et colle dans le presse-papier

### 11 - Génération automatique d'un mot de passe sécurisé.
- Permet au gestionnaire de mot de passe de générer un mot de passe robuste.
- `secrets` : génère une chaine de caractères cryptographiquement sûre
- `string` : fournit l'ensemble des caractères (lettres, chiffres, symboles...)

### 12 - Création d'une date d'ajout
- **dépend de 4 et 5**.
- Permet de connaitre la date de création ou de modification d'un mot de passe
- `datetime` : génère la date actuelle


