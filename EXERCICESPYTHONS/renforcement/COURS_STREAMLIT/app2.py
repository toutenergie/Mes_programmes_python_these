import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("ViSUALISATION DES DONNEES METREOLOGIQUE DE LA CENTRALE DE BOKHOL")

file_path = r"A:\Mes_Documents_de_these\DOCUMENTS_RECHERCHE\DOCUMENTS_DE_REPPORTS\Mes_programmes_python_these\EXERCICESPYTHONS\renforcement\centralebokhol.xlsx"

data = pd.read_excel(file_path)
#creation de colonnes
col1,col2 = st.columns([0.1,0.1])

with col1:
    observation = st.number_input(label="choisire le nombres d'observation a visialiser",
                                  min_value= 5,
                                  value= 5,
                                  )
    st.write(data.head(observation))
    
with col2:
    fig,ax = plt.subplots()
    titre= st.text_input(label="Donner un titre a cette figure")
    ax.plot(data[data.columns[2]])
    plt.title(titre) 
    st.pyplot(fig)