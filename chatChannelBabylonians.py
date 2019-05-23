# Program 4 - chat Covert chan
# Team: Babylonians
# Group Members: Martin Brock, John Chung, Casey Fernandez,William Francis,Joshua McDowell, Reid Naylor,    	Zachary Rogers
# Date: 4/27/2019
# Github: https://github.com/joshuamcdowell/ChatCovertChannel.git

import socket, sys
from binascii import hexlify
from binascii import unhexlify
from time import time

# server variables
ZERO = .025
ONE = .08
BITS = 8
IP = "192.168.1.119"
PORT = 31339


# connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))


covert_bin = ""
print("Message:")

# list of all timings
timinglist = []

data = s.recv(4096)

# do loop until EOF is read
while(data.rstrip("\n") != "EOF"):

    # write the message out as its received
    sys.stdout.write(data)
    sys.stdout.flush()

    # get timing of each character sent
    t0 = time()
    data = s.recv(4096)
    t1 = time()
    deltaT = round(t1-t0, 3)

    # appends timing to list of timings
    timinglist.append(deltaT)
    
    # if timing is greater than a certain value its a 1, else 0
    if(deltaT >= ONE):
        covert_bin += "1"
    else:
        covert_bin += "0"

# Close connection
s.close()


covert = ""
i = 0

# Decodes the message from binary to characters
while(i < len(covert_bin)):
    b = covert_bin[i:i + BITS]
    n = int("0b{}".format(b), 2)

    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"

    i += BITS

# prints the covert message
print("\n\nCovert:")
print(covert)

# Prints the timings list
#print("\n\nTiming List:")
#for i in range(len(timinglist)):
    #sys.stdout.write(str(timinglist[i]))



