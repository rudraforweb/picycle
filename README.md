# picycle
Accessory for bicycles with Raspberry Pi!
![Screenshot_2024-07-29_at_5 16 42_PM-removebg-preview](https://github.com/user-attachments/assets/4173ac8d-9a3d-4256-a5ec-2ea9102b92e8)

⚠️ THIS PROJECT IS NOT FINISHED ⚠️

##### version: v0.6-beta

The main goal of this is to show speed on a display.
I have also included other things such as:
* Turn signals
* Headlights
* Overheating indicatior
and more to come! (if im not lazy)

## materials:

* [ILI9341](https://www.amazon.com/dp/B0B1M9S9V6) with the [Adafruit_Python_ILI9341 library](https://github.com/adafruit/Adafruit_Python_ILI9341/tree/master),
* [NEO-6M GPS Module](https://www.amazon.com/GY-NEO6MV2-Module-Antenna-Arduino-Control/dp/B0CMV4JTX2) with [pynmea2](https://github.com/Knio/pynmea2) as the parser,
* [Raspberry Pi Zero W](https://www.amazon.com/Raspberry-Pi-Zero-Wireless-model/dp/B06XFZC3BX), you can get it from anywhere, it doesn't matter, and don't use the Zero 2 W if you don't have a 12W battery bank.
* Battery bank: [Mophie Powerstation](https://www.amazon.com/powerstation-Lightning-Connector-iPhone-Devices/dp/B07N28VKYQ), it isn't avaiable anymore so you much have to use a different battery bank.
* [3 way switch](https://www.amazon.com/dp/B085L9HFW2), for turn signals, headlight, and turn off.
* [Hinge switch](https://www.amazon.com/dp/B07MW2RPJY), for brake light.
* LEDs for lights.
* 3D printer, soldering iron, hot glue, etc.

## requirements:

* SPI and hardware serial ONLY enabled on the Raspberry Pi,
* A good view of the sky for speedometer,
* Good connections while soldering to avoid a short-circuit.

## other:

I will upload the .STL's and wiring diagrams later.
I'm planning when v1 releases I will make a pcb so everything will easily connect, but that's the future.
I will post a youtube video on this project after v1.
