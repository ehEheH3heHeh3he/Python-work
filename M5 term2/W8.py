import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
from keras import Model, Input, layers, losses, optimizers, datasets

# 1. Load data
mnist = pd.read_csv("NeuralNetworktest/dataset.csv")

(X, Y) = mnist.iloc[:, 1:-2].values, mnist.iloc[:, -1].values
xtrain, ytrain,xtest, ytest = X[:600], Y[:600], X[600:], Y[600:]

