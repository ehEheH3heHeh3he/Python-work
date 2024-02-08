import matplotlib.pyplot as plt 
import numpy as np
from sklearn.linear_model import LinearRegression
rng = np.random

x = rng.rand (50)*10
y = 2*x+rng.randn(50)

model = LinearRegression()
# print(type(x))

x_new = x.reshape(-1,1)
# reshaped to 2d array

model.fit(x_new,y)
print(model.score(x_new,y))
# ยิ่งใกล้1ยิ่งดี
print(model.intercept_)
# จุดตัดแกน
print(model.coef_)
# 

#test model
xfit = np.linspace(-1,11)
xfit_new = xfit.reshape(-1,1)
# reshaped to 2d array

yfit = model.predict(xfit_new)

plt.scatter(x,y)
plt.plot(xfit,yfit)
plt.show()