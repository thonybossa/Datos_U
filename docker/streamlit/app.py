import streamlit as st
import requests

# Define la URL de tu servidor FastAPI
FASTAPI_URL = 'http://fastapi:8085'

# Define una función para hacer una solicitud de predicción a tu API de FastAPI
def get_prediction(data):
    response = requests.post(f"{FASTAPI_URL}/predict", json=data)
    prediction = response.json()
    return prediction

# Define la interfaz de usuario de la aplicación Streamlit
def main():
    # Configure the Streamlit page layout
    st.set_page_config(layout="wide")

    st.title(':computer: Proyecto 2 MLOPS: Grupo 3 :computer:')
    st.subheader(
        "En este dashboard, encontrará toda la información relacionada con el proyecto 2 de la materia MLOPS"
    )
    st.sidebar.title("Integrantes")
    st.sidebar.write(
        """
        Anthony Bossa \n
        Jose Luis Vega \n
        Víctor De La Hoz
        """
    )
    st.divider()
    st.header(f"Links de interés")
    st.markdown("En esta sección podrá dirigirse tanto al repositorio del equipo como a las direcciones donde estan dispuestos los servicios integrados en la solución")
    _, col2, _, col4, _, col6, _ = st.columns([1, 5, 1, 5, 1, 5, 1])
    with col2:
        st.link_button("Repositorio del equipo", "https://github.com/thonybossa/MLOPS")
    with col4:
        st.link_button("MLFLOW", "http://10.43.101.152:8083")
    with col6:
        st.link_button("AirFlow", "http://10.43.101.152:8080")
    st.divider()
    cols = st.columns(4)

    # Define los campos de entrada
    expediente_invima = cols[0].number_input("Expediente INVIMA", value=123456)
    principio_activo = cols[1].text_input("Principio Activo", value="Paracetamol")
    concentracion = cols[2].text_input("Concentración", value="500mg")
    unidad_base = cols[3].text_input("Unidad Base", value="tableta")
    unidad_de_dispensacion = cols[0].text_input("Unidad de Dispensación", value="blíster")
    nombre_comercial = cols[1].text_input("Nombre Comercial", value="Acetaminofén Genérico")
    fabricante = cols[2].text_input("Fabricante", value="Laboratorios XYZ")
    medicamento = cols[3].text_input("Medicamento", value="Analgesico")
    canal = cols[0].text_input("Canal", value="Farmacia")
    precio_por_tableta = cols[1].number_input("Precio por Tableta", value=0.50)
    factoresprecio = cols[2].text_input("Factores Precio", value="Promoción")
    numerofactor = cols[3].number_input("Número de Factor", value=20)

    # Crea un botón para realizar la predicción
    if st.button('Predecir'):
        # Hace una solicitud de predicción a tu API de FastAPI
        data = {
            "expediente_invima": expediente_invima,
            "principio_activo": principio_activo,
            "concentracion": concentracion,
            "unidad_base": unidad_base,
            "unidad_de_dispensacion": unidad_de_dispensacion,
            "nombre_comercial": nombre_comercial,
            "fabricante": fabricante,
            "medicamento": medicamento,
            "canal": canal,
            "precio_por_tableta": precio_por_tableta,
            "factoresprecio": factoresprecio,
            "numerofactor": numerofactor
        }
        prediction = get_prediction(data)
        
        # Muestra el resultado de la predicción
        st.write('Prediction:', prediction['prediction'])

if __name__ == '__main__':
    main()



