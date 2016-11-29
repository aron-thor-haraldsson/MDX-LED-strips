#!/usr/bin/env python

import time
import opc
import rgb255
import color_names
import color_adjust
import led_class as led
import os





# Sends the current RGB values of all the LEDs to the fadecandy
def display_on_fadecandy():
    disp = []
    for i in range (len(leds)):
        disp.append(leds[i].get_rgb())
        client.put_pixels(disp)




"""
# For testing list of named colors from 'color_names' file
hls_value = color_names.white()
rgb_value = rgb255.hls1_to_rgb255(hls_value)
print "Testing 'color_names':"
print rgb_value
print

time.sleep(1)
"""

"""

# For testing functions from 'color_adjust' file
hls_value = (0.0, 0.5, 1.0)
print "Testing 'color_adjust':"
print rgb255.hls1_to_rgb255(hls_value)
print
for x in range(0, 100):
    time.sleep(2)   
    hls_value = color_adjust.hls_adjust(hls_value, "h", "jump", "down")
    print rgb255.hls1_to_rgb255(hls_value)
    print
    
"""

"""

led = [2, 1, 1, 1]

for item in range(len(led)):
    print led[item]
print (led)

"""

host = 'localhost:7890'
# host = '192.168.2.1:7890'
client = opc.Client(host)




if host.startswith('localhost'):
    os.system('readopcForStrands.exe')
    time.sleep(1)

leds = [led.Led() for i in range(0,360)]
#for i in range (len(leds)):
#    led.globalize()
    
led.localize_leds(leds, 1, 2000, 4000, 1000)
led.localize_leds(leds, 2, 2000, 4000, 2000)
led.localize_leds(leds, 3, 2000, 4000, 3000)
led.localize_leds(leds, 4, 2000, 2000, 1000)
led.localize_leds(leds, 5, 2000, 2000, 2000)
led.localize_leds(leds, 6, 2000, 2000, 3000)

leds[1].set_hls(1.0, 0.5, 1.0)
print leds[1].get_hls()
print leds[1].get_rgb()


    

for i in range (len(leds)):
    leds[i].set_hls(1-i*0.001, 1-i*0.001, 1-i*0.001)
    
display_on_fadecandy()






