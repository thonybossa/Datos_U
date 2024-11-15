from fastapi import FastAPI, HTTPException
from api.schemas import CoverType
import pandas as pd
import os
import mlflow

# Load model
os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://minio:9000"
os.environ['AWS_ACCESS_KEY_ID'] = 'minioadmin'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'minioadmin'

mlflow.set_tracking_uri("http://mlflow:8083")

model_name = "best_model"
model_prod_uri = "models:/{model_name}/production".format(model_name=model_name)
model = mlflow.pyfunc.load_model(model_uri=model_prod_uri)


# Initialize FastAPI
app = FastAPI()


# Define endpoint for root URL
@app.get("/")
async def root():
    return {"message": "Welcome to the CoverType Prediction API!"}


# Define endpoint for prediction
@app.post("/predict")
async def predict_cover_type(data: CoverType):
    # Perform prediction
    prediction = model.predict(
        [
            [
                data.expediente_invima,
                data.principio_activo,
                data.concentracion,
                data.unidad_base,
                data.unidad_de_dispensacion,
                data.nombre_comercial,
                data.fabricante,
                data.medicamento,
                data.canal,
                data.precio_por_tableta,
                data.factoresprecio,
                data.numerofactor
            ]
        ]
    )
    # Convertir el resultado de la predicción a un diccionario
    prediction_dict = {
        "prediction": str(prediction[0])
    }  # Convertir la predicción a una cadena
    return prediction_dict