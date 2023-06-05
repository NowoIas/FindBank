import pandas as pd
import numpy as np
import streamlit as st
import folium
from streamlit_folium import st_folium

st.title('Trouvez le point de retrait le plus proche de chez vous !')

df = pd.read_csv('banques-et-distributeurs-de-billets2.csv', sep=';')
df = df.drop(df.columns[0], axis=1)

commune = df['Commune'].unique()
commune_choice = st.sidebar.selectbox('Sélectionner la commune:', commune)

marque = df["Marque"].loc[df["Commune"] == commune_choice]
marque = marque.unique()
marque_choice = st.sidebar.selectbox("Sélectionner l'établissement:", marque)

type = df["type"].loc[(df["Marque"] == marque_choice) & (df["Commune"] == commune_choice)]
type = type.unique()
type_choice = st.sidebar.selectbox('Sélectionner le type:', type)

df = df.loc[(df['Commune']==commune_choice) & (df['Marque']==marque_choice) & (df['type']==type_choice)]

m = folium.Map(location=[50.633333, 3.066667], zoom_start=10)

for index, row in df.iterrows():
    geo_coor = [float(num) for num in row['Geo Point'].split(',')]
    folium.Marker(geo_coor, popup=f"{row['type']} de {row['Marque']} à {row['Commune']}.").add_to(m)

st_folium(m, width=725)
