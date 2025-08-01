import schedule
import time
from scripts.generate_script import generate_job_script
from scripts.generate_voiceover import generate_voiceover
from scripts.generate_video import generate_video
from scripts.upload_to_tiktok import upload_to_tiktok
from scripts/capcut_upload import simulate_capcut_upload

def job():
    print("🚀 Lancement du processus de génération automatique...")
    generate_job_script()
    generate_voiceover()
    generate_video()
    simulate_capcut_upload("output/final_video.mp4")
    upload_to_tiktok("output/final_video.mp4")
    print("🎉 Processus terminé.\n")

# Planification : 3 vidéos à 5h, 3 à 12h, 4 à 19h
schedule.every().day.at("05:00").do(job)
schedule.every().day.at("05:20").do(job)
schedule.every().day.at("05:40").do(job)
schedule.every().day.at("12:00").do(job)
schedule.every().day.at("12:20").do(job)
schedule.every().day.at("12:40").do(job)
schedule.every().day.at("19:00").do(job)
schedule.every().day.at("19:20").do(job)
schedule.every().day.at("19:40").do(job)
schedule.every().day.at("20:00").do(job)

if __name__ == "__main__":
    print("🕒 Planificateur lancé...")
    while True:
        schedule.run_pending()
        time.sleep(60)
