import numpy as np
import pandas as pd

from NeuralNetwork import My_nn

data = pd.read_csv('dataset.csv')
data = np.array(data)

m, n = data.shape

data = data.T
Y_train = data[-1]
X_train = data[1:n]
X_train = X_train / 255

nn = My_nn()
nn.fit(X_train, Y_train, 0.1, 1000)

for i in range(50):
    index = np.random.randint(1, m)
    nn.test_train(index , X_train, Y_train)
