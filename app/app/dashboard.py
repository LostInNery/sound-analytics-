import pandas as pd
import streamlit as st

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://admin:admin@postgres:5432/soundanalytics"
)

query = """
SELECT *
FROM plays_analytics
"""

df = pd.read_sql(query, engine)

st.title("🎵 Sound Analytics")

st.metric(
    "Total de Reproduções",
    len(df)
)

st.subheader(
    "Top Artistas"
)

st.bar_chart(
    df["artista"].value_counts()
)

st.subheader(
    "Top Gêneros"
)

st.bar_chart(
    df["genero"].value_counts()
)

st.subheader(
    "Dados Processados"
)

st.dataframe(df)
