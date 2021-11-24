# CMPE258_HW3
## assignment3_q1.py - this answers the first question. 
This creates a fully connected neural network, trains it, and then evaluates it. 
The data is randomly created using the sklearn library and is split within
tf data structures.

## assignment_q2.py - this answers the second question.
This creates a convolutional network attempting to somewhat mimic the YOLO network. However, YOLO has a lot of parameters so I could only do so much in terms of layers used so I could make sure it was trainable. The dataset is a keras dataset that only uses 10 classes (not 20) so results are not expected to be that great. Additionally, the images from the keras dataset used were 32 x 32 and had to be stretched to 127x127 to fit the assignment. This results in a lot of information loss AKA pixelated images.
