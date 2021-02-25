# OLS Linear Regression with Statsmodel
This is a code bit for performing OLS linear regression on a csv data set with the statsmodel api.

## Installation

This is just a placeholder, if you want to see the real deal reach out to me and get access to the google collab file.

## Usage

Takes in a csv file and maps it to a pandas data frame. Uses the data frame to build the regression model and prints out the model details and approximations. 

Piece from the apartment prices data set: 
```python
import statsmodels.api as sm
X = df[['--','---','complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr','----']]
y = df['medianComplexValue']
X = sm.add_constant(X)
X.head()
est = sm.OLS(y, X).fit()
est.summary()
```

## Contributing
No.
