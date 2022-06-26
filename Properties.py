from matplotlib import image
from matplotlib import pyplot
from PIL import Image
import os 
import os.path 
os.system("clear")
filename=input(" \n \t * Enter the path of the image : ")
print("\n\n")
im = Image.open(filename)
print(im.format)
print(im.mode)
print(im.size)
data = image.imread(filename)
print(data.dtype)
print(data.shape)
pyplot.imshow(data)
pyplot.show()

