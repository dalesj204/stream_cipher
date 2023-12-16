file = open('raw.txt', 'r')
lines = file.readlines()
decoded_lines = []
for line in lines:
    decoded_lines.append(line.strip().decode('hex'))


def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


xor_cipher0 = strxor(decoded_lines[0], decoded_lines[8])
xor_cipher1 = strxor(decoded_lines[1], decoded_lines[8])
xor_cipher2 = strxor(decoded_lines[2], decoded_lines[8])
xor_cipher3 = strxor(decoded_lines[3], decoded_lines[8])
xor_cipher4 = strxor(decoded_lines[4], decoded_lines[8])
xor_cipher5 = strxor(decoded_lines[5], decoded_lines[8])
xor_cipher6 = strxor(decoded_lines[6], decoded_lines[8])
xor_cipher7 = strxor(decoded_lines[7], decoded_lines[8])
# xor_cipher8 = strxor(decoded_lines[8], decoded_lines[8]) # figured out the longest cipher
xor_cipher9 = strxor(decoded_lines[9], decoded_lines[8])


print(strxor(xor_cipher0, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.")) # 0
print(strxor(xor_cipher1, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.")) # 1
print(strxor(xor_cipher2, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.")) # 2
print(strxor(xor_cipher3, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.")) # 3
print(strxor(xor_cipher4, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.")) # 4
print(strxor(xor_cipher5, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.")) # 5
print(strxor(xor_cipher6, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.")) # 6
print(strxor(xor_cipher7, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.")) # 7
print("When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.") # 8, longest cipher

print(strxor(xor_cipher9, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.")) # 9

file = open('jordan_stream.txt', 'w+')
file.write(strxor(xor_cipher0, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.") + "\n") # 0
file.write(strxor(xor_cipher1, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.") + "\n") # 1
file.write(strxor(xor_cipher2, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.") + "\n") # 2
file.write(strxor(xor_cipher3, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.") + "\n") # 3
file.write(strxor(xor_cipher4, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.") + "\n") # 4
file.write(strxor(xor_cipher5, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.") + "\n") # 5
file.write(strxor(xor_cipher6, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.") + "\n") # 6
file.write(strxor(xor_cipher7, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.") + "\n") # 7
file.write("When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.\n") # 8
file.write(strxor(xor_cipher9, "When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.")) # 9

# OLD XOR FUNCTION
# def xor(c1, c2):
#     result = '';
#     if len(c1) > len(c2):
#         for c in range(len(c2)):
#             x = ord(c1[c])
#             y = ord(c2[c])
#             result += chr(x ^ y)
            
#     else:
#         for c in range(len(c1)):
#             x = ord(c1[c])
#             y = ord(c2[c])
#             result += chr(x ^ y)
            
#     return result
