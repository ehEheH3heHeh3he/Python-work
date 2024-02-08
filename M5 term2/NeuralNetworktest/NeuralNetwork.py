import matplotlib.pyplot as plt
import numpy as np


def relu(z):
	return np.maximum(0, z)

def sigmoid(x):
 	return 1/(1 + np.exp(-x))

def tanh(x):
  	return (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))

def deriv_relu(z):
	return z > 0

def deriv_sigmoid(x):
    return x * (1 - x)

def der_tanh(x):
  	return 1 - tanh(x) * tanh(x)


def softmax(z): # stabel softmax
	z = z - np.max(z, axis=0)
	return np.exp(z) / np.sum(np.exp(z), axis=0)

def one_hot(Y):
	m = len(Y)
	one_hot = np.zeros((10, m))
	for i in range(m):
		one_hot[Y[i]][i] = 1
	return one_hot

def get_predict(A3):
	return np.argmax(A3, axis=0)

def get_accuracy(predict, Y):
	return np.sum(get_predict(predict) == Y) / len(Y)

class My_nn:
	def __init__(self):
		self.W1 = np.random.rand(50, 785) - 0.5
		self.b1 = np.random.rand(50, 1) - 0.5
		self.W2 = np.random.rand(50, 50) - 0.5
		self.b2 = np.random.rand(50, 1) - 0.5
		self.W3 = np.random.rand(10, 50) - 0.5
		self.b3 = np.random.rand(10, 1) - 0.5
	

	def forward_prop(self, X):
		Z1 = np.dot(self.W1, X) + self.b1
		A1 = relu(Z1)
		Z2 = np.dot(self.W2, A1) + self.b2
		A2 = relu(Z2)
		Z3 = np.dot(self.W3, A2) + self.b3
		A3 = softmax(Z3)
		return Z1, A1, Z2, A2, Z3, A3

	def back_prop(self, Z1, A1, Z2, A2, Z3, A3, X, Y, alpha):
		m = len(Y)
		dZ3 = A3 - one_hot(Y)
		dW3 = 1/m * np.dot(dZ3, A2.T)
		db3 = 1/m * np.sum(dZ3)
		dZ2 = np.dot(self.W3.T, dZ3) * deriv_relu(Z2)
		dW2 = 1/m * np.dot(dZ2, A1.T)
		db2 = 1/m * np.sum(dZ2)
		dZ1 = np.dot(self.W2.T, dZ2) * deriv_relu(Z1)
		dW1 = 1/m * np.dot(dZ1, X.T)
		db1 = 1/m * np.sum(dZ1)

		self.W3 = self.W3 - alpha * dW3
		self.b3 = self.b3 - alpha * db3
		self.W2 = self.W2 - alpha * dW2
		self.b2 = self.b2 - alpha * db2
		self.W1 = self.W1 - alpha * dW1
		self.b1 = self.b1 - alpha * db1

	def fit(self, X, Y, alpha, n_iters):
		for i in range(1, n_iters+1):
			Z1, A1, Z2, A2, Z3, A3 = self.forward_prop(X)
			self.back_prop(Z1, A1, Z2, A2, Z3, A3, X, Y, alpha)
			accuracy = get_accuracy(A3, Y)
			if i%100==0 or i==n_iters:
				print(f'Iteration: {i} Accuracy: {accuracy}')

	def test_train(self, index, X, Y):
		test = X[:, index, None] 
		Z1, A1, Z2, A2, Z3, A3 = self.forward_prop(X)
		predict = get_predict(A3) 
		label = Y[index]
		image = test.reshape((28, 28))

		plt.imshow(image, interpolation='nearest', cmap='gray')
		plt.title(f'Predict: {predict[index]} Label: {label}')
		plt.show()
