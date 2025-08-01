import requests
import json
from datetime import datetime

def collect_offres():
    url = "https://www.jobbank.gc.ca/jobsearch/jobsearch?fsrc=32&sort=M"  # Exemple URL
    # ⚠️ À adapter avec BeautifulSoup si tu veux du scraping plus précis
    offres = [
        {
            "titre": "Cuisinier - LMIA disponible",
            "ville": "Montréal",
            "entreprise": "Restaurant Bon Goût",
            "salaire": "20$/h",
            "description": "Poste temps plein, logement possible",
            "url": "https://www.jobbank.gc.ca/jobsearch/jobposting/123456"
        },
        {
            "titre": "Préposé aux bénéficiaires",
            "ville": "Québec",
            "entreprise": "Résidence du Lac",
            "salaire": "18$/h",
            "description": "Travail de nuit, LMIA offerte",
            "url": "https://www.jobbank.gc.ca/jobsearch/jobposting/654321"
        }
    ]

    date_today = datetime.now().strftime("%Y-%m-%d")
    with open(f"data/offres_du_jour.json", "w", encoding="utf-8") as f:
        json.dump({"date": date_today, "offres": offres}, f, ensure_ascii=False, indent=2)

    return offres
