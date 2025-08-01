import os
import requests
import schedule
import time
from datetime import datetime
from bs4 import BeautifulSoup
from gtts import gTTS
from moviepy.editor import *
from dotenv import load_dotenv
import pytz

# Charger les variables d'environnement
load_dotenv()

# Fuseau horaire
TIMEZONE = pytz.timezone('Africa/Lome')

# Paramètres de l'offre
SITE_EMPLOI_URL = "https://example.com/jobs"  # Remplace avec la vraie URL
NB_OFFRES = 5

# Dossier de sortie
OUTPUT_DIR = "videos"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_today_date():
    return datetime.now(TIMEZONE).strftime('%Y-%m-%d')


def extraire_offres():
    print(f"[{get_today_date()}] 🔍 Extraction des offres...")
    try:
        response = requests.get(SITE_EMPLOI_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        offres = []

        # 🔧 Exemple d'extraction — à adapter selon le site visé
        for i, card in enumerate(soup.select(".job-card")):
            if i >= NB_OFFRES:
                break
            titre = card.select_one(".job-title").text.strip()
            lieu = card.select_one(".job-location").text.strip()
            date_pub = card.select_one(".job-date").text.strip()
            offres.append(f"{titre} à {lieu} (publiée le {date_pub})")
        return offres

    except Exception as e:
        print(f"⚠️ Erreur lors de l'extraction : {e}")
        return []


def generer_audio(offres, audio_path):
    print("🔊 Génération audio...")
    texte = "\n".join(offres)
    tts = gTTS(text=texte, lang="fr")
    tts.save(audio_path)


def generer_video(audio_path, video_path):
    print("🎥 Création de la vidéo...")
    image = ImageClip("static/fond.jpg").set_duration(AudioFileClip(audio_path).duration)
    image = image.set_audio(AudioFileClip(audio_path))
    image.write_videofile(video_path, fps=24)


def pipeline():
    today = get_today_date()
    offres = extraire_offres()

    if not offres:
        print("❌ Aucune offre trouvée.")
        return

    audio_path = os.path.join(OUTPUT_DIR, f"offres_{today}.mp3")
    video_path = os.path.join(OUTPUT_DIR, f"offres_{today}.mp4")

    generer_audio(offres, audio_path)
    generer_video(audio_path, video_path)
    print(f"✅ Vidéo créée avec succès : {video_path}")


# 🕒 Planification (3 vidéos/jour : matin, midi, soir)
schedule.every().day.at("05:00").do(pipeline)
schedule.every().day.at("12:00").do(pipeline)
schedule.every().day.at("19:00").do(pipeline)

print("🚀 Bot lancé. En attente des horaires...")

while True:
    schedule.run_pending()
    time.sleep(30)
