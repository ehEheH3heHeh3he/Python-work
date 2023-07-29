from scipy.io import loadmat
import numpy as np
import  matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score
import itertools

mnist_raw = loadmat("mnist-original.mat")
mnist = {
    "data" : mnist_raw["data"].T,
    "target" : mnist_raw["label"][0]
}

x, y = mnist["data"], mnist["target"]

x_train, x_test, y_train, y_test = x[:60000], x[60000:], y[:60000], y[60000:]

predict_number = 4500
y_train_7 = (y_train == 4)
y_test_7 = (y_test == 4)

def displayImage(x):
    plt.imshow(
        x.reshape(28,28),
        cmap = plt.cm.binary,
        interpolation = "nearest"
    )
    plt.show()

def desplayPredict(clf, actually_y, x):
    print("Actually = ", actually_y)
    print("Prediction = ", clf.predict([x])[0])

sgd_clf = SGDClassifier()
sgd_clf.fit(x_train, y_train_7)

desplayPredict(sgd_clf, y_test_7[predict_number], x_test[predict_number])

print(cross_val_score(sgd_clf, x_train, y_train_7, cv = 3, scoring = 'accuracy'))

y_train_pred = cross_val_predict(sgd_clf, x_train, y_train_7, cv = 3)

print(confusion_matrix(y_train_7, y_train_pred))

y_test_pred = sgd_clf.predict(x_test)

print("Accuracy Score = ", accuracy_score(y_test_7, y_test_pred)*100)

displayImage(x_test[predict_number])