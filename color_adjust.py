# This file contains various HLS/RGB conversion functions relying on 'colorsys'

import colorsys

step_increment = 0.01
jump_increment = 0.25

def hls_adjust(hls_tuple, variable, operation, direction):
    h = hls_tuple[0]
    l = hls_tuple[1]
    s = hls_tuple[2]
    if variable == "h":
        h = adjust_color_property(h, operation, direction)
    elif variable == "l":
        l = adjust_color_property(l, operation, direction)
    elif variable == "s":
        s = adjust_color_property(s, operation, direction)
    else:
        print "Failed during 'hls_adjust' function: unknown variable.\n"
    return (h, l, s)

# parameters: the original value, what do do with it and wether the change is positive or negative
def adjust_color_property(old_value, operation, direction):
    if operation == "step":
        new_value = step_color_property(old_value, direction)
    elif operation == "jump":
        new_value = jump_color_property(old_value, direction)
    else:
        print "Failed during 'adjust_color_property' function: unknown operation.\n"
        new_value = old_value
    return new_value

def step_color_property(old_value, direction):
    if direction == "up":
        new_value = old_value + step_increment
    elif direction == "down":
        new_value = old_value - step_increment
    else:
        print "Failed during 'step_color_property' function: unknown direction."
        new_value = old_value
    return new_value
		
def jump_color_property(old_value, direction):
    if direction == "up":
        if old_value < 0.00:
            new_value = 0.00
        elif old_value < jump_increment:
            new_value = jump_increment
        elif old_value < jump_increment*2:
            new_value = jump_increment*2
        elif old_value < jump_increment*3:
            new_value = jump_increment*3
        elif old_value < jump_increment*4:
            new_value = jump_increment*4
        elif old_value == jump_increment*5:
            new_value = jump_increment*5
        else:
            print "Failed during 'jump_color_property' function: invalid input value."
            new_value = old_value
        return new_value
    elif direction == "down":
        if old_value < 0.00:
            new_value = -jump_increment
        elif old_value < jump_increment:
            new_value = 0.00
        elif old_value < jump_increment*2:
            new_value = jump_increment
        elif old_value < jump_increment*3:
            new_value = jump_increment*2
        elif old_value < jump_increment*4:
            new_value = jump_increment*3
        elif old_value < jump_increment*4:
            new_value = jump_increment*3
        elif old_value < jump_increment*5:
            new_value = jump_increment*4
        else:
            print "Failed during 'jump_color_property' function: invalid input value."
            new_value = old_value
        return new_value