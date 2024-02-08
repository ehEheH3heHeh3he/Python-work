import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('Final\Weather.csv')

# data linear
x = dataset["MinTemp"].values.reshape(-1,1)
y = dataset["MaxTemp"].values.reshape(-1,1)

# split data train80% test20%
# test เอาไว้ตรวจ
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

# train
model = LinearRegression()
model.fit(x_train,y_train)

#test
y_pred = model.predict(x_test)
df = pd.DataFrame({'Actually':y_test.flatten(),'Predicted':y_pred.flatten()})
print(df)

# graph
df1 = df.head(20)
df1.plot(kind='bar')
plt.show()

print('MAE= ',metrics.mean_absolute_error(y_test,y_pred))
print('MSE= ',metrics.mean_squared_error(y_test,y_pred))
print('RMAE= ',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))
print('Score= ',metrics.r2_score(y_test,y_pred))
