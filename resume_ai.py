import openai
import json

openai.api_key = "sk-xxxx"  # 🔐 Remplace par ta vraie clé API OpenAI

def summarize(texte):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu es un assistant RH qui résume des offres d’emploi pour une vidéo TikTok."},
            {"role": "user", "content": texte}
        ]
    )
    return response.choices[0].message.content.strip()

def generate_resumes(offres):
    resumes = []
    for offre in offres:
        full_text = f"{offre['titre']} à {offre['ville']} chez {offre['entreprise']}. {offre['description']} - {offre['salaire']}"
        resume = summarize(full_text)
        resumes.append({"resume": resume, "url": offre['url']})
    return resumes
