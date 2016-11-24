import math
import numpy as np

"""

To determine the position and facing a strip of LEDs has,
These six equations describe the shape of the graph they form.
This represents one unit of 'length' and the equation can be scaled up/down
to fit the actual size of the LED strips by changing the value of 'a'.

y=(e^a)*(ln(x)+2)       {y>e}{0>x>2e^a}
y=(e^a)*(ln(-x)+2)      {y>0}{-2e^a>x>0}
y=(e^a)*(ln(x^(-1)+2)   {y>0}{0>x>2e^a}
y=(e^a)*(ln(-x^(-1))+2) {y>0}{-2e^a>x>0}
x=(e^a)*(ln(y)+2)       {x>0}{0>y>2e^a}
x=(e^a)*(ln(-y)+2)      {x>0}{-2e^a>y>0}
x=(e^a)*(ln(y^(-1))+2)  {x>0}{0>y>2e^a}
x=(e^a)*(ln(-y^(-1))+2) {x>0}{-2e^a>y>0}
"""

# 2000mm is the length of the strip from end to end, then use pythagoras a^2+b^2=c^2 to calculate the radius of the partial circle.
circle_rad = math.sqrt(math.pow(2000, 2)/2) 
# The range of the shape of the partial circle is from 95 degrees to 175 degrees, where 0 degrees is on the positive x axis,
# Then divide by 60 to get the degree space between each LED.
degree_per_light = (175-95)/60.0


result_array = np.empty((0, 100))

for line in data_array:
    result = do_stuff(line)
    result_array = np.append(result_array, [result], axis=0)
    
print x
"""
led_xyz=[(0,0,0,0,0,0,0,0)*60, (1,0,0,0,0,0,0,0), (2,0,0,0,0,0,0,0), (3,0,0,0,0,0,0,0), (4,0,0,0,0,0,0,0), (5,0,0,0,0,0,0,0)]

for item in enumerate(led_colour):
    print item
    x, y, z = item[1]
    x = 0
    y = 255
    z = 255
    #add create new one
    new_xyz =(x,y,z)
    led_xyz[item[0]]= new_colour
    
    """