import pandas as pd
import logging
import time

from sqlalchemy import create_engine

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO
)

time.sleep(15)

usuarios = pd.read_csv("data/usuarios.csv")
musicas = pd.read_csv("data/musicas.csv")
plays = pd.read_csv("data/plays.csv")

assert usuarios["id"].is_unique
assert musicas["id"].is_unique

usuarios = usuarios.dropna()
musicas = musicas.dropna()
plays = plays.dropna()

analytics = plays.merge(
    usuarios,
    left_on="usuario_id",
    right_on="id"
)

analytics = analytics.merge(
    musicas,
    left_on="musica_id",
    right_on="id"
)

analytics["timestamp"] = pd.Timestamp.now()

engine = create_engine(
    "postgresql://admin:admin@postgres:5432/soundanalytics"
)

analytics.to_sql(
    "plays_analytics",
    engine,
    if_exists="replace",
    index=False
)

logging.info(
    "Pipeline executado com sucesso"
)

print("Pipeline executado")
