from matplotlib import pyplot
from numpy import array
import numpy

import sys
sys.setrecursionlimit(100000)
from count import count


from BSC import BSC
from TMR import TMR
from TMR import Decode
from Gilbert import Gilbert_Model
from interleaving import interleaving,decode_interleaving,encode_interleaving_Hamming,decode_interleaving_Hamming
from ImageProcess import load_image,save_image
from reedsolo import RSCodec
from HammCode import Ham, DecodeHamm,HamEncode,HamDecode
#from commpy.channelcoding import turbo


from ImageProcess import load_image
from ImageProcess import save_image
from interleaving import encode_interleaving_Hamming




"""
input  = array([1, 0, 0, 1])
longer_input = [1,0,1,1,1,0,0,1,1,0,1,0,1,1,1,0]
bits = [1,0,1,1,1,0,0,1]

output = BSC(input, 0.1)

#Ham(input)
#print("\n")

input  = bytearray([1, 0, 0, 1])
longer_input = array ([1,0,1,1,1,0,0,1,1,0,1,0])


#enc = turbo_encode(input)
#print(enc)
#denc = turbo_decode(enc)
#print(denc)

"""

### ZDJECIE - BSC
image_output = load_image("image.jpg")
#save_image(image_output,"image_out.jpg")

print(image_output)
gil = Gilbert_Model(image_output,0.99,0.0001)
print(gil)
ile = 0
#save_image(gil,"gilb.jpg")
#image_gilb = load_image("gilb.jpg")
#print(image_gilb)
for i in range(len(image_output)):
    if(image_output[i]!=gil[i]):
        ile = ile + 1

#print(count(image_output, gil))
print(ile)


"""
print(count(image_output, BSC(image_output,0.00023)))

tmr_out = TMR(image_output)
bsc = BSC(tmr_out,0.00023)
tmr_dec = Decode(bsc)
print(count(image_output, tmr_dec))
"""
"""
bledy = 15560000
min_p = 0;

for i in numpy.arange(1.0, 0.0, -0.1):

    tmr_out = TMR(image_output)
    bsc = BSC(tmr_out,i)
    tmr_dec = Decode(bsc)
    if count(image_output, tmr_dec) < bledy:
        bledy = count(image_output, tmr_dec)
        min_p = i
        print(bledy)
        print(i)
        print("\n")
    #save_image(bsc,"BSC.jpg")

"""
"""
###Zdjecie BSC i hamming
image_output = load_image("image.jpg")
ham = HamEncode(image_output)
bsc = BSC(ham,0.05)
output = HamDecode(bsc)
#save_image(output, "bsc_hamm.jpg")

###Zdjecie TMR BSC
image_output = load_image("image.jpg")
tmr = TMR(image_output)
bsc = BSC(tmr, 0.1)
picture = Decode(bsc)
#save_image(picture, "tmr i bsc.jpg")

###Zdjecie TMR BSC Przeplot Hamming
image_output = load_image("image.jpg")
coded = encode_interleaving_Hamming(image_output,16,4) ###hamming po przeplocie
tmr = TMR(coded)
bsc = BSC(tmr, 0.1)
out = Decode(bsc)
picture = decode_interleaving_Hamming(out,7,4)
#save_image(picture, "przeplot_hamming_tmr_bsc.jpg")

###Zdjecie BSC i przeplot
image_output = load_image("image.jpg")
inter = interleaving(image_output,4)
bsc = BSC(inter, 0.1)
picture = decode_interleaving(bsc,4)
#save_image(picture, "bsc_interleaving.jpg")

###Zdjecie Gilbert
image_output = load_image("image.jpg")
coded = encode_interleaving_Hamming(image_output,16,4)
gilb = Gilbert_Model(coded,0.1,0.9)
picture = decode_interleaving_Hamming(gilb,7,4)
save_image(picture, "gilb.jpg")


###przeplot
image_output = load_image("image.jpg")
coded = encode_interleaving_Hamming(image_output,16,4)
picture = decode_interleaving_Hamming(coded,7,4)
save_image(picture, "przeplot22.jpg")
"""
###zdjecie Gilbert
#image_input = load_image("image.jpg")
#tmr = TMR(image_input)
#gilb = Gilbert_Model(image_input, 0.9, 0.002)
#picture = Decode(gilb)

#save_image(gilb, "gilb222.jpg")
"""
#rs = RSCodec(10)
#msg = "Hello World"
#print(msg)
#enc = rs.encode(msg)
#print(enc)
#denc = rs.decode(enc)
#print(denc)



#tmr_output = TMR(input)
#bsc_output = BSC(tmr_output, 0.1)
#print("BSC after TMR:")
#print(bsc_output)

#output = Decode(bsc_output)
#print("Decoded BSC:")
#print(output)
#print("\n")

print(longer_input)
gilbert_output = Gilbert_Model(longer_input)
print("Gilbert:")
print (gilbert_output)
print("\n")

#print("Przeplot:")
#interleaving_output = decode_interleaving(interleaving('11010110',4), 4)

#print("przeplot i Gilbert")
#interleaving_output = decode_interleaving(Gilbert_Model(interleaving(bits,4)),4)


###Zdjecie Gilbert i interleaving i hamming
#image_output = load_image("image.jpg")
#coded = encode_interleaving_Hamming(image_output,16,4)
#gilb = Gilbert_Model(coded)
#picture = decode_interleaving_Hamming(gilb,7,4)
#save_image(picture, "gilb.jpg")

###Zdjecie Gilbert i Hamming
#image_output = load_image("image.jpg")
#coded = Ham(image_output)
#gilb = Gilbert_Model(coded)
#picture = DecodeHamm(gilb)
#save_image(picture, "gilb.jpg")


###Zdjecie Gilbert i przeplot
image_output = load_image("image.jpg")
coded = interleaving(image_output,4)
tmr = TMR(coded)
gilb = Gilbert_Model(tmr)
decoded = Decode(gilb)
picture = decode_interleaving(decoded,4)
#save_image(picture, "gilb_tmr.jpg")

###Zdjecie Gilbert
#image_output = load_image("image.jpg")
#gilb = Gilbert_Model(image_output)
#save_image(gilb, "gilb3.jpg")

###Zdjecie BSC
#image_output = load_image("image.jpg")
#output = BSC(image_output, 0.1)
#save_image(output, "bsc.jpg")

###Zdjecie TMR BSC
#image_output = load_image("image.jpg")
#tmr = TMR(image_output)
#bsc = BSC(tmr, 0.1)
#picture = Decode(bsc)
#save_image(picture, "tmr i bsc.jpg")

###Zdjecie BSC i hamming
#image_output = load_image("image.jpg")
#ham = Ham(image_output)
#bsc = BSC(ham,0.1)
#output = DecodeHamm(bsc)
#save_image(output, "bsc_hamm.jpg")

###Zdjecie BSC i przeplot
#image_output = load_image("image.jpg")
#inter = interleaving(image_output,4)
#bsc = BSC(inter, 0.1)
#picture = decode_interleaving(bsc,4)
#save_image(picture, "bsc_interleaving.jpg")

###Zdjecie TMR BSC Przeplot Hamming
#image_output = load_image("image.jpg")

#coded = encode_interleaving_Hamming(image_output,16,4) ###hamming po przeplocie
#tmr = TMR(coded)
#bsc = BSC(tmr, 0.1)
#out = Decode(bsc)
#picture = decode_interleaving_Hamming(out,7,4)

#save_image(picture, "przeplot_hamming_tmr_bsc.jpg")

print("Przeplot:")
interleaving_output = decode_interleaving(interleaving('110101',4), 4)
#interleaving_output = encode_interleaving(Gilbert_Model(interleaving('110101',4),0.1,0.9),4)


"""
