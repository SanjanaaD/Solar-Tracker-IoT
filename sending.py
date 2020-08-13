import serial
import pandas as pd

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]
k=0
no=0
H=[]
V=[]
time=[]
while True:
  if(ser.readline()):
    k=k+1
    read_serial=ser.readline().decode("utf-8")
    if(k==1):
      print("H: ")
      H.append(read_serial.strip("\r\n'").strip("b'"))
    elif(k==2):
      print("V: ", read_serial.strip("\r\n'").strip("b'"))
      V.append(read_serial.strip("\r\n'").strip("b'"))
    elif(k==3):
      print("time: ", read_serial.strip("\r\n'").strip("b'")) 
      time.append(read_serial.strip("\r\n'").strip("b'"))
      k=0
      no=no+1
      if no>10:
        break
    
df1= pd.DataFrame(H) 
df2=pd.DataFrame(H)
df3= pd.DataFrame(time)

result = pd.concat([df1, df2, df3], axis=1, sort=False)
