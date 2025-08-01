import os
from datetime import datetime

# Dossier où seront stockées les vidéos prêtes à être uploadées
DOSSIER_SORTIE = "data/videos_generees"

def generer_nom_fichier(titre_offre):
    """Crée un nom de fichier unique à partir du titre de l'offre."""
    nom_base = titre_offre.lower().replace(" ", "_").replace(",", "")
    date_str = datetime.today().strftime("%Y%m%d")
    return f"{nom_base}_{date_str}.mp4"

def generer_clip_depuis_offre(offre):
    """
    Simule la génération d'un clip vidéo pour une offre d'emploi.
    (Tu brancheras Canva ou CapCut API plus tard ici.)
    """
    if not os.path.exists(DOSSIER_SORTIE):
        os.makedirs(DOSSIER_SORTIE)

    nom_fichier = generer_nom_fichier(offre["titre"])
    chemin_fichier = os.path.join(DOSSIER_SORTIE, nom_fichier)

    with open(chemin_fichier, "w") as f:
        f.write(f"🎥 Vidéo simulée pour l'offre : {offre['titre']}\n")
        f.write(f"📍 Lieu : {offre['lieu']}\n")
        f.write(f"🏢 Organisation : {offre['organisation']}\n")
        f.write(f"🗓️ Publié le : {offre['date_publication']}\n\n")
        f.write(f"💼 Description : {offre['description']}\n")

    return chemin_fichier
