from google.colab import files
uploaded = files.upload()

import numpy as np
import pandas as pd
import io
print(len(uploaded))
df = pd.read_csv(io.StringIO(uploaded['apartmentComplexData.csv'].decode('utf-8')))
df.head()

import statsmodels.api as sm
X = df[['--','---','complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr','----']]
y = df['medianComplexValue']
X = sm.add_constant(X)
X.head()
est = sm.OLS(y, X).fit()
est.summary()

predictions = est.predict(X) 
print (predictions)