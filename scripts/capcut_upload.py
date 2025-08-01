import os
import time

def simulate_capcut_upload(video_path):
    if not os.path.exists(video_path):
        print("❌ Vidéo introuvable.")
        return False

    print(f"📤 Téléversement de la vidéo {video_path} vers CapCut en cours...")
    time.sleep(2)  # Simulation du délai
    print("✅ Vidéo téléversée avec succès !")
    return True

if __name__ == "__main__":
    simulate_capcut_upload("output/final_video.mp4")
