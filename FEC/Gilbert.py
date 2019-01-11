#from numpy.random import random
import numpy

def Gilbert_Model(packet2, omg_error=0.3, no_error_mate=0.02):
  packet = packet2.copy()
  state = omg_error
  for idx, bit in enumerate(packet):
    the_bit_flips = numpy.random.binomial(1,state)
    if the_bit_flips:
      if state == no_error_mate:
        state = omg_error
      packet[idx] = 1 - packet[idx]
    else:
      if state == omg_error:
        state = no_error_mate
  return packet