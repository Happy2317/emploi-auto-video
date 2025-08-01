import os
import requests

def generate_canva_script(job_title, company_name, location):
    return f"""🌟 {job_title} chez {company_name} 📍 {location}
👉 Postule vite sur notre site ou consulte l'offre complète.
#emploi #recrutement #canadajobs"""

def create_video_slide(content, filename="slide.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"✅ Slide script sauvegardé dans {filename}")

if __name__ == "__main__":
    example = generate_canva_script("Développeur Python", "TechNova", "Montréal")
    create_video_slide(example)
