from mnist import MNIST
import numpy as np
import serial, random, struct


# set constants
RESP_SIZE = 40 #bytes


# get data set
mndata = MNIST('samples')
mndata.gz = True
images, labels = mndata.load_training()

# open conection
s = serial.Serial('COM6')

# choose random image from data set
index = random.randrange(0, len(images))

# process input data
data = b''
for byte in images[index]:
    #byte = byte^255                        # atempt to invert bits (model does that for some reason) didn't work
    data += struct.pack("!f", byte/255)

# send data
s.write(data)

# recive response
resp = b''
for i in range(RESP_SIZE):
    resp += s.read()

# form np array
arr = []
for i in range(10):
    arr.append(struct.unpack('f', resp[4*i:4*i+4]))
arr = np.array(arr)

# get value or prediction
prediction = np.argmax(arr)

# print result
print("data set index:", index)
print("image label:", labels[index])
print("prediction:", prediction)