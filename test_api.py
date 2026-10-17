import requests

# URL de l'API Vélib Métropole (données en temps réel)
url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=3"

# Envoi de la requête HTTP GET
response = requests.get(url)

# Vérification du statut HTTP (200 = Succès)
if response.status_code == 200:
    data = response.json()
    print("Connexion API réussie !\n")
    # Affichage du premier enregistrement (une station)
    print(data["results"][0])
else:
    print(f"Erreur HTTP : {response.status_code}")