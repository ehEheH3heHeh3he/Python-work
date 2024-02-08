import tensorflow as tf
import numpy as np
import pandas as pd

N = 100
X = np.random.rand(N, 1)
Y = np.sin(2 * np.pi * X) + 0.4 * np.random.rand(N, 1)

def relu(x):
  return tf.where(x>=0, x, 0)

class MLP():
  def __init__(self, neurons=[1, 100, 100, 1], activation=[relu, relu, None]):
    self.W = []
    self.activation = activation
    for i in range(1, len(neurons)):
      self.W.append(tf.Variable(np.random.randn(neurons[i-1], neurons[i]))) # W
      self.W.append(tf.Variable(np.random.randn(neurons[i]))) # b
  def __call__(self, x):
    for i in range(0, len(self.W), 2):
      x = x @ self.W[i] + self.W[i+1]
      if self.activation[i // 2] is not None:
        x = self.activation[i // 2](x)
    return x
  def fit(self, X, Y, lr=0.0001, epochs=2000):
    for epoch in range(epochs):
      with tf.GradientTape() as t:
        loss = tf.reduce_mean((self(X) - Y)**2)
      dW = t.gradient(loss, self.W)
      for i, W in enumerate(self.W):
        W.assign_sub(lr * dW[i])
      if epoch % 1000 == 0:
        print(f"epoch = {epoch}, loss = {loss.numpy()}")
        

df = pd.read_csv('NeuralNetworktest/dataset.csv')


itrain = []
itest = []
X = df.iloc[:, :783].values
L = df.iloc[:, -1].values
classes = np.unique(L) # store all the labels
print(classes)
split = 0.7
Y = []


for c in classes:
  Idx = L == c
  idx = np.where(Idx)[0]
  sp = int(split * len(idx))
  itrain.extend(idx[:sp])
  itest.extend(idx[sp:])
  Y.append(Idx.astype(np.int32)) # one-hot
Y = np.array(Y).T

model = MLP([783, 100, 100, 10], [tf.sigmoid, tf.sigmoid, tf.nn.softmax])
model.fit(X[itrain], Y[itrain], lr=0.1, epochs=6000)

Z = model(X[itest])
tf.argmax(Z, axis=1)

tf.argmax(Y[itest], axis=1)
np.sum(tf.argmax(Y[itest], axis=1) == tf.argmax(Z, axis=1)) / len(itest)