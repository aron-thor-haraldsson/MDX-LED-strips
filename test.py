#!/usr/bin/env python

import time
import opc
import rgb255
import color_names
import color_adjust
import led_class as led
import os










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
"""
def update_leds():
    for i in range (len(leds)):
        leds[i] = update_led()
"""


leds = [led.Led() for i in range(0,360)]
#for i in range (len(leds)):
#    led.globalize()
    
led.localize_leds(leds, 1, (2000, 4000, 1000))
led.localize_leds(leds, 2, (2000, 4000, 2000))
led.localize_leds(leds, 3, (2000, 4000, 3000))
led.localize_leds(leds, 4, (2000, 2000, 1000))
led.localize_leds(leds, 5, (2000, 2000, 2000))
led.localize_leds(leds, 6, (2000, 2000, 3000))

print "hls convert: " , led.hls1_to_rgb255([0.33, 0.5, 1.0])
leds[1].set_current_hls([1.0, 0.5, 1])
leds[1].set_target_hls([0.1, 0.5, 1])
for n in range (60):
    leds[1].update_led()
    leds[1].print_led_variables()
    led.display_on_fadecandy(leds)
    time.sleep(0.1)
    
"""
for n in range(1000):
    print n
    for i in range (len(leds)):
        leds[i].set_current_hls([1.0 + n*0.003 + i*0.003, 0.5, 1.0])
        #print [1.0-n*0.01-i*0.01, 1.0-n*0.01-i*0.01, 1-n*0.01-i*0.01]
    led.display_on_fadecandy(leds)
    time.sleep(0.01)
  """      
    

#led.print_leds_info(leds)








