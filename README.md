# Gestionnaire-de-mots-de-passe

## Nom du groupe : JR

### Membres : 
- Roland Ung 20231933
- Jeff Bernabeo 20232406

## Fonctionnalités indispensables 
### 1 - Initialisation du magasin de mot de passe
- Création du répertoire local ~/.password-store via init.
- Utilisation d’une clé GPG existante pour le chiffrement.
- `os/os.path`: crée le répertoire
- `gnupg` : génère, stocke et utilise une clé GPG

### 2 - Chiffrement et déchiffrement des mots de passe du fichier
- Chiffrement et déchiffrement des mots de passe avec gpg 
- Chaque mot de passe est stocké dans un fichier .gpg chiffré.
- Le déchiffrement est déclenché lors de la lecture avec show. 
- `os` : lecture/écriture des fichiers avant chiffrement

### 3 - Authentification de l'utilisateur via GPG 
- L’accès aux mots de passe est protégé par la passphrase de la clé GPG.
- Cette passphrase joue le rôle de mot de passe maître.
- `gnupg`

### 4 - Mémorisation du nom d'utilisateur et du mot de passe donné selon l'url.
- **dépend de 1**.
- `os` : enregistre un fichier par URL
- `gnupg`: chiffre le fichier en gpg

### 5 - Ajout d'un mot de passe
- **dépend de 1 et 4**.
- `os/open()`: créer un fichier 
- `gnupg`: chiffre le fichier en gpg

### 6 - Affichage d'un mot de passe
- **dépend de 1 et 4**.
-   Affiche les mots de passe, avec l'identifiant mémorisé et l'URL associée
- `gnupg`: déchiffre le fichier
- `glob`: liste les fichiers

### 7 - Edition d'un mot de passe
- **dépend de 1, 4 et 5**.
-   Modifie un mot de passe dans le gestionnaire
- `gnupg`: déchiffre le fichier gpg, rechiffre et écrase l'ancien fichier
- `open()`: modification du contenu

### 8 - Suppresion d'un mot de passe
- **dépend de 1 et 5**.
- `os.remove()`: supprime le fichier

### 9 - Liste et recherche d'un mot de passe
- **dépend de 1 et 4**.
- Liste et recherche d'un mot de passe à partir du nom du site
- `string`: filtrer par nom de site

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


