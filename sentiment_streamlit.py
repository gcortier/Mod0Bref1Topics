import streamlit as st
import requests
from loguru import logger
import os



API_URL = "http://127.0.0.1:9000/"

# === CONFIGURATION LOGURU ===
# Création dossier si n'existe pas
os.makedirs('logs', exist_ok=True)
logger.remove()  # Nettoie la config de base
logger.add(
   	"logs/sentiment_streamlit.log", # use "logs/sentiment_streamlit{time}.log" to use with timestamp
	# Nouveau fichier tous les 500 Mo
   	rotation="500 MB",            
	# Conserver les logs 7 jours
   	retention="7 days",         
# Compresser les anciens logs 
   	# compression="zip",          
# Niveau info
   	level="INFO",               
   	format="{time} {level} {message}"
)
logger.info(f"Starting project sentiment_streamlit")


st.title("Analyseur de sentiment (VADER) NLTK")
texte = st.text_area("Saisissez le texte à analyser (In English PLEEEEEASSSE) :")

# Fonction pour analyser le texte avec gestion des exceptions
def analyse_input_withexceptions(input_text):
    if texte:
        logger.info(f"Texte à analyser: {texte}")
        try:
            response = requests.post(
                f"{API_URL}/analyse_sentiment/",
                json={"texte": input_text})
            # Lève une exception pour les codes d'erreur HTTP (4xx ou 5xx)
            response.raise_for_status() 
            
            sentiment = response.json()
            
            st.write("Résultats de l'analyse :")
            st.write(f"Polarité négative : {sentiment['neg']}")
            st.write(f"Polarité neutre : {sentiment['neu']}")
            st.write(f"Polarité positive : {sentiment['pos']}")
            st.write(f"Score composé : {sentiment['compound']}")
            
            
            
            if sentiment['compound'] >= 0.05 :
                st.write("Sentiment global : Positif 😀")
            elif sentiment['compound'] <= -0.05 :
                st.write("Sentiment global : Négatif 🙁")
            else :
                st.write("Sentiment global : Neutre 😐")
                logger.info(f"Résultats affichés: {sentiment}")

        # traitement de la réponse
        except requests.exceptions.RequestException as e:
            st.error(f"Erreur de connexion à l'API : {e}")
            logger.error(f"Erreur de connexion à l'API : {e}")
        except Exception as e :
            st.error(f"Une erreur est survenue: {e}")
            logger.error(f"Une erreur est survenue: {e}")
    else:
        st.write("Veuillez entrer du texte pour l'analyse.")


if st.button("Analyser"):
    analyse_input_withexceptions(texte)
    
        

