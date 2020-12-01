# Solar-Tracker-IoT
An IoT and ML based dual axis Solar Tracker using an Arduino and Raspberry Pi

## Overview
This project was designed to obtain a solar panel that is able to harvest its maximum possible power for as long as possible thereby improving its efficiency.
With the help of an Arduino, Raspberry Pi and a simple ML algorithm, a solar panel is enabled to track the sun, rotate and position itself accordingly such that no part of the solar array is covered by shade due to any obstructing factors. A smart mechanical system is implemented to adjust the panel to a better angle and position to re-obtain maximum current and voltage therefore producing maximum power output.

## Components Used
1. Photoresistors (LDRs)
2. Servo Motors
3. Arduino Uno
4. Raspberry Pi Zero
5. Solar Panel
6. 12V Battery (Power supply) 

## Solar Energy Optimization
This project aims to build a model of a smart solar panel that faces the sun as it moves during the duration of the day. Furthermore, to improve the device by building a Machine Learning model to predict where the panel needs to be facing at different parts of the day to make it usable in any terrain without a sensor. <br/>
<br/>
![solar](/demo_solar.png)
<br/>
<br/>
The flat platform on which the panel is placed has 4 LDR sensors in the corners. Servo motors are used to rotate the panel. The sensors and the motors are connected to an Arduino Uno which is then connected to a Raspberry Pi. Refer Solar tracking Proj.pptx for more details regarding the circuit <br/>
Firstly, IoTproj.ino is run. This code moves the panel according to the direction of the light by observing the light intensity values of the four sensors. Additionally, the sending.py code is run in the Raspberry Pi simultaneously to record the values of the Servo Motor with the timestamp in which it was received. This helps in creating a regression model which will predict the angle in which the Motor needs to turn in different parts of the day. <br/>
<br/>
Finally, the work.py code is run which has the regression model to give values to the servo motor in different times of the day to make it turn towards the sun using this code and not the sensors. </br>
