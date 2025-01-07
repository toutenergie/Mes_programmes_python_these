import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("ViSUALISATION DES DONNEES METREOLOGIQUE DE LA CENTRALE DE BOKHOL")
st.subheader("Abdoulaye FAYE")
st.markdown("***Afichage des graphes***")

distribution = np.random.normal(size=1000)
st.line_chart(distribution)

# diagramme en barre
bar_data = pd.DataFrame(
    [100,19,88,54],
    ["A","B","c","d"]
)
st.bar_chart(bar_data)
file_path = r"A:\Mes_Documents_de_these\DOCUMENTS_RECHERCHE\DOCUMENTS_DE_REPPORTS\Mes_programmes_python_these\EXERCICESPYTHONS\renforcement\centralebokhol.xlsx"

data = pd.read_excel(file_path)


#creation de colonnes