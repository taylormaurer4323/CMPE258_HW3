# -*- coding: utf-8 -*-
"""assignment3_Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BLIOaPUmxHqvGyZukuUAxa70-5j77lsj
"""

import tensorflow as tf
from tensorflow.keras import layers
from sklearn.datasets import make_regression
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import cv2
from google.colab.patches import cv2_imshow

#Get sample data
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

#Get subset of images and resize them based on assifnment
#Just get 100 images to train on:
tmp_np_imgs = np.zeros([100, 127,127,3])
for i in range(0, 100):
  newimg = cv2.resize(train_images[i], dim, interpolation = cv2.INTER_AREA)
  tmp_np_imgs[i] = newimg
tf_train_img = tf.constant(tmp_np_imgs)
tf_train_labels = train_labels[0:100]
#Get 10 images to test on
tmp_np_imgs = np.zeros([10, 127,127,3])
for i in range(0,10):
  newimg = cv2.resize(test_images[i], dim, interpolation = cv2.INTER_AREA)
  tmp_np_imgs[i] = newimg
tf_test_img = tf.constant(tmp_np_imgs)
tf_test_labels = test_labels[0:10]

#Create the CNN/YOLO like design:
model =tf.keras.models.Sequential()
model.add(layers.Conv2D(64, (7, 7), activation='relu', input_shape=(127, 127, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (2, 2), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(256, (2, 2), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
#This layer is final layer, see the model.summary output for this layer
#it will show output of 50x8x8, which is consistent with an 8x8 grid with 2x 
#anchors per each cell resulting in length 50 of vector per each cell.
model.add(layers.Conv2D(50, (7, 7), activation='relu')) 
model.add(layers.Flatten())
#Expected input into Fullt connected NN is 50*8*8 = 3200
model.add(layers.Dense(3200, activation='relu')) 
#20 classes, so 20 output with softmax activiation
model.add(layers.Dense(20, activation='softmax'))
model.summary()

#Compile, use adam as should be fastest
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

#Don't need a lot of epochs as there's a lot of parameters to train
history = model.fit(tf_train_img, tf_train_labels, epochs=10, 
                    validation_data=(tf_test_img, tf_test_labels))

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(tf_test_img,  tf_test_labels, verbose=2)
print(test_acc)

