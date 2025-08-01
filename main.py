from scrape_offres import collect_offres
from resume_ai import generate_resumes
from video_generator import create_video
from publishers.publish_all import publish_everywhere

def main():
    print("📥 Collecte des offres en cours...")
    offres = collect_offres()
    
    print("🧠 Génération des résumés IA...")
    resumes = generate_resumes(offres)

    print("🎬 Création de la vidéo...")
    video_path = create_video(resumes)

    print("📤 Publication en cours...")
    publish_everywhere(video_path)

    print("✅ Processus complet terminé avec succès.")

if __name__ == "__main__":
    main()
