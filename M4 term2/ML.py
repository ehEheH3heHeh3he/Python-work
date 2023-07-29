from scipy.io import loadmat
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# iris_dataset=load_iris()

# x_train,x_test,y_train,y_test=train_test_split(
#     iris_dataset['data'],
#     iris_dataset['target'],
#     test_size=0.2,
#     random_state=0
# )

# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)


mnist_raw = loadmat('mnist-original.mat')
mnist={
    'data':mnist_raw['data'].T,
    'target':mnist_raw['label'][0]
}
x,y = mnist['data'],mnist['target']
number=x[0]
number_image=number.reshape(28,28)
print(y[0])
plt.imshow(number_image,cmap=plt.cm.binary)
plt.show()



# digits_dataset = datasets.load_digits()

# iris_dataset = datasets.load_iris()
# print(digits_dataset.target[0])
# plt.imshow(digits_dataset.images[9],cmap=plt.get_cmap('gray_r'))
# plt.show()
