from fastapi import FastAPI, File, UploadFile
import pandas as pd
from pydantic import BaseModel
from typing import List, Dict
from io import StringIO
import joblib  # Библиотека для загрузки моделей
from utils import preprocess_data  # Импортируем функцию предобработки
import logging



# Создаем экземпляр FastAPI
app = FastAPI()

# Загрузка предварительно обученной модели
model = joblib.load("model.joblib")

class PredictionResponse(BaseModel):
    id: int
    prediction: float

# Настройка логгера
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Обрабатываем загруженный CSV-файл, применяем модель и возвращаем результат.
    
    :param file: Загружаемый CSV-файл
    :return: Список предсказанных значений в формате JSON
    """
    try:
        # Чтение CSV-файла
        df = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-8')
        
        # Логируем событие приёма файла
        logger.debug("Received file for prediction.")

        # Предобработка данных
        preprocessed_df = preprocess_data(df)
        
        # Применение модели для предсказания
        predictions = model.predict(preprocessed_df)
        
        # Форматируем результат
        results = [
            {"id": i, "prediction": float(pred)} 
            for i, pred in enumerate(predictions)
        ]
        
        return {"predictions": results}
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return {"error": str(e)}