#Pillow:
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#TFT, GPIO, SPI:
import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

#GPS:
import serial
import time
import string
import pynmea2

import subprocess

#RPi.GPIO:
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
GPIO.setmode(GPIO.BCM) 

leftled = LED(17) 
GPIO.setup(6, GPIO.IN)

rightled = LED(27)
GPIO.setup(16, GPIO.IN)


#SPI config:
DC = 25
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0



# Create TFT LCD display class.
disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))

# Initialize display.
disp.begin()


# Call blank screen:
disp.clear()

# Get a PIL Draw object to start drawing on the display buffer.
draw = disp.draw()

#SF Pro by Apple:
font110 = ImageFont.truetype("SF-Pro.ttf", 110)
font32 = ImageFont.truetype("SF-Pro.ttf", 32)
#Carcycle:
carcycle = ImageFont.truetype("carcycle.ttf", 65)
carcyclesmall = ImageFont.truetype("carcycle.ttf", 45)


#Width/height:
height = disp.width
width = disp.height

left = 0
right = 0
light = 0
    
draw.text((5,0), "A", font=carcycle, fill="#00ff00")
draw.text((190,0), "B", font=carcycle, fill="#00ff00")
draw.text((65,10), "C", font=carcyclesmall, fill="#0000FF")
draw.text((120,10), "D", font=carcyclesmall, fill="#FFFF00")
draw.text((90, 90), "--", font=font110, fill="#FFFFFF")
draw.text((100, 210), "kph", font=font32, fill="#FFFFFF")
disp.display()
rightled.on()
leftled.on()
time.sleep(2)
while True:
	port="/dev/serial0"
	ser=serial.Serial(port, baudrate=9600, timeout=0.5)
	dataout = pynmea2.NMEAStreamReader()
	newdata=ser.readline()
	if newdata[0:6].decode("utf-8") == '$GPRMC':
			
		newmsg=pynmea2.parse(newdata.decode("utf-8"))
		lat=newmsg.latitude
		lng=newmsg.longitude
		gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
		newDataLines = newdata.decode("utf-8").splitlines()
		#print(str(newmsg.spd_over_grnd_kmph))
		
		newdata=ser.readline()
		newmsg=pynmea2.parse(newdata.decode("utf-8"))
		speed=str(newmsg.spd_over_grnd_kmph)
		if speed != "None":
			 bikeSpeed, deci = speed.split(".")
			 print(bikeSpeed)
			 draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
			 draw.text((90, 90), bikeSpeed, font=font110, fill="#FFFFFF")
			 draw.text((100, 210), "kph", font=font32, fill="#FFFFFF")
			 draw.text((5,0), "A", font=carcycle, fill="#A9A9A9")
			 draw.text((190,0), "B", font=carcycle, fill="#A9A9A9")
			 
			 draw.text((125,10), "D", font=carcyclesmall, fill="#A9A9A9")
			 if light == 1:
				 draw.text((65,10), "C", font=carcyclesmall, fill="#0000FF")
			 else: 
				 draw.text((65,10), "C", font=carcyclesmall, fill="#A9A9A9")
			 print("printing")
			 disp.display()
			 print("rpinted")
		else:
			 draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
			 draw.text((90, 90), "--", font=font110, fill="#FFFFFF")
			 draw.text((100, 210), "kph", font=font32, fill="#FFFFFF")
			 draw.text((5,0), "A", font=carcycle, fill="#A9A9A9")
			 draw.text((190,0), "B", font=carcycle, fill="#A9A9A9")
			 
			 draw.text((125,10), "D", font=carcyclesmall, fill="#A9A9A9")
			 if light == 1:
				 draw.text((65,10), "C", font=carcyclesmall, fill="#00ff00")
			 else: 
				 draw.text((65,10), "C", font=carcyclesmall, fill="#A9A9A9")
			 print("printing")
			 disp.display()
			 print("rpinted")
	
	cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk \'{printf \"CPU Temp: %.1f C\", $(NF-0) / 1000}\'" # pylint: disable=line-too-long
	Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")
	parts = Temp.split()
	temperature = float(parts[2])
	# Print the extracted temperature
	
	if GPIO.input(6) == 1:
		draw.text((5,0), "A", font=carcycle, fill="#00ff00")
		disp.display()
		leftled.on()
		time.sleep(0.2)
		draw.text((5,0), "A", font=carcycle, fill="#A9A9A9")
		disp.display()
		leftled.off()

		
	elif GPIO.input(16) == 1:
		draw.text((190,0), "B", font=carcycle, fill="#00ff00")
		disp.display()
		rightled.on()
		time.sleep(0.2)
		draw.text((190,0), "B", font=carcycle, fill="#A9A9A9")
		disp.display()
		rightled.off()
		
	else:
		rightled.off()
		
	
	
	if temperature > 75:	
		draw.text((120,10), "D", font=carcyclesmall, fill="#FFFF00")
		disp.display()
		
	time.sleep(0.1)

