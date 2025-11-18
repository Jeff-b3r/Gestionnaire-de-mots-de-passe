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

### 5 - Ajout d'un mot de passe
- **dépend de 1 et 4**.

### 6 - Affichage d'un mot de passe
- **dépend de 1 et 4**.
-   Affiche les mots de passe, avec l'identifiant mémorisé et l'URL associée

### 7 - Edition d'un mot de passe
- **dépend de 1, 4 et 5**.
-   Modifie un mot de passe dans le gestionnaire

### 8 - Suppresion d'un mot de passe
- **dépend de 1 et 5**.

### 9 - Recherche d'un mot de passe
- **dépend de 1 et 4**.
-   Recherche d'un mot de passe à partir du nom du site ou d'un URL
  

## Fonctionnalités supplémentaires 
### 10 - Copie du mot de passe dans le presse-papier. 
- **dépend de 1 et 4**.

### 11 - Génération automatique d'un mot de passe sécurisé.
- Permet au gestionnaire de mot de passe de générer un mot de passe robuste.

### 12 - Création d'une date d'ajout 
- **dépend de 4 et 5**.
- Permet de connaitre la date de création ou de modification d'un mot de passe

## Briques logicielles
### 1 - Initialisation du magasin de mot de passe
- `os/os.path`: crée le répertoire
- `gnupg` : génère, stocke et utilise une clé GPG

### 2 - Chiffrement et déchiffrement des mots de passe du fichier
- `os` : lecture/écriture des fichiers avant chiffrement
- `gpg-agent` : gère la demande passphrase

### 3 - Authentification de l'utilisateur via GPG 
- `gnupg`
- `gpg-agent` : stocke le passphrase temporairement

### 4 - Mémorisation du nom d'utilisateur et du mot de passe donné selon l'url.
- `os` : enregistre un fichier par URL
- `gnupg`: chiffre le fichier en gpg

### 5 - Ajout d'un mot de passe
- `os/open()`: créer un fichier temporaire
- `gnupg`: chiffre le fichier en gpg

### 6 - Affichage d'un mot de passe
- `gnupg`: déchiffre le fichier
- `glob`: liste les fichiers

### 7 - Edition d'un mot de passe
- `gnupg`: déchiffre le fichier gpg, rechiffre et écrase l'ancien fichier
- `open()`: modification du contenu

### 8 - Suppresion d'un mot de passe
- `os.remove()`: supprime le fichier

### 9 - Recherche d'un mot de passe
- `re`: filtrer par URL, nom de site, identifiant.
- `glob`

### 10 - Copie du mot de passe dans le presse-papier.
- `pyperclip` : copie le mot de passe et colle dans le presse-papier

### 11 - Génération automatique d'un mot de passe sécurisé.
- `secrets` : génère une chaine de caractères cryptographiquement sûre
- `string` : fournit l'ensemble des caractères (lettres, chiffres, symboles...)

### 12 - Création d'une date d'ajout
- `datetime` : génère la date actuelle
- `re` : met à jour une date (lors d'une modification)
