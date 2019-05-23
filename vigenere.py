# Program 2 - Vigenere Cipher
# Team: Babylonians
# Group Members: Martin Brock, John Chung, Casey Fernandez,William Francis,Joshua McDowell, Reid Naylor, Zachary Rogers
#
# Github Repository: https://github.com/joshuamcdowell/Vigenere.git


# VIGENERE CIPHER
import sys
from string import whitespace

# Interprets initial arguements, find out if encoding/decoding and the key to be used
def scan():
    typeMod = sys.argv[1]
    key = sys.argv[2]
    key = key.translate(None, whitespace)
    if(typeMod == "-e"):
        encode(key)

    elif (typeMod == "-d"):
        decode(key)

    else:
        print("Please enter -e or -d for encode or decode")
        exit()

# Encodes text using the passed key
def encode(k):
    while True:
        # Get input from user as text to encode
        phrase = sys.stdin.readline()
        encString = ""
        keyIter = 0

        # Check if text is valid
        if(phrase == ""):
            exit()
        elif '\n' in phrase:
            phrase = phrase[:len(phrase)-1]

        # Encode each character one at a time
        for i in range(0, len(phrase)):
            isSymb = False
            isCapital = False


            if 'a' <= phrase[i] <= 'z':
                # Lowercase
                phInt = ord(phrase[i]) - 97
            elif 'A' <= phrase[i] <= 'Z':
                # Uppercase
                phInt = ord(phrase[i]) - 65
                isCapital = True
            elif phrase[i] == ' ':
                # Space
                encString += ' '
                continue
            else:
                # Special character
                phInt = ord(phrase[i])
                isSymb = True

            if 'a' <= k[keyIter] <= 'z':
                # Lowercase of key
                keyInt = ord(k[keyIter]) - 97
            elif 'A' <= k[keyIter] <= 'Z':
                # Uppercase of key
                keyInt = ord(k[keyIter]) - 65
            else:
                # Key should only contain uppercase and/or lowercase characters
                print("Key contains non-alphabetical character.")
                exit()

            # Iterate key counter and make it loop
            if keyIter >= len(k) - 1:
                keyIter = 0
            else:
                keyIter += 1

            # Encode character
            if isSymb:
                # Special character remains the same
                encString += chr(phInt)
                keyIter -= 1 # Account for special character, key iterator should not increment
                if keyInt < 0:
                    keyInt = len(k) - 1
            elif isCapital:
                # Encode uppercase character
                encString += chr(((phInt + keyInt) % 26) + 65)
            else:
                # Encode lowercase character
                encString += chr(((phInt + keyInt) % 26) + 97)
                
        print(encString)

# Decodes text using the passed key
def decode(k):
    while True:
        # Get input from user as text to decode
        phrase = sys.stdin.readline()
        decString = ""
        keyIter = 0

        # Check if text is valid
        if(phrase == ""):
            exit()
        elif '\n' in phrase:
            phrase = phrase[:len(phrase)-1]

        # Decode each character one at a time
        for i in range(0, len(phrase)):
            isSymb = False
            isCapital = False


            if 'a' <= phrase[i] <= 'z':
                # Lowercase
                phInt = ord(phrase[i]) - 97
            elif 'A' <= phrase[i] <= 'Z':
                # Uppercase
                phInt = ord(phrase[i]) - 65
                isCapital = True
            elif phrase[i] == ' ':
                # Space
                decString += ' '
                continue
            else:
                # Special character
                phInt = ord(phrase[i])
                isSymb = True

            if 'a' <= k[keyIter] <= 'z':
                # Lowercase of key
                keyInt = ord(k[keyIter]) - 97
            elif 'A' <= k[keyIter] <= 'Z':
                # Uppercase of key
                keyInt = ord(k[keyIter]) - 65
            else:
                # Key should only contain uppercase and/or lowercase characters
                print("Key contains non-alphabetical character.")
                exit()

            # Iterate key counter and make it loop
            if keyIter >= len(k) - 1:
                keyIter = 0
            else:
                keyIter += 1

            # Decode character
            if isSymb:
                # Special character remains the same
                decString += chr(phInt)
                keyIter -= 1 # Account for special character, key iterator should not increment
                if keyInt < 0:
                    keyInt = len(k) - 1
            elif isCapital:
                # Decode uppercase character
                decString += chr(((26 + phInt - keyInt) % 26) + 65)
            else:
                # Decode lowercase character
                decString += chr(((26 + phInt - keyInt) % 26) + 97)
                
        print(decString)

# Check if the user entered the proper amount of arguments
if(len(sys.argv) >= 3):
    scan()
else:
    print("Too few arguments")

