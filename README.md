# Due 9/14/2014  (50 points)


## Name
Sam Korn

## Hardware Photo (7 points)
![image][LoggerPCB.png]
![image][LoggerSchematic.png]
![image][LoggerWorld1.jpg]
![image][LoggerWorld2.jpg]
![image][LoggerWorld3.jpg]


## Data type (2 points) 
Tab Seperated Values

## How did you get your prototype working? (7 points)
I made my prototype PCB at the ITLL Electronics Center. I started with DHT22 example code from Adafruit.com and built addition functionality around it in order to timestamp and save the data as a tab sepeared value.

## Arduino Code (10 points)
DHTSparkfun.py

## Data Sample (7 points)
[Replace the sample data file in this repo with your data file, then put the name of your file here]

## How did you collect this data? (5 points)
Since I still needed to be able to command the Raspberry Pi to begin taking in data I had to keep it attached to an ethernet cable. I put the sensor outside of my closed window and kept the Raspberry Pi inside of my house where it could be connected to a MicroUSB cable and Ethernet.

## What signal do you think is in your data? (3 points)
Since the DHT22 uses a 1-wire communication bus in order to send digital data, I know exactly what fields are temperature and what fields are humidity and the exact values of those fields. This is much more accurate than an AnalogRead on a pin connected to a microphone or a light sensor.

## How fun was this mini-project? (3 points)
7. Making the hardware was more fun than writing the software and dealing with Linux. Had issues with Python because I am less fluent in it than I am in C. 

## How hard was it? (3 points)
6. Making the hardware was relatively easy. I have made a smaller DHT22 prototype PCB before, so this one only had the additional two LEDs to make it different. My time function on the Raspberry Pi returns the time in UTC, and I was not able to figure out how to get it to local time during my time programming. I wish I was a little more familiar with Linux startup commands, writing to files, and Python.

## How much did you learn from the experience? (3 points)
4. The PCB was pretty easy to make and I already knew how to do it. I have written code based of the Adafruit DHT library before, but I have never had to save the data to a file or try to make custom code run at boottime for a Linux machine. Getting the Sparkfun data storage to work was the most difficult part for me, because it was a completely new thing to do.
