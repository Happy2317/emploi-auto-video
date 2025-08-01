import json
import datetime

def publish_to_tiktok(video_path, caption):
    print(f"🚀 Publication sur TikTok : {video_path} avec la légende : {caption}")

def publish_to_instagram(video_path, caption):
    print(f"📸 Publication sur Instagram : {video_path} avec la légende : {caption}")

def publish_to_youtube_shorts(video_path, caption):
    print(f"📺 Publication sur YouTube Shorts : {video_path} avec la légende : {caption}")

def main():
    with open("data/offres_du_jour.json", "r", encoding="utf-8") as f:
        offres = json.load(f)

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    video_path = f"videos/emploi_auto_{today}.mp4"
    caption = f"📌 Offres d’emploi du {today} — #emploi #canada #immigration"

    publish_to_tiktok(video_path, caption)
    publish_to_instagram(video_path, caption)
    publish_to_youtube_shorts(video_path, caption)

if __name__ == "__main__":
    main()
