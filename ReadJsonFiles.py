import json
import os
import base64
from labelme import utils
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from os import listdir
from os.path import isfile, join
mypath = 'C:\\Users\\jross\\OneDrive\\Data Analytics\\Machine Learning\\Project\\Project Data\\Labeled France Potholes\\'
onlyfiles = [mypath + f for f in listdir(mypath) if isfile(join(mypath, f))]

print(len(onlyfiles))

with open('C:\\Users\jross\OneDrive\Desktop\\yo.txt') as json_file:
    data = json.load(json_file)

with open(onlyfiles[1]) as json_file:
    data = json.load(json_file)

mypath = 'C:\\Users\\jross\\OneDrive\\Data Analytics\\Machine Learning\\Project\\Project Data\\Labeled France Potholes\\'
onlyfiles = [mypath + f for f in listdir(mypath) if isfile(join(mypath, f))]


imageData = data['imageData']

img = utils.img_b64_to_arr(imageData)

x_training = []
y_training = []

print(data['shapes'][0]['label'])

for file in onlyfiles:
    with open(file) as json_file:
        data = json.load(json_file)
        x_training.append(utils.img_b64_to_arr(data['imageData']))
        y_training.append(data['shapes'][0]['label'])

print(x_training[0])
print(y_training[0])

print(x_training[0].shape)

#convert to gray-scale
from skimage import color
from skimage import io

print(x_training[0][:,:,0])
x_training_gray = []

for x in x_training:
    x_training_gray.append(color.rgb2gray(x))
#print(x_training_gray.shape[0])
print(x_training_gray[0])
#print(x_training_gray)
io.imshow(x_training_gray[0])
io.show()
