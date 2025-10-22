import streamlit as st
import pandas as pd
import joblib

# --- Cargar el modelo entrenado ---
import joblib
import os

# Cargar el modelo desde la ruta completa
ruta_modelo = r"C:\Users\pandr\OneDrive\Escritorio\Transport\modelo_entrenado.pkl"
model = joblib.load(ruta_modelo)


st.title("🚚 Predicción de Demora en Viajes de Carga")

st.write("Ingrese los datos del viaje para predecir si será **Demorado** o **Ideal**.")

# --- Entradas del usuario ---
naturaleza = st.selectbox("Naturaleza del viaje", ["Carga Normal", "Carga Peligrosa", "Refrigerada"])
hora_salida_cargue = st.number_input("Hora de salida del cargue (0-23)", min_value=0, max_value=23, step=1)
cantidad_remesas = st.number_input("Cantidad de remesas por viaje", min_value=1, step=1)
empresa_transporte = st.selectbox(
    "Empresa de transporte",
    ["3,230", "1,843", "1,976", "150", "539", "546", "3,033", "4,046", "1,148", "227", "335"]
)
# --- Crear dataframe con los datos ingresados ---
df_input = pd.DataFrame({
    'NATURALEZA': [naturaleza],
    'HORA_SALIDA_CARGUE': [hora_salida_cargue],
    'CANTIDAD_REMESAS_VIAJE': [cantidad_remesas],
    'EMPRESA_TRANSPORTE': [empresa_transporte]
})

# --- Predicción ---
if st.button("Predecir"):
    pred = model.predict(df_input)[0]
    if pred == "Demorado":
        st.error("🚨 El viaje probablemente será **DEMORADO**.")
    else:
        st.success("✅ El viaje probablemente será **IDEAL**.")

    st.write("Datos ingresados:")
    st.dataframe(df_input)
    