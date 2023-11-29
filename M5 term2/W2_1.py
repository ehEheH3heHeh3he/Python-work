from sklearn import datasets
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

mnist_raw = loadmat("M5 term2/mnist-original.mat")
mnist = {
    "data" : mnist_raw["data"].T,
    "target" : mnist_raw["label"][0]
}
x, y = mnist["data"], mnist["target"]

x_train, x_test, y_train, y_test = x[:60000], x[60000:], y[:60000], y[60000:]

model = MLPClassifier(hidden_layer_sizes=(3000,), max_iter=1000, alpha=0.0001,learning_rate_init=0.0001)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred)*100)


# plot first 100 image
# for i in range(100):
#     num_image = x[i]
#     num_label = y[i]
#     num_image = num_image.reshape(28,28)
#     # subplot
#     plt.subplot(10,10,i+1)
#     plt.title("Label = " + str(int(num_label)), fontsize = 10)
#     plt.imshow(
#         num_image,
#         cmap = plt.get_cmap("gray"),
#         interpolation = "nearest"
#     )

# plot random 100 image from test sets
rndperm = np.random.permutation(10000)
num_image = x_test[rndperm]
num_label = y_test[rndperm]

for i in range(100):
    eiei = num_image[i].reshape(28,28)
    # subplot
    plt.subplot(10,10,i+1, xticks=[], yticks=[])
    plt.title("La=" + str(int(num_label[i])), fontsize = 10)
    plt.title("Tr=" + str(int(y_pred[i])), fontsize = 10)

    plt.imshow(
        eiei,
        cmap = plt.get_cmap("gray"),
        interpolation = "nearest"
    )


plt.show()
