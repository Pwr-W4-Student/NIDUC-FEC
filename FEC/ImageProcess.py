from PIL import Image
import numpy as np
from scipy.misc import imread
from scipy.misc import imsave

from matplotlib import pyplot as plt

#########################
# uzyc numpy.flatten
def load_image( infilename ) :

    img = imread(infilename)
    #imsave("sf.jpg", img)
    #print(type(img))
    #print(img)

    output = np.unpackbits(img)
    #print(output)

    return np.asarray(output)


"""
    #img = Image.open( infilename )
    #img.load()


=======


def load_image( infilename ) :
    #img = Image.open( infilename )
    #img.load()

>>>>>>> piotr
=======


def load_image(infilename):
    #img = Image.open( infilename )
    #img.load()

>>>>>>> jakub
    img = imread(infilename)
    #print(img2)
    data = np.asanyarray( img, dtype="uint8" )
    #print(data)
    output = data.reshape(-1) #np.reshape(data, (np.product(data.shape), ))
    #print(output)
    tmp = []
    out = []
    for c in output:
        tmp.append(np.binary_repr(c, 8))

    for c in tmp:
        for k in c:
            out.append(k)
    return np.asarray(out, dtype=int)
<<<<<<< HEAD
<<<<<<< HEAD
    """

def save_image( data, outfilename ) :

   # plt.imshow(data, cmap='gray', interpolation='nearest')

    data = np.asarray(data, dtype=str)

    data = data.reshape((1920000, 8))
    #print(data[0])
    output = []
    for d in data:
        output.append(int("".join(d), 2))

    #print(output)

    output = np.asarray(output, dtype=np.uint8)
    #print(output)

    arr3d = output.reshape((800,800,3))
    #print(type(arr3d))
    #print(arr3d)
    imsave(outfilename, arr3d)



    """
=======

def save_image( data, outfilename ) :
>>>>>>> piotr
=======

def save_image(data, outfilename):
>>>>>>> jakub
    data = np.asarray(data, dtype=str)
    tmp = ""
    out = []

    for i, bit in enumerate(data):
        tmp += bit
        if (i+1)%8 == 0 and i != 0:
            out.append(tmp)
            tmp = ""

    tmp = []
    for c in out:
        tmp.append(int(c, 2))
    tmp2 = np.asarray(tmp)
    #print(tmp2)
    npdata = tmp2.reshape((100,100,3))
    #print(npdata)

<<<<<<< HEAD
    imsave(outfilename, npdata)
<<<<<<< HEAD
    """
