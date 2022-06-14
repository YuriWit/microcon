import serial
from mnist import MNIST
import random


mndata = MNIST('samples')
mndata.gz = True
images, labels = mndata.load_training()

s = serial.Serial('COM6')
s.timeout = 100

def send(index):
    print("sending:", labels[index])
    data = b''
    for i in images[index]:
        data += i.to_bytes(1, "big")
    s.write(data)
    a = []
    for i in range(10):
        res = s.read()
        a.append(int.from_bytes(res, "big"))
    print(getNum(a))

def getNum(a):
    max_value = max(a)
    index = a.index(max_value)
    return index


