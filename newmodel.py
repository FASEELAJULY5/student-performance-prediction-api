import joblib
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import numpy as np

model=joblib.load("newmodel.pkl")

app=FastAPI(
    title="Student Performance ML API",
    description="ML prediction API for student performance",
    version="1.0.0"
)
 
class InputData(BaseModel):
    study_hours:float
    attendance:float

@app.get("/")
def home():
    return {"message":"API is working"}


@app.post("/predict")
def predict(data:InputData):
    if data.study_hours < 0:
        raise HTTPException(
            status_code=400,
            detail="study_hours cannot be negative"
        )

    if data.attendance < 0 or data.attendance > 100:
        raise HTTPException(
            status_code=400,
            detail="attendance must be between 0 and 100"
        )


    
    input_data=np.array([[data.study_hours, data.attendance]])
    prediction=model.predict(input_data)
    return{ "study_hours": data.study_hours,
    "attendance": data.attendance,
        "prediction":prediction[0]}

