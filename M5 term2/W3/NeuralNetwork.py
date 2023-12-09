import matplotlib.pyplot as plt
import numpy as np


def relu(z):
	return np.maximum(0, z)

def deriv_relu(z):
	return z > 0

def softmax(z): # stabel softmax
	z = z - np.max(z, axis=0)
	return np.exp(z) / np.sum(np.exp(z), axis=0)

def one_hot(Y):
	m = len(Y)
	one_hot = np.zeros((10, m))
	for i in range(m):
		one_hot[Y[i]][i] = 1
	return one_hot

def get_predict(A2):
	return np.argmax(A2, axis=0)

def get_accuracy(predict, Y):
	return np.sum(get_predict(predict) == Y) / len(Y)

class My_nn:
	def __init__(self):
		self.W1 = np.random.rand(10, 784) - 0.5
		self.b1 = np.random.rand(10, 1) - 0.5
		self.W2 = np.random.rand(10, 10) - 0.5
		self.b2 = np.random.rand(10, 1) - 0.5
	
	def forward_prop(self, X):
		Z1 = np.dot(self.W1, X) + self.b1
		A1 = relu(Z1)
		Z2 = np.dot(self.W2, A1) + self.b2
		A2 = softmax(Z2)	
		return Z1, A1, Z2, A2
	
	def back_prop(self, Z1, A1, Z2, A2, X, Y, alpha):
		m = len(Y)
		dZ2 = A2 - one_hot(Y)
		dW2 = 1/m * np.dot(dZ2, A1.T)
		db2 = 1/m * np.sum(dZ2)
		dZ1 = np.dot(self.W2.T, dZ2) * deriv_relu(Z1)
		dW1 = 1/m * np.dot(dZ1, X.T)
		db1 = 1/m * np.sum(dZ1)

		self.W2 = self.W2 - alpha * dW2
		self.b2 = self.b2 - alpha * db2
		self.W1 = self.W1 - alpha * dW1
		self.b1 = self.b1 - alpha * db1

	def fit(self, X, Y, alpha, n_iters):
		for i in range(1, n_iters+1):
			Z1, A1, Z2, A2 = self.forward_prop(X)
			self.back_prop(Z1, A1, Z2, A2, X, Y, alpha)
			accuracy = get_accuracy(A2, Y)
			if i%100==0 or i==n_iters:
				print(f'Iteration: {i} Accuracy: {accuracy}')

	def test_train(self, index, X, Y):
		test = X[:, index, None] 
		Z1, A1, Z2, A2 = self.forward_prop(X)
		predict = get_predict(A2) 
		label = Y[index]
		image = test.reshape((28, 28))

		plt.imshow(image, interpolation='nearest', cmap='gray')
		plt.title(f'Predict: {predict[index]} Label: {label}')
		plt.show()
