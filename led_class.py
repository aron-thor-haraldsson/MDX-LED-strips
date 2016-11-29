import math
import colorsys
import opc
import os
import time

def _deg_to_rad(deg):
    return (2*math.pi*deg)/360.0
def _rad_to_deg(rad):
    return 360.0*rad/(2*math.pi)
    
# 2000mm is the length of the strip from end to end, then use pythagoras a^2+b^2=c^2 to calculate the radius of the partial circle.
_circle_radius = math.sqrt(math.pow(2000, 2)/2) 
# The range of the shape of the partial circle is from 95 degrees to 175 degrees, where 0 degrees is on the positive x axis,
# Then divide by 60 to get the degree space between each LED.
_number_of_led_per_strip = 60.0
_degree_start = 90+5
_degree_stop = 180-5
_degree_per_light = (_degree_stop-_degree_start)/_number_of_led_per_strip
_rad_start = _deg_to_rad(_degree_start)
_rad_stop = _deg_to_rad(_degree_stop)
_rad_per_light = _deg_to_rad(_degree_per_light)

"""
def globalize():
    global hls1_to_rbg255
    def hls1_to_rbg255(h1, l1, s1):
        return rgb1_to_rgb255(hls1_to_rgb1(hls1))
"""

host = 'localhost:7890'
# host = '192.168.2.1:7890'
client = opc.Client(host)

if host.startswith('localhost'):
    os.system('readopcForStrands.exe')
    time.sleep(1)

# This part of the class has methods
# converting hls values (0.0 to 1.0 format)
# to rgb values (0 to 255).
    
def hls1_to_rgb255(hls1):
    return rgb1_to_rgb255(hls1_to_rgb1(hls1))
def hls1_to_rgb1(hls1):
    return colorsys.hls_to_rgb(hls1[0], hls1[1], hls1[2])
def rgb1_to_rgb255(rgb1):
    return (int(rgb1[0] * 255.0), int(rgb1[1] * 255.0), int(rgb1[2] * 255.0))
        
def localize_leds(led_array, strip_number, strip_xyz):
    lower_limit = 60*(strip_number-1)
    upper_limit = 60*(strip_number)
    for i in range (lower_limit,upper_limit):
        led_array[i].set_strip_xyz(strip_xyz)
        led_array[i].calc_xyz(i-lower_limit)
def print_leds_info(led_array):
        for i in range (len(led_array)):
            print "Strip xyz: ", led_array[i].get_strip_xyz()
            print "Led   xyz: ", led_array[i].get_xyz()
            print "Curr  hls: ", led_array[i].get_current_hls()
            print "Curr  rgb: ", led_array[i].get_current_rgb()
            print "Targ  hls: ", led_array[i].get_target_hls()
            print "Targ  rgb: ", led_array[i].get_target_rgb()
            print

# Sends the current RGB values of all the LEDs to the fadecandy
def display_on_fadecandy(led_array):
    disp = []
    for i in range (len(led_array)):
        disp.append(led_array[i].get_current_rgb())
        client.put_pixels(disp)



# This class handles all relevant information regarding
# one single LED.
class Led(object):

    # Default instance values in case they will not be set.
    def __init__(self):
        self._strip_xyz = (0, 0, 0)
        self._xyz = (0, 0, 0)
        self._current_hls = (0, 0, 0)
        self._current_rgb = (0, 0, 0)
        self._target_hls = (0, 0, 0)
        self._target_rgb = (0, 0, 0)
        
    # This part of the class has methods
    # that handle the start position of the strip
    # the LED belongs to.
    def set_strip_xyz(self, strip_xyz):
        self._strip_xyz = strip_xyz
    def get_strip_xyz(self):
        return self._strip_xyz

        
    # This part of the class has methods
    # setting and getting the x,y,z coordinates of this LED.
    # For these methods to work properly, the above 'start position'
    # methods need to be set first.
    def calc_xyz(self, increment):
        x = self.get_strip_xyz()[0] + _circle_radius*math.cos(increment*_rad_per_light+_rad_start)
        y = self.get_strip_xyz()[1] + _circle_radius*math.sin(increment*_rad_per_light+_rad_start)
        z = self.get_strip_xyz()[2]
        self._xyz = [x, y, z]
    def set_xyz(self, xyz):
        self._xyz(xyz)
    def get_xyz(self):
        return self._xyz 


    # This part of the class has methods
    # setting and getting current HLS and RGB values for this LED.
    def set_current_hls(self, curr_hls):
        self._current_hls = curr_hls
        self.set_current_rgb()
    def get_current_hls(self):
        return (self._current_hls)
    def set_current_rgb(self):
        self._current_rgb = hls1_to_rgb255(self.get_current_hls())
    def get_current_rgb(self):
        return (self._current_rgb)

    # This part of the class has methods
    # setting and getting target HLS and RGB values for this LED.
    def set_target_hls(self, targ_hls):
        self._target_hls = targ_hls
        self.set_target_rgb()
    def get_target_hls(self):
        return (self._target_hls)
    def set_target_rgb(self):
        self._target_rgb = hls1_to_rgb255(self.get_target_hls())
    def get_target_rgb(self):
        return (self._target_rgb)