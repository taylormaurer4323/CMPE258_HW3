# -*- coding: utf-8 -*-
"""assignment3_Q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Phi_wmqWCxUwhE5j5G-pTPsZ9H_yF7Vm
"""

import tensorflow as tf
from tensorflow.keras import layers
from sklearn.datasets import make_regression
from matplotlib import pyplot as plt
import numpy as np

#create regression dataset to use as housing set
#y_data = housing price data
#x_data = associated features
x_data, y_data = make_regression(n_samples=1000, n_features=25, n_informative = 20, n_targets = 1, noise=10000, bias = 50000)

tf_y_data = tf.constant(y_data)
tf_x_data = tf.constant(x_data)

#Create split:
train_size = int(.9 * tf_x_data.shape[0])
test_size = tf_x_data.shape[0] - train_size
incr = np.arange(1,train_size+1, 1)
tf_x_train = tf_x_data[0:train_size, :]
tf_y_train = tf_y_data[0:train_size]
tf_x_test = tf_x_data[train_size:-1, :]
tf_y_test = tf_y_data[train_size:-1]
#tf_x_test = tf_x_data.skip(train_size)
#tf_y_test = tf_y_data.skip(train_size)

#View distribution of y data
plt.scatter(incr, tf_y_train)
plt.show()

#Create Fully Connected Neural network:

auto_model = tf.keras.Sequential([
    layers.Input(shape=(25,)),
    layers.Dense(256, activation = tf.nn.relu),
    layers.Dense(256, activation = tf.nn.relu),
    layers.Dropout(0.5),
    layers.Dense(1) #<- output layer
])

auto_model.compile(loss = 'mean_absolute_error', optimizer = tf.keras.optimizers.Adam(0.01))

auto_model.summary()

history = auto_model.fit(
    tf_x_train,
    tf_y_train,
    validation_split=0.2,
    verbose=0, epochs=1000)

plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')

  plt.xlabel('Epoch')
  plt.ylabel('Error')
  plt.legend()
  plt.grid(True)

tresults = auto_model.evaluate(tf_x_test, tf_y_test, verbose=0)
print('Mean Squared Error: ', tresults)



