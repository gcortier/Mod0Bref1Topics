# Installation
`python -m venv .venv`

## Activation de l'environnement virtuel
### Windows
-  `.venv\Scripts\Activate.ps1`

## installation des bibliothèques
- `pip install nltk fastapi uvicorn streamlit requests pydantic loguru`

### Téléchargement du lexique VADER :
- `python -c "import nltk; nltk.download('vader_lexicon')"`
- 
### Génération requirements.txt
- `pip freeze > requirements.txt`

### ou directement : 
- `pip install -r requierements.txt`


## https://fastapi.tiangolo.com/

## run server uvicorn :
- `uvicorn sentiment_api:app --host 127.0.0.1 --port 9000 --reload`

## Afficher la doc : 
- `http://127.0.0.1:9000/docs`
- ## Afficher la redoc : 
- `http://127.0.0.1:9000/redocs`


## lancer le client streamlit:
`streamlit run sentiment_streamlit.py`

=> https://github.com/gcortier/fast_api