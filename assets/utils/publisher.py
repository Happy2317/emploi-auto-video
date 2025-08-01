import os
import shutil

def publier_video_sur_dossier_public(video_path, titre):
    dossier_public = os.path.join("public", "videos")
    os.makedirs(dossier_public, exist_ok=True)

    # Nouveau nom de fichier basé sur le titre
    nouveau_nom = titre.lower().replace(" ", "_") + ".mp4"
    destination = os.path.join(dossier_public, nouveau_nom)

    shutil.copy(video_path, destination)
    print(f"✅ Vidéo copiée dans : {destination}")
