import os
from pathlib import Path
import io
import subprocess         
import gnupg              
import glob
import re
import pyperclip
import secrets
import string
from datetime import datetime
import json
import stat

STORE_DIR_NAME = "password_store"
BASE_DIR = Path(__file__).resolve().parent
STORE_DIR = BASE_DIR / STORE_DIR_NAME


def init_password_store(gpg_key_email=None, force=False):
    """Initialise le magasin de mots de passe avec chiffrement GPG."""
    
    if not STORE_DIR.exists():
        STORE_DIR.mkdir(mode=0o700, parents=True)
        print(f"Répertoire créé : {STORE_DIR}")
    elif not force:
        print(f"Magasin déjà initialisé dans : {STORE_DIR}")
        return

    gpg = gnupg.GPG()
    
    if gpg_key_email:
        keys = gpg.list_keys(secret=True)
        existing_key = None
        
        for key in keys:
            for uid in key.get('uids', []):
                if gpg_key_email in uid:
                    existing_key = key
                    break
        
        if not existing_key:
            print(f"Génération d'une clé GPG pour : {gpg_key_email}")
            input_data = gpg.gen_key_input(
                name_real="Password Store",
                name_email=gpg_key_email,
                key_type="RSA",
                key_length=2048,
                expire_date=0
            )
            key = gpg.gen_key(input_data)
            print(f"Clé générée avec l'ID : {key.fingerprint}")
        else:
            print(f"Clé existante trouvée pour : {gpg_key_email}")
    
    config_file = STORE_DIR / ".gpg-id"
    with open(config_file, 'w') as f:
        f.write(gpg_key_email + '\n')
    
    os.chmod(config_file, 0o600)
    
    print("Magasin de mots de passe initialisé avec succès !")

init_password_store(gpg_key_email="user@example.com"); 