#!/usr/bin/env python

import time
import opc
import color_names
import color_adjust
import led_class as led
import os


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
       


leds = [led.Led() for i in range(0,360)]
wall = led.Wall()
 
led.localize_leds(leds, 1, (2000, 4000, 1000))
led.localize_leds(leds, 2, (2000, 4000, 2000))
led.localize_leds(leds, 3, (2000, 4000, 3000))
led.localize_leds(leds, 4, (2000, 2000, 1000))
led.localize_leds(leds, 5, (2000, 2000, 2000))
led.localize_leds(leds, 6, (2000, 2000, 3000))

led.set_base_colour([1.0, 0.0, 1.0], leds)

def perform_sweep(direction, speed, colour = color_names.red()):
    print color_names.red()
    prepare_wall_movement(direction, speed)
    for n in range (55):
        wall.update()
        wall.set_normal(leds)
        for m in range (len(wall.get_normal())):
            normal = wall.get_normal()[m]
            leds[normal].set_target(colour, "linear")
        update_leds()
        
        led.display_on_fadecandy(leds)
        time.sleep(0.1)
        
def perform_fade():
    for n in range(1000):
        print n
        for i in range (len(leds)):
            leds[i].set_current([1.0 + n*0.003 + i*0.003, 0.5, 1.0])
            #print [1.0-n*0.01-i*0.01, 1.0-n*0.01-i*0.01, 1-n*0.01-i*0.01]
        led.display_on_fadecandy(leds)
        time.sleep(0.01)
        
perform_sweep("diagonal", "linear")
time.sleep(1)
perform_sweep("diagonal", "cosine")
time.sleep(1)
perform_sweep("left_to_right", "linear")
time.sleep(1)
perform_sweep("left_to_right", "cosine")
time.sleep(1)
perform_sweep("down_to_up", "linear")
time.sleep(1)
perform_sweep("down_to_up", "cosine")
time.sleep(1)
perform_fade()
time.sleep(1)








