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

Regression model details:

OLS Regression Results
Dep. Variable:	medianComplexValue	R-squared:	0.637
Model:	OLS	Adj. R-squared:	0.637
Method:	Least Squares	F-statistic:	4528.
Date:	Thu, 25 Feb 2021	Prob (F-statistic):	0.00
Time:	17:28:01	Log-Likelihood:	-2.5941e+05
No. Observations:	20640	AIC:	5.188e+05
Df Residuals:	20631	BIC:	5.189e+05
Df Model:	8		
Covariance Type:	nonrobust		
coef	std err	t	P>|t|	[0.025	0.975]
const	-3.594e+06	6.25e+04	-57.468	0.000	-3.72e+06	-3.47e+06
--	-4.282e+04	713.008	-60.061	0.000	-4.42e+04	-4.14e+04
---	-4.258e+04	673.257	-63.240	0.000	-4.39e+04	-4.13e+04
complexAge	1156.3039	43.167	26.787	0.000	1071.693	1240.915
totalRooms	-8.1816	0.788	-10.381	0.000	-9.726	-6.637
totalBedrooms	113.4107	6.902	16.432	0.000	99.882	126.939
complexInhabitants	-38.5351	1.079	-35.716	0.000	-40.650	-36.420
apartmentsNr	48.3083	7.515	6.429	0.000	33.579	63.037
----	4.025e+04	335.060	120.123	0.000	3.96e+04	4.09e+04
Omnibus:	4940.460	Durbin-Watson:	0.974
Prob(Omnibus):	0.000	Jarque-Bera (JB):	18460.080
Skew:	1.163	Prob(JB):	0.00
Kurtosis:	7.007	Cond. No.	5.10e+05

## Contributing
No.
