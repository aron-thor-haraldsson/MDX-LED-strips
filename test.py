#!/usr/bin/env python

import time
import opc
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
wall = led.Wall()
leds = [led.Led() for i in range(0,360)]

def reset_all():
    wall = led.Wall()
    leds = [led.Led() for i in range(0,360)]

    led.localize_leds(leds, 1, (2000, 4000, 1000))
    led.localize_leds(leds, 2, (2000, 4000, 2000))
    led.localize_leds(leds, 3, (2000, 4000, 3000))
    led.localize_leds(leds, 4, (2000, 2000, 1000))
    led.localize_leds(leds, 5, (2000, 2000, 2000))
    led.localize_leds(leds, 6, (2000, 2000, 3000))

def update_leds():
    for q in range (len(leds)):
        if leds[q].update() == 0:
            leds[q].set_current(leds[q].get_target())
            leds[q].set_target(led.get_base_colour(), "linear")
def prepare_wall_movement(direction, speed):
    
    if direction == "diagonal":
        wall.set_current([0, 0, 0])
        wall.set_proximity(120)
        wall.set_target([6000, 6000, 6000], speed)
    elif direction == "left_to_right":
        wall.set_current([0, 0, 0])
        wall.set_proximity(39)
        wall.set_target([6000, 0, 0], speed)
    elif direction == "down_to_up":
        wall.set_current([0, 0, 0])
        wall.set_proximity(39)
        wall.set_target([0, 6000, 0], speed)
    else:
        print "invalid wall movement"
        
reset_all()



def perform_sweep(direction, speed):
    led.set_base_colour([1.0, 0.0, 1.0], leds)
    prepare_wall_movement(direction, speed)
    for n in range (55):
        wall.update()
        wall.set_normal(leds)
        for m in range (len(wall.get_normal())):
            normal = wall.get_normal()[m]
            leds[normal].set_target([1.0, 0.5, 1.0], "linear")
        update_leds()
        
        led.display_on_fadecandy(leds)
        time.sleep(0.1)
    reset_all()


perform_sweep("diagonal", "linear")
perform_sweep("diagonal", "linear")

"""
for n in range(1000):
    print n
    for i in range (len(leds)):
        leds[i].set_current_hls([1.0 + n*0.003 + i*0.003, 0.5, 1.0])
        #print [1.0-n*0.01-i*0.01, 1.0-n*0.01-i*0.01, 1-n*0.01-i*0.01]
    led.display_on_fadecandy(leds)
    time.sleep(0.01)
"""



