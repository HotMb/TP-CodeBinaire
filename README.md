# Manipulation d’un code binaire

Petit module Python qui représente une suite non vide de bits avec l’énumération `Bit` et la classe `CodeBinaire`. Le module `reader.py` convertit une chaîne de 0 et de 1 en objet.

## Fonctions

- Ajouter, lire, modifier et supprimer des bits.
- Concaténer deux codes binaires.
- Lire une chaîne ou demander une saisie au terminal.
- Lever une erreur si le code devient vide ou contient un caractère invalide.

## Lancer les tests

Python 3.9 ou plus récent :

```sh
python -m pip install -r requirements.txt
python -m pytest
```

Les tests importent les modules depuis la racine du dépôt.
