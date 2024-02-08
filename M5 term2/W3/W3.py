
import numpy as np

class NeuralNetwork:
    def __init__(self):
        self.W1 = np.random.randn(10, 784) - 0.5
        self.b1 = np.random.randn(10, 1) - 0.5
        self.W2 = np.random.randn(10, 10) - 0.5
        self.b2 = np.random.randn(10, 1) - 0.5

    def forward_prop(self, x):
        z1 = np.dot(self.W1, x) + self.b1
        a1 = self.sigmoid(self.z1)
        z2 = np.dot(self.W2, self.a1) + self.b2
        a2 = self.sigmoid(self.z2)
        return z1, a1, z2, a2
    
    def relu(self, z):
        return np.maximum(0, z)
    
    def dervi_relu(self, z):
        return z > 0
    
    def softmax(self, z):
        z = z - np.max(z, axis=0)
        return np.exp(z) / np.sum(np.exp(z), axis=0)
    
    