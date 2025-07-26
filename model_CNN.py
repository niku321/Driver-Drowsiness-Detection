
import os
from PIL import Image
from numpy import *

# input image dimensions
img_rows, img_cols = 64, 64

# number of channels
img_channels = 3

#%%
#  data

path1 = 'D:/sarasvati biradar/SarasvatiBitmap 24-25/24c9307-Driver Drowsiness Detection/100%code/dataset_new/train/yawn'    #path of folder of images    
path2 = 'D:/sarasvati biradar/SarasvatiBitmap 24-25/24c9307-Driver Drowsiness Detection/100%code/training set/3'  #path of folder to save images    

listing = os.listdir(path1)
num_samples=size(listing)
print(num_samples)

for file in listing:
    im = Image.open(path1 + '\\' + file)  
    img = im.resize((img_rows,img_cols))
    gray = img.convert(mode='RGB')
                #need to do some more processing here          
    gray.save(path2 +'\\' +  file, "png")

imlist = os.listdir(path2)

im1 = array(Image.open('' + imlist[0])) # open one image to get size
m,n = im1.shape[0:2] # get the size of the images
imnbr = len(imlist) # get the number of images

