from mnist import MNIST
import numpy as np
import serial, random, struct


# set constants
RESP_SIZE = 40 #bytes
PRINT_ON = True
DEBUG_ON = False

# defining the predict function recives the index of the image to use from data set
def predict(index):
    # process input data
    data = b''
    for byte in images[index]:
        byte = byte^255 #invert bits [the model does it in TFKpredict.py]
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
        arr.append(struct.unpack('!f', resp[4*i:4*i+4]))
    arr = np.array(arr)

    # get value or prediction
    prediction = np.argmax(arr)
    return prediction


# get data set
mndata = MNIST('samples')
mndata.gz = True
images, labels = mndata.load_training()

# open conection
s = serial.Serial('COM6')

# choose random image from data set
index = random.randrange(0, len(images))

# predict
prediction = predict(index)

# print result
if PRINT_ON:
    print("data set index:", index)
    print("image label:", labels[index])
    print("prediction:", prediction)



# debug section
if DEBUG_ON:
    dic = {}
    for i in range (10):
        for j in range (10):
            key = str(i)+str(j)
            dic[key] = 0

    for i in range (1000):
        val = labels[i]
        pre = predict(i)
        key = str(val)+str(pre)
        dic[key] += 1

    print("on the left we have value on the right we have what the ai predicted")
    for i in range (10):
        print(i, end=' ----- ')
        for j in range (10):
            key = str(i)+str(j)
            print(dic[key], end='\t')
        print()
