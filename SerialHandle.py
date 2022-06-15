import serial
from mnist import MNIST
import random, struct, binascii
import numpy as np


mndata = MNIST('samples')
mndata.gz = True
images, labels = mndata.load_training()

s = serial.Serial('COM6')
s.timeout = 100
# struct.pack("!f", 4.1)
# a.append(int.from_bytes(res, "big"))
def send(index):
    #print("sending:", labels[index])
    data = b''
    for i in images[index]:
        #data += i.to_bytes(1, "big")
        #val = i^255
        val = i
        data += struct.pack("!f", val/256)
        #data += struct.pack("!i", i)
    s.write(data)
    a = b''
    for i in range(40):
        res = s.read()
        a+=res
    #print(a, len(a))
    b = []
    return a

def getNum(a):
    max_value = max(a)
    index = a.index(max_value)
    return index

def h(a):
    for i in range(10):
        print(binascii.hexlify(bytearray(a[4*i:4*i+4])))
    print()

def f(a):
    b = []
    for i in range(10):
        f = struct.unpack('f', a[4*i:4*i+4])
        b.append(f)
        #print(i,"{:.2f}".format(f[0]))
    c = np.array(b)
    return np.argmax(c)

def test(i):
    a = send(i)
    ip = f(a)
    ir = labels[i]
    if ip==ir:
        #print(i)
        return True
    return False

def runStat():
    a = 0
    for i in range(60000):
        if test(i):
            a+=1
            print(a/(i+1), end='\r')

index = random.randrange(0, len(images))
print(index, labels[index], f(send(index)))