from numpy import array

def TMR(input):

    input_bits = input.copy()
    output_bits = []

    for i, bit in enumerate(input_bits):
        output_bits.append(input_bits[i])
        output_bits.append(input_bits[i])
        output_bits.append(input_bits[i])

    return array(output_bits)

def Decode(input):

    output = []

    for i in range(0, len(input), 3):
        if input[i] == input[i + 1] and input[i + 1] == input[i + 2]:
            output.append(input[i])
        else:
            suma = input[i]
            suma += input[i + 1]
            suma += input[i + 2]

            if suma > 1:
                output.append(1)
            else:
                output.append(0)

    return array(output)