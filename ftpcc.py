############################################################################
# Team: Babylonians
# Members: Martin Brock, John Chung, Casey Fernandez, William Francis,
#           Joshua Mcdowell, Reid Naylor, Zachary Rogers
# Assignment: Program #3, FTP (storage) Covert Channel
# Date: 4/4/2019
# Description: This program fetches the file permissions from an ftp server
#               and converts it to english text using either a 7 bit
#               or 10 bit method.
############################################################################

import sys
import ftplib
from ftplib import FTP

# Change this either to 7 or 10 to fetch and read
#   the appropriate directory with the appropriate
#   method
METHOD = 7

# sets the host name and credentials to connect to ftp server
IP = "jeangourd.com"
PORT = "21"
USERNAME = "anonymous"
PASSWORD = ""

# Function that converts binary string to english string
def  make_string(binary, bitLength):

    # python list for holding all of the characters that
    #   are converted to from binary
    sent = []

    
    while True:

        # ch is the characters that are converted from binary
        ch = chr(int(binary[:bitLength], 2))

        # ignore if ch is backspace character
        if(ch == '\b'):
            sent = sent[:-1]

        # appends the character to the sent list
        else:
            sent.append(ch)

        if(len(binary) > bitLength):
            binary = binary[bitLength:]

        else:
            break

    # finMess is the final string to be printed
    finMess = ""

    # concatonates all the characters in the sent list to the finMess string
    for char in sent:
        finMess += char

    # returns the final string
    return finMess

# Function to connect to ftp server and retrieve the file permissions
# passed in direct (the directory to go to) and binLen( 7 or 10 )
def get_list(direct, binLen):
    
    # empty list to hold the permissions reading from ftp server
    data = []

    # goes to correct directory and appends the permission data to data
    ftp.cwd("/")
    fstr = ""
    ftp.cwd(direct)
    ftp.dir(data.append)

    for f in data:

        # if method is 7, check first three permissions and ignore
        #   any with something in the first three positions
        if(binLen == 7):
            if(f[0:3] != "---"):
                continue

            # if the first 3 are empty apply everything but those first three 
            #   to the string fstr
            else:
                fstr += f[3:10]

        # if method is 10, apply the whole permission set to the string fstr
        else:
            fstr += f[0:10]

    # return the string of permissions from the ftp server
    return fstr

# Function to convert the string of permissions to binary
# takes fstr (the string of permissions) and binLen(7 or 10)
def to_bin(fstr, binLen):

    # an empty string to store the binary message
    binary = ""

    # for each character in the fstr
    for ch in fstr:

        #if the character is - set the binary to 0
        if ch == "-":
            binary += "0"

        # if the character is anything but - set the binary to 1
        else:
            binary += "1"

    if binLen == 10:
        oldbin = binary
        binstrip = len(oldbin) - (len(oldbin) % 7)
        binary = oldbin[:binstrip]
    
    # replacing the binary string special characters with empty string
    data = binary
    data = data.replace('\n', '')
    data = data.replace('\r', '')
    data = data.replace('\r\n', '')
    data = data.replace(' ', '')

    if(data == ""):
        print("Binary string is empty. Exiting.")
        exit()

    # Calls for the binary string to be converted to english text
    if(len(data) % 7 == 0):
        finDat = make_string(data, 7)

    else:
        print("Binary is not 7 bits. Exiting.")
        exit()

    # returns the final string message 
    return finDat

#######################################################################################
# Main Controller of program
#######################################################################################

# establishes ftp connection
try:
    ftp = FTP()
    ftp.connect(IP, PORT)
    ftp.login(USERNAME, PASSWORD)

except ftplib.all_errors as err:
    print(err)
    exit()

# Calls for ftp data to be retrieved and converted for 7 bit method
if METHOD == 7:
    string = get_list('/7', METHOD)
    ftp.quit()
    message = to_bin(string, METHOD)

# Calls for ftp data to be retrieved and converted for 10 bit method
else:
    string = get_list('/10', METHOD)
    ftp.quit()
    message = to_bin(string, METHOD)

# Prints the final covert message
print(message)

