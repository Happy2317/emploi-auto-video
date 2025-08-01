from datetime import datetime

def recuperer_offres_emploi():
    # Simulation de données : tu pourras brancher une API réelle plus tard
    return [
        {
            "titre": "Chargé de mission développement local",
            "organisation": "UNDP",
            "lieu": "Dakar, Sénégal",
            "date_publication": datetime.today().strftime("%Y-%m-%d"),
            "description": "Appui au développement des communautés locales."
        },
        {
            "titre": "Consultant en gestion de projet",
            "organisation": "Banque Mondiale",
            "lieu": "Abidjan, Côte d’Ivoire",
            "date_publication": datetime.today().strftime("%Y-%m-%d"),
            "description": "Suivi et évaluation des projets en Afrique de l’Ouest."
        },
    ]
