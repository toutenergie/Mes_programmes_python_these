import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Titre de l'application
st.title("Optimisation des paramètres du VSG en temps réel")

# --- Entrée des données du réseau ---
st.sidebar.header("Données du Réseau")
frequence = st.sidebar.slider("Fréquence (Hz)", 49.0, 51.0, 50.0, 0.01)
delta_f = st.sidebar.slider("Variation de Fréquence (Hz/s)", -1.0, 1.0, 0.0, 0.01)
tension = st.sidebar.slider("Tension (V)", 210, 250, 230, 1)
charge = st.sidebar.slider("Charge (MW)", 0, 500, 250, 10)
puissance_active = st.sidebar.slider("Puissance Active du VSG (MW)", 0, 100, 50, 5)
puissance_reactive = st.sidebar.slider("Puissance Réactive du VSG (MVAR)", -50, 50, 0, 5)

# --- Modèle d'optimisation simple ---
# Création d'un modèle linéaire fictif (peut être remplacé par du Machine Learning avancé)
df = pd.DataFrame({
    "frequence": np.random.uniform(49, 51, 100),
    "delta_f": np.random.uniform(-1, 1, 100),
    "tension": np.random.uniform(210, 250, 100),
    "charge": np.random.uniform(0, 500, 100),
    "puissance_active": np.random.uniform(0, 100, 100),
    "puissance_reactive": np.random.uniform(-50, 50, 100),
    "H": np.random.uniform(2, 10, 100),  # Inertie virtuelle
    "D": np.random.uniform(0.1, 1, 100),  # Amortissement
})

X = df[["frequence", "delta_f", "tension", "charge", "puissance_active", "puissance_reactive"]]
y_H = df["H"]
y_D = df["D"]

model_H = LinearRegression().fit(X, y_H)
model_D = LinearRegression().fit(X, y_D)

# Prédiction des paramètres optimaux
X_input = np.array([[frequence, delta_f, tension, charge, puissance_active, puissance_reactive]])
inertie_opt = model_H.predict(X_input)[0]
amortissement_opt = model_D.predict(X_input)[0]

# --- Affichage des résultats ---
st.subheader("Paramètres Optimisés du VSG")
st.write(f"**Inertie Virtuelle (H) :** {inertie_opt:.2f} s")
st.write(f"**Coefficient d'Amortissement (D) :** {amortissement_opt:.2f}")

# --- Graphique des résultats ---
st.subheader("Visualisation des Paramètres")
data = pd.DataFrame({"Paramètre": ["Inertie H", "Amortissement D"], "Valeur": [inertie_opt, amortissement_opt]})
st.bar_chart(data.set_index("Paramètre"))

st.write("\n\n**Prochaines améliorations possibles :** Ajout d'un modèle avancé avec Machine Learning et optimisation par PSO ou RL.")