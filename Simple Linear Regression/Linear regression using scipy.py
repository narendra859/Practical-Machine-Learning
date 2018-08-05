#%% importing the packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# importing the datasets

dataset=pd.read_csv('Data.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values


#Taking care of missing values
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values="NaN",strategy="mean",axis=0,)
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3]) 


#dealing with categorical variables i.e we need to encode the categorical variables
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()

labelencoder_Y=LabelEncoder()
Y=labelencoder_Y.fit_transform(Y)


#dividing Training and Testing set
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)


#feature scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.fit_transform(X_test)

#%% Simple linear regression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sa_data=pd.read_csv('Salary_Data.csv')

X=sa_data.iloc[:,:-1].values
Y=sa_data.iloc[:,1].values

from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=1/3,random_state=0)

#fitting simple linear regression to the training data
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)

Y_pred=regressor.predict(X_test)

plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.xlabel('Experience')
plt.ylabel('salary')
plt.show()
Ypred2=regressor.predict(np.array([[5]]))























