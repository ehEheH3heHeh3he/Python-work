import numpy as np
import pandas as pd
from scipy.io import loadmat
from NeuralNetwork import My_nn

# mnist_raw = loadmat("mnist-original.mat")
# mnist = {
#     "data" : mnist_raw["data"].T,
#     "target" : mnist_raw["label"][0]
# }

data = pd.read_csv('train.csv')
data = np.array(data)
print (data)


# changing the shape of mnist the data
# new_data = mnist.get("data")
# print(new_data)

# for i in range(1,70000):
#     new_data = np.insert(new_data, 0, mnist_raw["label"][0][i])
# print(new_data)

m, n = data.shape

data = data.T
Y_train = data[0]
X_train = data[1:n]
X_train = X_train / 255.

nn = My_nn()
nn.fit(X_train, Y_train, 0.1, 1000)

for i in range(20):
    index = np.random.randint(1, m)
    nn.test_train(index , X_train, Y_train)