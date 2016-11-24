#!/usr/bin/env python

import colorsys

# This function converts HLS (Hue/Lightness/Saturation) color format to RGB (Red/Green/Blue).
# parameter: tuple or list of 3 floating point numbers (values ranging from 0 to 1)
# return: a tuple of 3 integers (values ranging from 0 to 255)
def hls1_to_rgb255(hls1):
    print hls1[0], hls1[1], hls1[2]
    rgb1 = colorsys.hls_to_rgb(hls1[0], hls1[1], hls1[2])
    rgb255 = (int(rgb1[0] * 255), int(rgb1[1] * 255), int(rgb1[2] * 255))
    return rgb255

