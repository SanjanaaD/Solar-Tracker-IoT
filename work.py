import pandas as pd
import time
import serial


data=pd.read_csv('Storage.csv')
y1=data.iloc[:,1:2]
y2=data.iloc[:,2:3]
X=data.iloc[:,3:4]

ser = serial.Serial('/dev/ttyACM0',9600)
ser.flushInput()

from sklearn.preprocessing import PolynomialFeatures
poly_reg1 = PolynomialFeatures(degree = 2)
X_poly = poly_reg1.fit_transform(X)

from sklearn.linear_model import LinearRegression
p1=LinearRegression()
p2=LinearRegression()
p1.fit(X_poly, y1)
p2.fit(X_poly, y2)


t1=time.time()
while True:
    time.sleep(2)
    t2=((time.time()-t1)*1000) 
    b=str(p1.predict(poly_reg1.transform([[t2]]))[0][0])
    a=str(p2.predict(poly_reg1.transform([[t2]]))[0][0])
    ser.write(str.encode('<Yo,'+a+ ',' +b+ '>'))
    print(str.encode('<Yo,'+a+ ',' +b+ '>'))