import serial #import the serial library
from vpython import *#import vpython library

arduinoSerialdata= serial.Serial('COM11',9600) #read the serial port

myobject= cylinder(length=2, color=color.green, radius=1.5,pos=vector(-8,0,0),axis=vector(0,1,0))
lab=label(text='Tube 01',box=False,pos=vector(-8,0,0))

while(1):#loop forever
    rate(20)
    if (arduinoSerialdata.inWaiting()>0):#check whether there is data on serial port or not
        mydata=arduinoSerialdata.readline()#read the data if there is any data
        radius = float(mydata) 
        if (radius==0):
            radius=0.1
        elif(radius==5):
            lab.text='Tube 01 - FULL'
        else:
            lab.text='Tube 01'
        print (radius)
        myobject.length=radius
        if (radius>4):
            myobject.color=color.red
        elif(radius>3):
            myobject.color=color.yellow
        else:
            myobject.color=color.green
        
    
