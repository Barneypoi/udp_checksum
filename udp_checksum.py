from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0,16)
a = "0110011001100000"
b = "0101010101010101"
c = "1000111100001100"
y = np.array([])

def sumup(a,b):
    seq = int(a, 2) + int(b, 2)
    if seq >= 65536:
        seq = seq - 65535
    seq = bin(seq)[2:].zfill(16)
    return seq

seq = sumup(sumup(a,b),c)

#求补码
for i in seq:
    if i == '0':
        i = 1
    else:
        i = 0
    y= np.append(y,i)
print(y)
plt.plot(x,y)
plt.show()

