from keras.datasets import cifar10
(in_train, out_train), (in_test, out_test) = cifar10.load_data()

import matplotlib.pyplot as plt
plt.imshow(in_train[0])

in_train.max()
# Output
# 255
in_train = in_train/255
in_test = in_test/255