# Program 1 - Binary Decoder
# Team: Babylonians
# Group Members: Martin Brock, John Chung, Casey Fernandez,William Francis,Joshua McDowell, Reid Naylor, Zachary Rogers
#
# Github Repository: https://github.com/joshuamcdowell/BinaryDecoder.git


# PYTHON BINARY INTERPRETER
import sys

# Takes binary data, and chunk size and converts it into its ASCII characters.
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

    print
    for char in sent:
        sys.stdout.write(char)
    print

# Removes whitespaces
def clean(string):
    string = string.replace(' ', '')
    string = string.replace('\n', '')
    return string


# Read the binary data from standard input and remove all whitespaces
bi = sys.stdin.read()
bi = clean(bi)

# Check for input
if(bi == ""):
    print("No Input Recieved")
    exit()

# See if the binary data is divisible into chunks of 7 and/or 8 bits and then convert it to text respectively
biLen = len(bi)
if(biLen % 8 == 0 and biLen % 7 == 0):
    make_string(bi, 7)
    make_string(bi, 8)

elif(biLen % 7 == 0):
    make_string(bi, 7)

elif(biLen % 8 == 0):
    make_string(bi, 8)

else:
    print("Not comprised of only 7 bits or only 8 bits.")
    exit()
