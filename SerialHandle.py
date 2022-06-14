import serial
from mnist import MNIST
import random, struct, binascii


mndata = MNIST('samples')
mndata.gz = True
images, labels = mndata.load_training()

s = serial.Serial('COM6')
s.timeout = 100
# struct.pack("!f", 4.1)
# a.append(int.from_bytes(res, "big"))
def send(index):
    print("sending:", labels[index])
    data = b''
    for i in images[index]:
        #data += i.to_bytes(1, "big")
        data += struct.pack("!f", i/256)
    s.write(data)
    a = b''
    for i in range(40):
        res = s.read()
        a+=res
    #print(a, len(a))
    b = []
    for i in range(10):
        f = struct.unpack('f', a[4*i:4*i+4])
        b.append(f)
    #for i in range(len(b)):
        #print(i, b[i])
    return a

def getNum(a):
    max_value = max(a)
    index = a.index(max_value)
    return index

def p(a):
    for i in range(10):
        print(binascii.hexlify(bytearray(a[4*i:4*i+4])))
    print()

