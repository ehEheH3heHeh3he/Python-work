# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
# %matplotlib inline
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import confusion_matrix
import seaborn as sns

np.random.seed(0)

mnist_raw = loadmat("mnist-original.mat")
mnist = {
    "data" : mnist_raw["data"].T,
    "target" : mnist_raw["label"][0]
}

x, y = mnist["data"], mnist["target"]

x_train, x_test, y_train, y_test = x[:60000], x[60000:], y[:60000], y[60000:]

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

num_classes = 10
# f, ax = plt.subplots(1, num_classes, figsize=(20,20))

# for i in range(0, num_classes):
#   sample = x_train[y_train == i][0]
#   ax[i].imshow(sample, cmap='gray')
#   ax[i].set_title("Label: {}".format(i), fontsize=16)

for i in range(10):
  print(y_train[i])

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

for i in range(10):
  print(y_train[i])

"""# Prepare Data"""

# Normalize Data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape Data
x_train = x_train.reshape(x_train.shape[0], -1)
x_test = x_test.reshape(x_test.shape[0], -1)
print(x_train.shape)

"""# Create Model - Fully Connected Neural Network"""

model = Sequential()

model.add(Dense(units=128, input_shape=(784,), activation='relu'))
model.add(Dense(units=128, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(units=10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

"""# Train"""

batch_size = 512
epochs=5
model.fit(x=x_train, y=y_train, batch_size=batch_size, epochs=epochs)

"""# Evaluate"""

test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test Loss: {}, Test Accuracy: {}".format(test_loss, test_acc))

y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)
# print(y_pred)
# print(y_pred_classes)

# Single Example
import tkinter as tk
from tkinter import messagebox
def validate_input():
    number = slider_var.get()
    # messagebox.showinfo("Success", f"Valid input: {number}")
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Number Input GUI")
root.geometry("350x150+550+350")

# Create a slider and a variable to store its value
slider_var = tk.IntVar()
slider = tk.Scale(root, from_=1, to=10000, variable=slider_var, orient=tk.HORIZONTAL, label="Select a number:")
slider.pack(pady=20)

# Create a button to validate the input
validate_button = tk.Button(root, text="Validate Input", command=validate_input)
validate_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
print(slider_var.get())

idx = int(slider_var.get())
x_sample = x_test[idx]
y_true = np.argmax(y_test, axis=1)
y_sample_true = y_true[idx]
y_sample_pred_class = y_pred_classes[idx]

plt.title("Predicted: {}, True: {}".format(y_sample_pred_class, y_sample_true), fontsize=16)
plt.imshow(x_sample.reshape(28, 28), cmap='gray')


"""# Confusion Matrix"""

confusion_mtx = confusion_matrix(y_true, y_pred_classes)

# Plot
fig, ax = plt.subplots(figsize=(15,10))
ax = sns.heatmap(confusion_mtx, annot=True, fmt='d', ax=ax, cmap="Blues")
ax.set_xlabel('Predicted Label')
ax.set_ylabel('True Label')
ax.set_title('Confusion Matrix')

plt.show()