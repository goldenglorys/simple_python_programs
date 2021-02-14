import math


def binary_to_decimal():
    binary_list = []
    result = 0
    binary = input('Enter the binary number:\n')
    binary_len = len(binary)
    for i in binary:
        binary_list.append(i)
    for data in binary_list:
        binary_len = binary_len - 1
        result += (int(data) * pow(2, binary_len))
    print(result)


# binary_to_decimal()


def bitwise():
#===== BINARY AND ========
    a = 50      #110010
    b = 25      #011001
    c = a & b   #010000
    print(c)

#===== BINARY RIGHT SHIFT =====
    x = 240     #11110000
    y = x >> 2  #00111100
    print(y)


bitwise()
