# Portfolio avec Django (Python)

## Installation
Dans le répertoire racine du projet, exécutez les commandes suivantes :
```powershell
python -m venv env
```

```powershell
env\Scripts\activate
```

```powershell
pip install -r requirements.txt
```

## Configuration
Une fois l'environnement virtuel configuré, effectuer les étapes suivantes à la racine du projet :
- créer un fichier .env, et le remplir selon le fichier .env.example
- créer un fichier db.sqlite3

## Lancement
Une fois le projet configuré, exécutez les commandes suivantes pour lancer l'application :
```
python manage.py migrate
```

```powershell
python manage.py runserver
```
