import numpy as np
import pandas as pd
import io
df = pd.read_csv('/code/app/apartmentComplexData.csv')
df.head()

import statsmodels.api as sm
X = df[['--','---','complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr','----']]
y = df['medianComplexValue']
X = sm.add_constant(X)
X.head()
est = sm.OLS(y, X).fit()
est.summary()

from pydantic import BaseModel

class ApartmentComplex(BaseModel):
    column0: float 
    column1: float 
    complexAge: float 
    totalRooms: float 
    totalBedrooms: float 
    complexInhabitants: float 
    apartmentsNr: float 
    column7: float
    class Config:
        schema_extra = {
            "example": {
                "column0": -122.230000, 
                "column1": 37.880000, 
                "complexAge": 41.000000,
                "totalRooms": 880.000000,
                "totalBedrooms": 129.000000,
                "complexInhabitants": 322.000000,
                "apartmentsNr": 126.000000,
                "column7": 8.325200
            }
        }

from fastapi import FastAPI
import statsmodels.api as sm
import uvicorn

app = FastAPI()

@app.on_event("startup")
def load_model():
    global model
    model = est

@app.get('/')
def index():
    return {'message': 'This is the basepath of the apartment cost prediction api'}


@app.post('/predict')
def get_apartment_complex_details(data:ApartmentComplex):
    received = data.dict()
    column0 = received['column0']
    column1 = received['column1']
    complexAge = received['complexAge']
    totalRooms = received['totalRooms']
    totalBedrooms = received['totalBedrooms']
    complexInhabitants = received['complexInhabitants']
    apartmentsNr = received['apartmentsNr']
    column7 = received['column7']

    data = {'const' : 1.0,'--' : column0, '---' : column1, 'complexAge' : complexAge, 'totalRooms' : totalRooms, 'totalBedrooms' : totalBedrooms, 'complexInhabitants' : complexInhabitants, 'apartmentsNr' : apartmentsNr, '----' : column7}
    X = pd.DataFrame(data, index=[0])
    predictions = model.predict(X) 

    return {'medianComplexValue': predictions[0]}