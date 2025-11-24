import os
from pathlib import Path
import gnupg              
import argparse
import stat
import secrets
import string
import getpass
import json
from datetime import datetime
import pyperclip

STORE_DIR_NAME = "password_store"
BASE_DIR = Path(__file__).resolve().parent
STORE_DIR = BASE_DIR / STORE_DIR_NAME


def init_password_store(gpg_key_email, force=False):
    """Initialise le magasin de mots de passe avec chiffrement GPG."""
    
    if not STORE_DIR.exists():
        STORE_DIR.mkdir(mode=0o700, parents=True)
        print(f"Répertoire créé : {STORE_DIR}")
    elif not force:
        print(f"Magasin déjà initialisé dans : {STORE_DIR}")
        return

    gpg = gnupg.GPG()
    keys = gpg.list_keys(secret=True)
    existing_key = None
    
    # Recherche de la clé correspondante
    for key in keys:
        for uid in key.get('uids', []):
            if gpg_key_email in uid:
                existing_key = key
                break
        if existing_key:
            break
    
    if not existing_key:
        print(f"""
        ⚠️  Aucune clé GPG trouvée pour : {gpg_key_email}
        Veuillez créer une clé GPG manuellement :

        1. Exécutez la commande suivante dans votre terminal :
        gpg --full-generate-key

        2. Choisissez les options suivantes :
        - Type de clé : 1 (RSA et RSA)
        - Taille : 2048
        - Validité : 0 (pas d'expiration)
        - Nom réel : Password Store
        - Adresse e-mail : {gpg_key_email}
        - Commentaire : (laissez vide)

        3. Relancez ce script après la création de la clé
        """)
        return
    else:
        print(f"✓ Clé existante trouvée pour : {gpg_key_email}")
    
    # Sauvegarde de la configuration
    config_file = STORE_DIR / ".gpg-id"
    with open(config_file, 'w') as f:
        f.write(gpg_key_email + '\n')
    
    os.chmod(config_file, 0o600)
    
    print("✓ Magasin de mots de passe initialisé avec succès !")
