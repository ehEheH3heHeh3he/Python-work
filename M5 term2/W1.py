from sklearn import datasets
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

mnist_raw = loadmat("M5 term2/mnist-original.mat")
minst = {
    "data" : mnist_raw["data"].T,
    "target" : mnist_raw["label"][0]
}
x, y = minst["data"], minst["target"]

number = [7000, 15000, 20000, 27000, 35000, 40000, 43000, 50000, 58000]

# loop num = number[i]
for i in range(len(number)):
    num_image = x[number[i]]
    num_label = y[number[i]]
    num_image = num_image.reshape(28,28)
    # subplot 
    plt.subplot(3,3,i+1)
    plt.title("Label = " + str(num_label), fontsize = 10)
    plt.imshow(
        num_image,
        cmap = plt.cm.binary,
        interpolation = "nearest"
    )

plt.show()
