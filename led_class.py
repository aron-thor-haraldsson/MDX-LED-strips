import math

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


# This class handles all relevant information regarding
# one single LED.
class Led(object):

    # Default instance values in case they will not be set.
    def __init__(self):
        self.set_start_pos(self, 0, 0, 0)
        self.set_xyz(self, 0, 0, 0)
        self.set_rgb(self, 0, 0, 0)
        
    # This part of the class has methods
    # that handle the start position of the strip
    # the LED belongs to.
    def set_start_pos(self, start_x, start_y, start_z):
        self.set_start_x(start_x)
        self.set_start_y(start_y)
        self.set_start_z(start_z)
    def get_start_pos():
        return self.start_pos      
    def set_start_x(self, start_x):
        self.start_x = start_x
    def get_start_x(self):
        return self.start_x  
    def set_start_y(self, start_y):
        self.start_y = start_y
    def get_start_y(self):
        return self.start_y
    def set_start_z(self, start_z):
        self.start_z = start_z
    def get_start_z(self):
        return self.start_z

        
    # This part of the class has methods
    # setting and getting the x,y,z coordinates of this LED.
    # For these methods to work properly, the above 'start position'
    # methods need to be set first.
    def calc_xyz(self, increment):
        self.set_x(self.get_start_x() + _circle_radius*math.cos(increment*_rad_per_light+_rad_start))
        self.set_y(self.get_start_y() + _circle_radius*math.sin(increment*_rad_per_light+_rad_start))
        self.set_z(self.get_start_z())
    def set_xyz(self, x, y, z):
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
    def get_xyz(self):
        return self.get_x(), self.get_y(), self.get_z() 
    def set_x(self, x):
        self.x = x
    def get_x(self):
        return self.x
    def set_y(self, y):
        self.y = y
    def get_y(self):
        return self.y
    def set_z(self, z):
        self.z = z
    def get_z(self):
        return self.z


    # This part of the class has methods
    # setting and getting color information for this LED.
    def set_rgb(self, r, g, b):
        self.set_r(r)
        self.set_g(g)
        self.set_b(b)
    def get_rgb(self):
        return get_r(), get_g(), get_b()
    def set_r(self, r):
        self.r = r
    def get_r():
        return self.r
    def set_g(self, g):
        self.g = g
    def get_g(self):
        return self.g
    def set_b(self, b):
        self.b = b
    def get_r(self):
        return self.b