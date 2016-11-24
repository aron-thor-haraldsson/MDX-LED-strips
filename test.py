#!/usr/bin/env python

import time
import opc
import rgb255
import color_names
import color_adjust
import led_class as led

"""
# The following code is more or less copied directly from nick25's pixel project
hls_to_rgb=(1, 0.5, 1)
led_colour=[(255/255,0/255,0/255)]*10

client = opc.Client('localhost:7890')
print enumerate(led_colour)
for item in enumerate(led_colour):
    print item
    if item[0]==1:
        #need to get values out of tuple
        r, g, b = item[1]
        r = 0
        g = 255
        b = 255
        #add create new one
        new_colour =(r,g,b)
        led_colour[item[0]]= new_colour


client.put_pixels(led_colour)
print led_colour
"""


"""
# For testing conversion function from 'rgb255' file
hls_value = (0.33, 0.5, 1.0)
rgb_value = rgb255.hls1_to_rgb255(hls_value)
print "Testing 'rgb255':"
print rgb_value
print

time.sleep(1)

"""

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
leds = [led.Led() for i in range(0,60)]

for i in range (0,60):
    print i
    leds[i].set_start_pos(2000, 4000, 3000)
    leds[i].calc_xyz(i)
    
    print leds[i].get_xyz()

"""
for i in range(0, 59):
    l(i) = led.Led(i)
for i in range(0, 59):
    l(i) = led.get_number(i)
"""