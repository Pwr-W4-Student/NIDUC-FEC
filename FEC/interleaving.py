
from HammCode import Ham
from HammCode import DecodeHamm
import numpy

def interleaving(input_bits, verse_length): #na jakie segmenty chcemy dzielić bity

    column_length = round(len(input_bits)/verse_length)

    array = [None] * column_length
    for i in range(column_length):
        array[i] = [None] * verse_length

    for i in range(column_length):
        for j in range(verse_length):
            if(len(input_bits) > verse_length * i + j):
                array[i][j] = input_bits[verse_length * i + j]

    #print(array)

    output_bits = []
    for i in range(verse_length):
        for j in range(column_length):
                output_bits.append(array[j][i])

    #print(output_bits)
    #print("\n")
    return numpy.asarray(output_bits,dtype = int)


def decode_interleaving(input_bits, verse_length): #na jakie segmenty chcemy dzielić bity
    
    #print(input_bits)
    length = len(input_bits)
    column_length = round(length/verse_length)

    array = [None] * column_length
    for i in range(column_length):
        array[i] = [None] * verse_length

    for i in range(verse_length):
        for j in range(column_length):
            array[j][i] = input_bits[column_length * i + j]

    #print(array)

    output_bits = []
    for i in range(column_length):
        for j in range(verse_length):
                output_bits.append(array[i][j])


    #print(output_bits)
    return numpy.asarray(output_bits,dtype = int)


def encode_interleaving_Hamming(input_bits,how_many_bits_interleaving,how_many_bits_hamming): #pomocnicza polaczenie przeplotu i Hamminga
    number_of_parts_interleaving = round(len(input_bits)/how_many_bits_interleaving) ###16 - za pierwszym razem by miec 4x4 i potem 4 zeby uzyc do Hamminga
    for_interleaving = []
    for_hamming = []
    output_bits = []

    for i in range(number_of_parts_interleaving):
        for j in range(how_many_bits_interleaving):
            for_interleaving.append(int(input_bits[how_many_bits_interleaving*i+0+j]))
        next_bits=interleaving(for_interleaving,4)
        for_interleaving = []

        number_of_parts_hamming = round(len(next_bits)/how_many_bits_hamming)

        for k in range(number_of_parts_hamming):
            for l in range(how_many_bits_hamming):
                for_hamming.append(int(next_bits[how_many_bits_hamming*k+0+l]))
            temp = Ham(for_hamming)
            for m in range(7):
                output_bits.append(temp[m])
            for_hamming = []

    return numpy.asarray(output_bits,dtype = int)


def decode_interleaving_Hamming(input_bits, how_many_bits_hamming,
                                how_many_bits_interleaving):  # pomocnicza polaczenie przeplotu i Hamminga
    number_of_parts_hamming = round(
        len(input_bits) / how_many_bits_hamming)  ###16 - za pierwszym razem by miec 4x4 i potem 4 zeby uzyc do Hamminga

    for_hamming = []
    output_bits = []
    next_bits = []

    for i in range(number_of_parts_hamming):
        for j in range(how_many_bits_hamming):

            for_hamming.append(input_bits[how_many_bits_hamming * i + 0 + j])

        temp = DecodeHamm(for_hamming)
        for k in range(4):
            next_bits.append(temp[k])
        for_hamming = []


    output_bits = decode_interleaving(next_bits, how_many_bits_interleaving)
    return numpy.asarray(output_bits,dtype = int)

