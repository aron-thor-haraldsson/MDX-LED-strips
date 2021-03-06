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
_base_colour = [0.0, 0.0, 0.0]



#host = 'localhost:7890'
host = '192.168.2.1:7890'
client = opc.Client(host)

if host.startswith('localhost'):
    os.system('readopcForStrands.exe')
    time.sleep(2)

# This part of the class has methods
# converting hls values (0.0 to 1.0 format)
# to rgb values (0 to 255).

def set_base_colour(colour, led_array):
    _base_colour = colour
    for q in range (len(led_array)):
        led_array[q].set_current(_base_colour)
def get_base_colour():
    return _base_colour
    
def hls1_to_rgb255(hls1):
    rgb1 = colorsys.hls_to_rgb(hls1[0], hls1[1], hls1[2])
    rgb255 = int(rgb1[0] * 255.0), int(rgb1[1] * 255.0), int(rgb1[2] * 255.0)
    return rgb255
        
def localize_leds(led_array, strip_number, strip_xyz):
    lower_limit = 60*(strip_number-1)
    upper_limit = 60*(strip_number)
    for i in range (lower_limit,upper_limit):
        led_array[i].set_strip_xyz(strip_xyz)
        led_array[i].calc_xyz(i-lower_limit)
def print_leds_info(led_array):
        for i in range (len(led_array)):
            print "Printing LED info:"
            print "Strip xyz: ", led_array[i].get_strip_xyz()
            print "Led   xyz: ", led_array[i].get_xyz()
            print "Current  : ", led_array[i].get_current()
            print "Target   : ", led_array[i].get_target()
            print

# Sends the current RGB values of all the LEDs to the fadecandy
def display_on_fadecandy(led_array):
    disp = []
    for i in range (len(led_array)):
        disp.append(hls1_to_rgb255(led_array[i].get_current()))
    client.put_pixels(disp)

def numberfy(var):
    var_type = type(var).__name__
    if var_type == "int" or var_type == "long" or var_type == "float":
        return var
    else:
        print "variable: ", var, " is not a valid number, it is of type '", var_type, "."
        return 0.0
def numberfys(vars):
    return [numberfy(vars[0]), numberfy(vars[1]), numberfy(vars[2])]

def calc_instant_steps(old, curr, targ, max_steps, is_h = False):
    output_array = []
    for j in range (max_steps):
        output_array.append(targ)
    return output_array
    
def calc_linear_steps(old, curr, targ, max_steps, is_h = False):
    output_array = []
    diff = targ-curr
    if diff < 0.0:
        sign = -1
    elif diff > 0.0:
        sign = 1
    else:
        sign = 0
    
    if sign == 0:
        for j in range (max_steps):
            output_array.append(targ)
    else:
        for j in range (max_steps):
            output_array.append(old + diff*j/float(max_steps))
    return output_array
    
    
def calc_cosine_steps(old, curr, targ, max_steps, is_h = False):
    output_array = []
    diff = targ-curr
    if diff < 0.0:
        sign = -1
    elif diff > 0.0:
        sign = 1
    else:
        sign = 0
    
    if sign == 0:
        for j in range (max_steps):
            output_array.append(targ)
    else:
        # A sine wave is used to describe the speed of change
        # where the 'x-axis' represents the time from start to end of change
        # and the 'y-axis' represents the speed at which it changes.
        # The integral of this yields a negative cosine wave that describes the distance of change
        # where the 'x-axis' represents the time from start to end of change
        # and the 'y-axis' represents the distance.

        # Using half sine wave ranging from 0 to 2*pi (period of 4*pi) to
        # describe the velocity at which the values
        # change towards the target value.
        # The integral of a half wave in that range
        # shows that the amplitude of the wave is
        # half the distance needed to travel.
        
        cos_amplitude = diff/2.0
        #
        for j in range (max_steps):
            output_array.append(old + cos_amplitude-cos_amplitude*math.cos(math.pi * j/float(max_steps)))
    return output_array
                   

class Triplets(object):
    # Default instance values in case they will not be set.
    def __init__(self):
        pass
        


    # This part of the class has methods
    # setting and getting various values for this object.
    def set_lower_limit(self, lower):
        self._lower_limit = lower
    def get_lower_limit(self):
        return self._lower_limit      
    def set_upper_limit(self, upper):
        self._upper_limit = upper
    def get_upper_limit(self):
        return self._upper_limit
    def set_old(self, old):
        self._old = old
    def get_old(self):
        return self._old

    def set_current(self, curr):
        self._current = [curr[0], curr[1], curr[2]]
    def get_current(self):
        return self._current

    def set_target(self, targ, step_type):
        self._target = targ
        if not self.is_same(self.get_current(), self.get_target()):
            self.set_steps_left(self.get_max_steps(), self.get_max_steps())
            self.calc_steps(step_type)
    def get_target(self):
        return self._target
    def is_same(self, curr, targ):
        bool0 = abs(targ[0]-curr[0]) < 0.01
        bool1 = abs(targ[1]-curr[1]) < 0.01
        bool2 = abs(targ[2]-curr[2]) < 0.01
        return bool0 and bool1 and bool2
        
    def set_max_steps(self, max):
        self._max_steps = max
    def get_max_steps(self):
        return self._max_steps
        
    def set_steps_left(self, left, total):
        self._steps_left = [left, total]
    def get_steps_left(self):
        return self._steps_left
        
    def set_mapped_steps(self, mapped):
        self.reset_mapped_steps
        self._mapped_steps = mapped
    def get_mapped_steps(self):
        return self._mapped_steps
    def reset_mapped_steps(self):
        self._mapped_steps = []
        

    def calc_steps(self, step_type):
        targ = self.get_target()
        curr = self.get_current()
        old = self.get_old()
        """
        print
        print "Values before calculation:"
        print "old: ", old
        print "curr: ", curr
        print "targ: ", targ
        old = curr
        print "updated old: ", old
        print
        """
        
        if step_type == "cosine":
            var0_shift = calc_cosine_steps(old[0], curr[0], targ[0], self.get_max_steps(), True)
            var1_shift = calc_cosine_steps(old[1], curr[1], targ[1], self.get_max_steps())
            var2_shift = calc_cosine_steps(old[2], curr[2], targ[2], self.get_max_steps())
            vars_shift = [var0_shift, var1_shift, var2_shift]
            self.set_mapped_steps(vars_shift)
        elif step_type == "linear":
            var0_shift = calc_linear_steps(old[0], curr[0], targ[0], self.get_max_steps(), True)
            var1_shift = calc_linear_steps(old[1], curr[1], targ[1], self.get_max_steps())
            var2_shift = calc_linear_steps(old[2], curr[2], targ[2], self.get_max_steps())
            vars_shift = [var0_shift, var1_shift, var2_shift]
            self.set_mapped_steps(vars_shift)
        elif step_type == "instant":
            var0_shift = calc_instant_steps(old[0], curr[0], targ[0], self.get_max_steps(), True)
            var1_shift = calc_instant_steps(old[1], curr[1], targ[1], self.get_max_steps())
            var2_shift = calc_instant_steps(old[2], curr[2], targ[2], self.get_max_steps())
            vars_shift = [var0_shift, var1_shift, var2_shift]
            self.set_mapped_steps(vars_shift)
            self.set_steps_left(2, self.get_steps_left()[1])
        """  
        print
        print "Mapped steps:"
        print self.get_mapped_steps()[0]
        print self.get_mapped_steps()[1]
        print self.get_mapped_steps()[2]
        print
        """
                
    def update(self):
        if self.get_steps_left()[1] > 0:
            if self.get_steps_left()[0] > 1:
                #print "updating..."
                curr_step = self.get_max_steps()-self.get_steps_left()[0]
                var0_next = self.get_mapped_steps()[0][curr_step]
                var1_next = self.get_mapped_steps()[1][curr_step]
                var2_next = self.get_mapped_steps()[2][curr_step]
                self.set_current([var0_next, var1_next, var2_next])
                self.set_steps_left(self.get_steps_left()[0]-1, self.get_steps_left()[1])
                
            elif self.get_steps_left()[0] == 1:
                self.set_steps_left(0, 0)
                self.set_current(self.get_target())
                self.set_old = [0, 0, 0]
                return -1
                
    def print_variables(self):
        print "Printing current variables:"
        print "old: ", self.get_old()
        print "current: ", self.get_current()
        print "target: ", self.get_target()
        print "max_steps: ", self.get_max_steps()
        print "steps_left: ", self.get_steps_left()
        print
        print

class Wall(Triplets):

    # Default instance values.
    def __init__(self, xyz = [0, 0, 0]):
        x = numberfy(xyz[0])
        y = numberfy(xyz[1])
        z = numberfy(xyz[2])
        self._lower_limit = 0
        self._upper_limit = 6000
        self._old = [x, y, z]
        self._current = [x, y, z]
        self._target = [x, y, z]
        self._steps_left = [0, 0]
        self._mapped_steps = []
        self._max_steps = 50
        self._vector = [0, 0, 0]
        self._proximity = 90000000
        self._normal_array = []
    
    def set_proximity(self, proximity):
        self._proximity = proximity
    def get_proximity(self):
        return self._proximity
        
    def set_vector(self):
        dx = self.get_target()[0]-self.get_old()[0]
        dy = self.get_target()[1]-self.get_old()[1]
        dz = self.get_target()[2]-self.get_old()[2]
        self._vector = [dx, dy, dz]
    def get_vector(self):
        return self._vector
    def reset_vector(self):
        self._vector = [0, 0, 0]
        
    def set_normal(self, led_array):
        
        self._normal_array = []
        for w in range (len(led_array)):
            mult_x = (self.get_vector()[0]*(led_array[w].get_xyz()[0]-self.get_current()[0]))
            mult_y = (self.get_vector()[1]*(led_array[w].get_xyz()[1]-self.get_current()[0]))
            mult_z = (self.get_vector()[2]*(led_array[w].get_xyz()[2]-self.get_current()[0]))
            value = (abs(mult_x + mult_y + mult_z))
            value = int(value/ 10000)
            if value < self.get_proximity():
                self._normal_array.append(w)
    def get_normal(self):
        return self._normal_array
    
    # This method is an overwrite of the parent method
    def set_target(self, targ, step_type):
        self._target = targ
        self.set_vector() #so that this line is included
        if not self.is_same(self.get_current(), self.get_target()):
            self.set_steps_left(self.get_max_steps(), self.get_max_steps())
            self.calc_steps(step_type)    
    
# This class handles all relevant information regarding
# one single LED.
class Led(Triplets):

    # Default instance values in case they will not be set.
    def __init__(self):
        self._strip_xyz = (0, 0, 0)
        self._xyz = (0, 0, 0)
        self._lower_limit = 0.0
        self._upper_limit = 1.0
        self._old = [0.0, 0.0, 0.0]
        self._current = [0.0, 0.0, 0.0]
        self._target = [0.0, 0.0, 0.0]
        self._steps_left = [0, 0]
        self._mapped_steps = []
        self._max_steps = 20
        
        
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

    # This overrides the method from the parent class
    def update(self):
        if self.get_steps_left()[1] > 0:
            if self.get_steps_left()[0] > 1:
                #print "updating..."
                curr_step = self.get_max_steps()-self.get_steps_left()[0]
                var0_next = self.get_mapped_steps()[0][curr_step]
                var1_next = self.get_mapped_steps()[1][curr_step]
                var2_next = self.get_mapped_steps()[2][curr_step]
                self.set_current([var0_next, var1_next, var2_next])
                self.set_steps_left(self.get_steps_left()[0]-1, self.get_steps_left()[1])
                return 1
                
            elif self.get_steps_left()[0] == 1:
                self.set_steps_left(0, 0)
                self.set_current(self.get_target())
                self.set_old = [0, 0, 0]
                return 0
        return -1