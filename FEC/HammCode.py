import numpy
import random




def Ham(input_bits):

    G = numpy.array([[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

    code = G.dot(input_bits)
    code = code % 2

    return code

def DecodeHamm(code):

    H = numpy.array([[1,0,1,0,1,0,1],[0,1,1,0,0,1,1],[0,0,0,1,1,1,1]])
    syndrom = H.dot(code)
    syndrom = syndrom % 2


    # print("Bit ulegl zmianie na pozycji:")
    position = 1 * syndrom[0] + 2 * syndrom[1] + 4 * syndrom[2] - 1
    # print(position+1)

    # print("Kod po naprawie:")
    if(position>=0 and position<7):
        if (code[position] == 0):
            code[position] = 1
        else:
            code[position] = 0

    decoded = [code[2],code[4],code[5],code[6]]


    return decoded

def HamEncode(code):

    output = []
    for_hamming = []
    number_of_parts_hamming = round(len(code)/4)
    for k in range(number_of_parts_hamming):
        for l in range(4):
            for_hamming.append(int(code[4*k+l]))
        temp = Ham(for_hamming)
        for m in range(7):
            output.append(temp[m])
        for_hamming = []



    return numpy.asarray(output,dtype = int)

def HamDecode(code):

    output = []
    for_hamming = []

    number_of_parts_hamming = round(len(code)/7)
    for k in range(number_of_parts_hamming):
        for l in range(7):
            for_hamming.append(int(code[7*k+l]))
        temp = DecodeHamm(for_hamming)
        for m in range(4):
            output.append(temp[m])
        for_hamming = []

    return numpy.asarray(output,dtype = int)












    # print("Bit ulegl zmianie na pozycji:")
    position = 1 * syndrom[0] + 2 * syndrom[1] + 4 * syndrom[2] - 1
    # print(position+1)

    # print("Kod po naprawie:")
    if(position>=0 and position<7):
        if (code[position] == 0):
            code[position] = 1
        else:
            code[position] = 0

    decoded = [code[2],code[4],code[5],code[6]]


    return decoded