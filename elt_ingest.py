import requests
import pandas as pd
from sqlalchemy import create_engine, text

# 1. Extraction : Récupération de l'ensemble du réseau via l'endpoint d'export JSON
url = "https://opendata.paris.fr/api/v2/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json"
response = requests.get(url)
data = response.json()

# 2. Structure : Conversion en DataFrame pandas
df = pd.DataFrame(data)

# Nettoyage technique : conversion des structures complexes (dict/list) en chaînes de caractères
for col in df.columns:
    if df[col].apply(lambda x: isinstance(x, (dict, list))).any():
        df[col] = df[col].astype(str)

# 3. Connexion à PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/velib_db")

# Suppression en cascade pour débloquer la vue dbt stg_velib existante
with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS raw_velib CASCADE;"))
    conn.commit()

# 4. Écriture : Insertion des données brutes dans raw_velib
df.to_sql("raw_velib", engine, if_exists="replace", index=False)

print(f"Chargement réussi : {len(df)} stations insérées dans 'raw_velib'.")