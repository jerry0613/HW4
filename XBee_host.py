import serial
import time
import matplotlib.pyplot as plt
import numpy as np

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())

s.write("ATMY 0x290\r\n".encode())
char = s.read(3)
print("Set MY 0x290.")
print(char.decode())

s.write("ATDL 0x920\r\n".encode())
char = s.read(3)
print("Set DL 0x920.")
print(char.decode())

s.write("ATID 0x1\r\n".encode())
char = s.read(3)
print("Set PAN ID 0x1.")
print(char.decode())

s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())

s.write("ATMY\r\n".encode())
char = s.read(4)
print("MY :")
print(char.decode())

s.write("ATDL\r\n".encode())
char = s.read(4)
print("DL : ")
print(char.decode())

s.write("ATCN\r\n".encode())
char = s.read(3)
print("Exit AT mode.")
print(char.decode())

print("start sending RPC")
N = []
s.write("/check/run\r".encode())
tmp = s.read(1)
print(tmp)
time.sleep(1)
s.write("/check/run\r".encode())
tmp = s.read(1)
print(tmp)
time.sleep(1)
s.write("/check/run\r".encode())
tmp = s.read(1)
print(tmp)
time.sleep(1)

t = []
while len(N) < 21:
    s.write("/check/run\r".encode())
    tmp = s.read(2)
    print(tmp)
    N.append(tmp)
    t.append(len(N))
    time.sleep(1)


print(N)
print(t)
plt.plot(t, N)
plt.ylabel("number")
plt.xlabel("timestamp")
plt.title('# collected data plot')
plt.show()    

s.close()