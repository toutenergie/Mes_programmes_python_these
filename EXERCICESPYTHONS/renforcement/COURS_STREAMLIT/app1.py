# Projet streamlit
import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r"A:\Mes_Documents_de_these\DOCUMENTS_RECHERCHE\DOCUMENTS_DE_REPPORTS\Mes_programmes_python_these\EXERCICESPYTHONS\renforcement\centralebokhol.xlsx"

data = pd.read_excel(file_path)

# creation de colonnes
col1,col2 = st.columns([0.1,0.1])

with col1:
    st.write(data.head())
    
with col2:
    fig,ax = plt.subplots()
    ax.plot(data[data.columns[2]])
    st.pyplot(fig)
    