# Program 6 - XOR Crypto
# Team: Babylonians
# Group Members: Martin Brock, John Chung, Casey Fernandez, William Francis, Joshua McDowell, Reid Naylor, Zachary Rogers
#
# Github Repository: https://github.com/joshuamcdowell/XOR.git


# XOR Crypto
import sys


# Takes two character inputs and compares them with XOR logic
def xor(b1, b2):
    output = '-1'
    if((b1 == '0' and b2 == '0') or (b1 == '1' and b2 == '1')): # same bits
        output = '0'
    elif((b1 == '0' and b2 == '1') or (b1 == '1' and b2 == '0')): # different bits
        output = '1'
    return output

# Adds leading 0s to make a full byte
def toByte(bits):
    byte = bits
    if(len(bits) != 8):
        # Do not already have a byte
        while(len(byte) != 8):
            byte = "0" + byte
    return byte

# Convert binary to string
def make_string(binary, bitLength):
    sent = []

    while True:
        ch = chr(int(binary[:bitLength], 2))

        if(ch == '\b'):
            sent = sent[:-1]

        else:
            sent.append(ch)

        if(len(binary) > bitLength):
            binary = binary[bitLength:]

        else:
            break

    for char in sent:
        sys.stdout.write(char)
    print


# Get key data
keyName = 'key' # Filename of key
with open(keyName, mode="rb") as file:
    content = file.read()
# Get input data
inText = sys.stdin.read()

# Convert key and cipher data to binary
keyBin = ' '.join(format(x, 'b') for x in bytearray(content))
cipherTextBin = ' '.join(format(x, 'b') for x in bytearray(inText))

# For each bit in the cipher text, xor it with the key and store result
calculating = True

c_Byte = "" # Current cipher byte
k_Byte = "" # Current key byte

c_ByteFound = False
k_ByteFound = False

c_counter = 0 # Current index of cipher position
k_counter = 0 # Current index of key position

result = "" # All converted bytes
resultByte = "" # Byte currently XOR'ed

while(calculating):

    # Check if both bytes are found and ready to be XOR'ed
    if(c_ByteFound and k_ByteFound):
        # XOR bits
        for i in range(0, 8):
            resultByte = resultByte + xor(c_Byte[i], k_Byte[i])
        result = result + resultByte # When byte is done being converted, add it to final result
        # Reset values to prepare for next byte conversion      
        resultByte = ""
        c_Byte = ""
        k_Byte = ""
        c_ByteFound = False
        k_ByteFound = False

        c_counter = c_counter + 1
        k_counter = k_counter + 1

    # Loop through the key    
    if(k_counter == len(keyBin)):
        k_counter = 0

    # FIND CIPHER AND KEY BYTES
    # If have not found entire cipher byte
    if(c_ByteFound == False):
        if(cipherTextBin[c_counter] != " "):
            # Still adding to byte
            c_Byte = c_Byte + cipherTextBin[c_counter]
            c_counter = c_counter + 1
        else:
            # End of cipher byte
            if(len(c_Byte) < 8):
                c_Byte = toByte(c_Byte) # Add leading 0s so bytes are same size
            c_ByteFound = True

    # If have not found entire key byte
    if(k_ByteFound == False):
        if(keyBin[k_counter] != " "):
            # Still adding to byte
            k_Byte = k_Byte + keyBin[k_counter]
            k_counter = k_counter + 1
        else:
            # End of key byte
            if(len(k_Byte) < 8):
                k_Byte = toByte(k_Byte) # Add leading 0s so bytes are same size
            k_ByteFound = True

    # When all of ciphertext is converted, exit
    if(c_counter == len(cipherTextBin)):
        calculating = False

# Convert the binary result to a string which also prints it to stdout
make_string(result, 8)
