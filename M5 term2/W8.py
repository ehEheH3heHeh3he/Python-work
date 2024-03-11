import tensorflow as tf
import numpy as np
from keras import Model, Input, layers, losses, optimizers, datasets
from matplotlib import pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd

df = pd.read_csv("dataset.csv")
df.replace('nan', np.nan, inplace=True)
df = df.dropna(axis=0)

data = np.array(df)
m, n = data.shape

itrain = []
itest = []
X = df.iloc[:, 1:784].values
L = df.iloc[:, 785].values
classes = np.unique(L)
split = 0.7
Y = []

for c in classes:
  Idx = L == c
  idx = np.where(Idx)[0]
  sp = int(split * len(idx))
  itrain.extend(idx[:sp])
  itest.extend(idx[sp:])

Y = np.array(Y).T

# clf = SVC()
# clf.fit(X[itrain],L[itrain])
# Z = clf.predict(X[itest])
# print('accuracy rate=', accuracy_score(L[itest], Z))
# print('confusion matrix:')
# print(confusion_matrix(L[itest], Z))

inputs = Input(shape=X.shape[1])

en1 = layers.Dense(X.shape[1] // 2, activation='relu')
en2 = layers.Dense(X.shape[1] // 4, activation='relu')
en3 = layers.Dense(X.shape[1] // 8, activation='relu')

de1 = layers.Dense(X.shape[1] // 4, activation='relu')
de2 = layers.Dense(X.shape[1] // 2, activation='relu')
de3 = layers.Dense(X.shape[1], activation='relu')

outputs = de3(de2(de1(en3(en2(en1(inputs))))))

model = Model(inputs, outputs)

model.compile(loss=losses.MeanSquaredError(),
              optimizer=optimizers.Adam())

np.where(np.isnan(X))
model.fit(X, X, epochs=200)

Xencoded = en3(en2(en1(X[itrain]))).numpy()
print(Xencoded.shape)
print(Xencoded)

clf1 = SVC()
clf1.fit(Xencoded, L[itrain])
Xtestencoded = en3(en2(en1(X[itest]))).numpy()
Z1 = clf1.predict(Xtestencoded)
print('accuracy rate=', accuracy_score(L[itest], Z1))
print('confusion matrix:')
print(confusion_matrix(L[itest], Z1))