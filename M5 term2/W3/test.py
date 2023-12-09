from scipy.io import loadmat

mnist_raw = loadmat("mnist-original.mat")

print(mnist_raw["data"])