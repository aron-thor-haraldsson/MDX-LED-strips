#!/usr/bin/env python
# the following code is more or less copied directly from nick25's pixel project

import opc

led_colour=[(255,0,0)]*10

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