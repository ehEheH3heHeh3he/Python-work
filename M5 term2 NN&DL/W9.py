import pandas as pd
import io
import requests
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.callbacks import EarlyStopping
from keras.datasets import mnist
from keras.utils import to_categorical


(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# df = pd.read_csv(
#     "https://data.heatonresearch.com/data/t81-558/iris.csv",
#     na_values=['NA', '?'])

# # Convert to numpy - Classification
# x = df[['sepal_l', 'sepal_w', 'petal_l', 'petal_w']].values
# dummies = pd.get_dummies(df['species']) # Classification
# species = dummies.columns
# y = dummies.values

# # Split into validation and training sets
# x_train, x_test, y_train, y_test = train_test_split(
#     x, y, test_size=0.25, random_state=42)

# Build neural network
model = Sequential()
model.add(Dense(100, input_dim= 784,  activation='relu', kernel_regularizer = 'l2')) # Hidden 1
model.add(Dropout(0.2)) ###using dropout
model.add(Dense(100, activation='relu', kernel_regularizer = 'l2')) # Hidden 2
model.add(Dropout(0.2)) ###using dropout
model.add(Dense(100, activation='relu', kernel_regularizer = 'l2')) # Hidden 3
model.add(Dropout(0.2)) ###using dropout
model.add(Dense(100, activation='relu', kernel_regularizer = 'l2')) # Hidden 4
model.add(Dropout(0.2)) ###using dropout
model.add(Dense(10,  activation='softmax', kernel_regularizer = 'l2')) # Output


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

monitor = EarlyStopping(monitor='val_loss', min_delta=1e-3, patience=5,
       verbose=1, mode='auto', restore_best_weights=True)
model.fit(X_train,y_train,validation_data=(X_test,y_test),
        callbacks=[monitor],verbose=2,epochs=1000)
