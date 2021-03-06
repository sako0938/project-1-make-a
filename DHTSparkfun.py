#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
import os
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setwarnings(False)
# Parse command line parameters.
#sensor_args = { '11': Adafruit_DHT.DHT11,
#				'22': Adafruit_DHT.DHT22,
#				'2302': Adafruit_DHT.AM2302 }
#if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
#	sensor = sensor_args[sys.argv[1]]
#	pin = sys.argv[2]
#else:
#	print 'usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#'
#	print 'example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4'
#	sys.exit(1)
sensor = 22
pin = 14
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).  
# If this happens try again!
#Get filename for data from user.
extend = raw_input("Input the filename ending.\n")
filename = "DHTdata" + str(extend)
file = open(filename,'w')
file.write("Temperature \t Humidity \t Time\n")
privatekey = 'NWnVXJyyJESPBJBzq4jM'
publickey = 'G2EnvwNNwMSq7278lKDo'
while True:
	time.sleep(3)
	GPIO.output(23, GPIO.HIGH)
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
		print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
	else:
		print 'Failed to get reading. Try again!'
	 GPIO.output(23, GPIO.LOW)
	currenttime = time.asctime( time.localtime(time.time()) )
	commandstring = """curl -X GET "http://data.sparkfun.com/input/""" + publickey + """?private_key=""" + privatekey + """&humidity={:0.1f}&temperature={:0.1f}" """.format(humidity, temperature)
	print commandstring
	os.system(commandstring)
	# file.write('Temp={:0.1f}*C  \t Humidity={:0.1f}% \t Time={:s}\n'.format(temperature, humidity,currenttime) )
	
