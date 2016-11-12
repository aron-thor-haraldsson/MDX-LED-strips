#!/usr/bin/env python

# The following code is more or less copied directly from nick25's pixel project


import opc
import rgb255
import color_names
"""
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

# For testing conversion function from 'rgb255' file
hls_value = (0.33, 0.5, 1)
rgb_value = rgb255.hls1_to_rgb255(hls_value)
print rgb_value

# For testing list of named colors from 'color_names' file
hls_value = color_names.black()
rgb_value = rgb255.hls1_to_rgb255(hls_value)
print rgb_value