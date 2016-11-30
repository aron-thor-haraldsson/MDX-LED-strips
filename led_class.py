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
#host = '192.168.2.1:7890'
client = opc.Client(host)

if host.startswith('localhost'):
    os.system('readopcForStrands.exe')
    time.sleep(2)

# This part of the class has methods
# converting hls values (0.0 to 1.0 format)
# to rgb values (0 to 255).
    
def hls1_to_rgb255(hls1):
    rgb1 = colorsys.hls_to_rgb(hls1[0], hls1[1], hls1[2])
    rgb255 = int(rgb1[0] * 255.0), int(rgb1[1] * 255.0), int(rgb1[2] * 255.0)
    return rgb255
    
def constrain_h(h):
    if h < 0.0:
        while h < 0.0:
            h = h + 1.0
    return h
def constrain_ls(ls):
    if ls > 1.0:
        ls = 1.0
    elif ls < 0.0:
        ls = 0.0
    return ls
        
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
        disp.append(hls1_to_rgb255(led_array[i].get_current_hls()))
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
        self._old_hls = (0, 0, 0)
        self._fade_steps_left = (0, 0)
        self._mapped_fade_steps = []
        self._max_fade_steps = 50
        
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
        self._current_hls = [constrain_h(curr_hls[0]), constrain_ls(curr_hls[1]), constrain_ls(curr_hls[2])]
    def get_current_hls(self):
        return (self._current_hls)

    # This part of the class has methods
    # setting and getting target HLS and RGB values for this LED.
    def set_target_hls(self, targ_hls):
        self._target_hls = [constrain_h(targ_hls[0]), constrain_ls(targ_hls[1]), constrain_ls(targ_hls[2])]
        if self.get_target_hls() != self.get_current_hls():
            self._fade_steps_left = (self._max_fade_steps, self._max_fade_steps)
            self.calc_fade()
    def get_target_hls(self):
        return (self._target_hls)
        

    def calc_fade(self):
        targ_hls = self.get_target_hls()
        curr_hls = self.get_current_hls()
        self._old_hls = curr_hls
        old_hls = self._old_hls
        print
        print "Color before fade calculation:"
        print "targ_hls: ", targ_hls
        print "curr_hls: ", curr_hls
        print "_old_hls: ", self._old_hls
        print
        
        h_shift = self.calc_fade_value(old_hls[0], curr_hls[0], targ_hls[0], True)
        l_shift = self.calc_fade_value(old_hls[1], curr_hls[1], targ_hls[1])
        s_shift = self.calc_fade_value(old_hls[2], curr_hls[2], targ_hls[2])
        hls_shift = [h_shift, l_shift, s_shift]
        self._mapped_fade_steps = hls_shift
        print
        print "Mapped fade steps:"
        print self._mapped_fade_steps[0]
        print self._mapped_fade_steps[1]
        print self._mapped_fade_steps[2]
        print
        
    def calc_fade_value(self, old, curr, targ, is_h = False):
        output_array = []
        diff = targ-curr
        if diff < 0.0:
            sign = -1
        elif diff > 0.0:
            sign = 1
        else:
            sign = 0
        
        if sign == 0:
            for i in range (self._max_fade_steps):
                output_array.append(targ)
        else:
            # While fading, a sine wave is used to describe the speed of color change
            # where the 'x-axis' represents the time from start to end of change
            # and the 'y-axis' represents the speed at which it changes.
            # The integral of this yields a negative cosine wave that describes the distance of color change
            # where the 'x-axis' represents the time from start to end of change
            # and the 'y-axis' represents the distance it has changed.
            # For this purpose, I have used half waves (ranging from 0 to 2*pi).
            # Using half sine wave ranging from 0 to 2*pi (period of 4*pi) to
            # describe the velocity at which the color values
            # change towards targat value.
            # The integral of a half wave in that range
            # shows that the amplitude of the wave is
            # half the distance needed to travel.
            
            cos_amplitude = diff/2.0
            #
            for i in range (self._max_fade_steps):
                output_array.append(old + cos_amplitude-cos_amplitude*math.cos(math.pi * i/float(self._max_fade_steps)))
        return output_array
                
    def update_led(self):
        if self._fade_steps_left[1] > 0:
            if self._fade_steps_left[0] > 0:
                print "updating led..."
                curr_step = self._max_fade_steps-self._fade_steps_left[0]
                h_next = self._mapped_fade_steps[0][curr_step]
                l_next = self._mapped_fade_steps[1][curr_step]
                s_next = self._mapped_fade_steps[2][curr_step]
                print "update current_hls: ",[h_next, l_next, s_next]
                self.set_current_hls([h_next, l_next, s_next])
                self._fade_steps_left = [self._fade_steps_left[0]-1, self._fade_steps_left[1]]
                
            elif self._fade_steps_left[0] == 0:
                self._fade_steps_left = (0, 0)
                self.set_current_hls(self.get_target_hls())
                self._old_hls = (0, 0, 0)
                self._mapped_fade_steps = []
                
        
    def print_led_variables(self):
        print
        print
        print "Printing current led variables:"
        print "_strip_xyz: ", self._strip_xyz
        print "_xyz: ", self._xyz
        print "_current_hls: ", self.get_current_hls()
        print "_target_hls: ", self.get_target_hls()
        print "_old_hls: ", self._old_hls
        print "_fade_steps_left: ", self._fade_steps_left
        print "_max_fade_steps: ", self._max_fade_steps
        print
        print