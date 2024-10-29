import tensorflow as tf
import numpy as np
import pandas as pd

def relu(x):
    return tf.where(x>=0, x, 0)

class MLP():
    def __init__(self, neurons=[1, 100, 100, 1], activation=[relu, relu, None]):
        self.W = []
        self.activation = activation
        for i in range(len(neurons)-1):
            self.W.append(tf.Variable(np.random.randn([neurons[i-1], neurons[i]]))) #W
            self.W.append(tf.Variable(np.random.randn(neurons[i]))) #b
        
    def __call__(self, x):
        for i in range(0, len(self.W), 2):
            x = tf.matmul(x, self.W[i]) + self.W[i+1]
            if self.activation[i//2] is not None:
                x = self.activation[i//2](x)
        return x
    
    def fit(self, X, Y, epochs=100, lr=0.01):
        for epochs in range(epochs):
            with tf.GradientTape() as t:
                loss = tf.reduce_mean((self(X)-Y)**2)
            dW = t.gradient(loss, self.W)
            for i, W in enumerate(self.W):
                W.assign_sub(lr*dW[i])
            if epochs % 1000 == 0:
                print('epochs: %d, loss: %f' % (epochs, loss))
        
df = pd.read_csv('iris.data', header=None)
itrain = []
itest = []
X = df.iloc[:, :4].values
L = df.iloc[:, -1].values
classes = np.unique(L)
split = 0.8
Y = []
for c in classes:
    Idx = L == c
    idx = np.where(Idx)[0]
    sp = int(split*len(idx))
    itrain.append(idx[:sp])
    itest.append(idx[sp:])
    Y.append(Idx.astype(np.int32)) # one-hot encoding
Y = np.array(Y).T

model = MLP([4, 100, 100, 3], [tf.sigmoid, tf.sigmoid, tf.nn.softmax])
model.fit(X[itrain], Y[itrain], epochs=10000, lr=0.01)

Z = model(X[itest])
tf.argmax(Z, axis=1)

tf.argmax(Y[itest], axis=1)
np.sum(tf.argmax(Y[itest], axis=1) == tf.argmax(Z, axis=1))/len(itest)