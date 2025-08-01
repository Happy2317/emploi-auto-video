# main.py

import datetime
import random
from core.job_scraper import get_job_data
from core.video_generator import generate_video
from scripts.uploader import upload_video

# 🕰 Planning automatique
production_schedule = {
    3: 1,
    4: 1,
    5: 1,
    12: 3,
    19: 4,
}

def get_current_hour():
    return datetime.datetime.now().hour

def main():
    hour = get_current_hour()
    number_of_videos = production_schedule.get(hour, 0)
    print(f"🕒 Il est {hour}h. On doit créer {number_of_videos} vidéo(s).")

    for i in range(number_of_videos):
        try:
            print(f"▶️ Vidéo {i + 1}")
            job_data = get_job_data()
            video_path = generate_video(job_data, index=i + 1)
            upload_video(video_path)
        except Exception as e:
            print(f"❌ Erreur pendant la création de la vidéo {i + 1} : {e}")

if __name__ == "__main__":
    main()
