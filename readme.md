# Installation
## Génération de l'environnement virtuel en début de projet
`python -m venv .venv`

## Activation de l'environnement virtuel
- Windows :  `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

## installation des bibliothèques
- `pip install nltk fastapi uvicorn streamlit requests pydantic loguru`

### Téléchargement du lexique VADER :
- `python -c "import nltk; nltk.download('vader_lexicon')"`
  
### Génération requirements.txt à chaque installation de module
- `pip freeze > requirements.txt`

### ou directement : 
- `pip install -r requierements.txt`


## run server uvicorn :
- `uvicorn sentiment_api:app --host 127.0.0.1 --port 9000 --reload`

## Afficher la doc : 
- `http://127.0.0.1:9000/docs`
- ## Afficher redocs : 
- `http://127.0.0.1:9000/redocs`


## lancer le client streamlit:
`streamlit run sentiment_streamlit.py`

## Lancer les tests
Pour exécuter les tests unitaires sur l'API FastAPI :

```powershell
pytest test_sentiment_api.py
```

## Arborescence du projet

```
Mod0Bref1Topics/
├── .venv/                              # Environnement virtuel 
├── sentiment_api.py                    # API FastAPI pour l'analyse de sentiment
├── sentiment_streamlit.py              # Application Streamlit pour l'interface utilisateur
├── requirements.txt                    # Liste des dépendances
├── logs/                               # Dossier pour les logs
│   ├── sentiment_api.log               # Log de l'API FastAPI
│   └── sentiment_streamlit.log         # Log de l'application Streamlit
├── notebook.ipynb                      # Jupyter notebook pour tester le modèle
├── readme.md                           # Ce fichier
```

=> https://github.com/gcortier/Mod0Bref1Topics

## Documentations :
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/) 
- [uvicorn :Documentation](https://www.uvicorn.org/)