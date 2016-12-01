# This file contains a long list of named colors and their HLS values.
# The list was acquired from http://www.standardista.com/css3/cssnamed-hsl-and-rgb-colors/ and modified



# A long list of functions that return the private color values of named colors.
def aliceblue(): return __aliceblue
def antiquewhite(): return __antiquewhite
def aqua(): return __aqua    #same as cyan
def aquamarine(): return __aquamarine
def azure(): return __azure
def beige(): return __beige
def bisque(): return __bisque
def black(): return __black
def blanchedalmond(): return __blanchedalmond
def blue(): return __blue
def blueviolet(): return __blueviolet
def brown(): return __brown
def burlywood(): return __burlywood
def cadetblue(): return __cadetblue
def chartreuse(): return __chartreuse
def chocolate(): return __chocolate
def coral(): return __coral
def cornflowerblue(): return __cornflowerblue
def cornsilk(): return __cornsilk
def crimson(): return __crimson
def cyan(): return __cyan    #same as aqua
def darkblue(): return __darkblue
def darkcyan(): return __darkcyan
def darkgoldenrod(): return __darkgoldenrod
def darkgray(): return __darkgray
def darkgreen(): return __darkgreen
def darkkhaki(): return __darkkhaki
def darkmagenta(): return __darkmagenta
def darkolivegreen(): return __darkolivegreen
def darkorange(): return __darkorange
def darkorchid(): return __darkorchid
def darkred(): return __darkred
def darksalmon(): return __darksalmon
def darkseagreen(): return __darkseagreen
def darkslateblue(): return __darkslateblue
def darkslategray(): return __darkslategray    #same as darkslategrey
def darkslategrey(): return __darkslategray    #same as darkslategray
def darkturquoise(): return __darkturquoise
def darkviolet(): return __darkviolet
def deeppink(): return __deeppink
def deepskyblue(): return __deepskyblue
def dimgray(): return __dimgray    #same as dimgrey
def dimgrey(): return __dimgray    #same as dimgray
def dodgerblue(): return __dodgerblue
def firebrick(): return __firebrick
def floralwhite(): return __floralwhite
def forestgreen(): return __forestgreen
def fuchsia(): return __fuchsia    #same as magenta
def gainsboro(): return __gainsboro
def ghostwhite(): return __ghostwhite
def gold(): return __gold
def goldenrod(): return __goldenrod 
def gray(): return __gray
def green(): return __green
def greenyellow(): __greenyellow
def honeydew(): return __honeydew
def hotpink(): return __hotpink
def indianred(): return __indianred
def indigo(): return __indigo
def ivory(): return __ivory
def khaki(): return __khaki
def lavender(): return __lavender
def lavenderblush(): return __lavenderblush
def lawngreen(): return __lawngreen
def lemonchiffon(): return __lemonchiffon
def lightblue(): return __lightblue
def lightcoral(): return __lightcoral
def lightcyan(): return __lightcyan
def lightgoldenrodyellow(): return __lightgoldenrodyellow
def lightgray(): return __lightgray    #same as lightgrey
def lightgrey(): return __lightgray    #same as lightgray
def lightgreen(): return __lightgreen
def lightpink(): return __lightpink
def lightsalmon(): return __lightsalmon
def lightseagreen(): return __lightseagreen
def lightskyblue(): return __lightskyblue
def lightslategray(): return __lightslategray    #same as lightslategrey
def lightslategrey(): return __lightslategray    #same as lightslategray
def lightsteelblue(): return __lightsteelblue
def lightyellow(): return __lightyellow
def lime(): return __lime
def limegreen(): return __limegreen 
def linen(): return __linen
def maroon(): return __maroon
def mediumaquamarine(): return __mediumaquamarine
def mediumblue(): return __mediumblue
def mediumorchid(): return __mediumorchid
def mediumpurple(): return __mediumpurple
def mediumseagreen(): return __mediumseagreen
def mediumslateblue(): return __mediumslateblue
def mediumspringgreen(): return __mediumspringgreen
def mediumturquoise(): return __mediumturquoise
def mediumvioletred(): return __mediumvioletred
def midnightblue(): return __midnightblue
def mintcream(): return __mintcream
def mistyrose(): return __mistyrose
def moccasin(): return __moccasin
def navajowhite(): return __navajowhite
def navy(): return __navy
def oldlace(): return __oldlace
def olive(): return __olive
def olivedrab(): return __olivedrab
def orange(): return __orange
def orangered(): return __orangered
def orchid(): return __orchid
def palegoldenrod(): return __palegoldenrod
def palegreen(): return __palegreen
def paleturquoise(): return __paleturquoise
def palevioletred(): return __palevioletred
def papayawhip(): return __papayawhip
def peachpuff(): return __peachpuff
def peru(): return __peru
def pink(): return __pink
def plum(): return __plum
def powderblue(): return __powderblue
def purple(): return __purple
def red(): return __red
def rosybrown(): return __rosybrown
def royalblue(): return __royalblue
def saddlebrown(): return __saddlebrown
def salmon(): return __salmon
def sandybrown(): return __sandybrown
def seagreen(): return __seagreen
def seashell(): return __seashell
def sienna(): return __sienna
def silver(): return __silver
def skyblue(): return __skyblue
def slateblue(): return __slateblue
def slategray(): return __slategray    #same as slategrey
def slategrey(): return __slategrey    #same as slategray
def snow(): return __snow 
def springgreen(): return __springgreen
def steelblue(): return __steelblue
def tan(): return __tan
def teal(): return __teal
def thistle(): return __thistle
def tomato(): return __tomato
def turquoise(): return __turquoise
def violet(): return __violet
def wheat(): return __wheat
def white(): return __white
def whitesmoke(): return __whitesmoke
def yellow(): return __yellow
def yellowgreen(): return __yellowgreen

# This function changes format of HLS values.
# parameter: a tuple of three integers, valued 0 to 360, 0 to 100 and 0 to 100.
# return: a tuple of three floating point numbers valued between 0.0 and 1.0.
def hls360_to_hls1(h360, l100, s100):
    h1 = 1 - h360 / 360.0
    l1 = l100 / 200.0
    s1 = s100 / 50.0
    return (h1, l1, s1)
    
# A long list of private variables containing tuples representing the HLS values of named colors.
# The values are put through a function to convert them to a format that is more usable.
__aliceblue = hls360_to_hls1(208, 97, 100)
__antiquewhite = hls360_to_hls1(34, 91, 78)
__aqua = hls360_to_hls1(180, 50, 100)    #same as cyan
__aquamarine = hls360_to_hls1(160, 75, 100)
__azure = hls360_to_hls1(180, 97, 100)
__beige = hls360_to_hls1(60, 91, 56)
__bisque = hls360_to_hls1(33, 88, 100)
__black = hls360_to_hls1(0, 0, 0)
__blanchedalmond = hls360_to_hls1(36, 90, 100)
__blue = hls360_to_hls1(240, 50, 100)
__blueviolet = hls360_to_hls1(271, 53, 76)
__brown = hls360_to_hls1(0, 41, 59)
__burlywood = hls360_to_hls1(34, 70, 57)
__cadetblue = hls360_to_hls1(182, 50, 25)
__chartreuse = hls360_to_hls1(90, 50, 100)
__chocolate = hls360_to_hls1(25, 47, 75)
__coral = hls360_to_hls1(16, 66, 100)
__cornflowerblue = hls360_to_hls1(219, 79, 66)
__cornsilk = hls360_to_hls1(48, 100, 93)
__crimson = hls360_to_hls1(348, 83, 58)
__cyan = hls360_to_hls1(180, 100, 50)    #same as aqua
__darkblue = hls360_to_hls1(240, 100, 27);
__darkcyan = hls360_to_hls1(180, 100, 27)
__darkgoldenrod = hls360_to_hls1(43, 89, 38)
__darkgray = hls360_to_hls1(0, 0, 66)
__darkgreen = hls360_to_hls1(120, 100, 20)
__darkkhaki = hls360_to_hls1(56, 38, 58)
__darkmagenta = hls360_to_hls1(300, 100, 27)
__darkolivegreen = hls360_to_hls1(82, 39, 30)
__darkorange = hls360_to_hls1(33, 100, 50)
__darkorchid = hls360_to_hls1(280, 61, 50)
__darkred = hls360_to_hls1(0, 100, 27)
__darksalmon = hls360_to_hls1(15, 72, 70)
__darkseagreen = hls360_to_hls1(120, 25, 65)
__darkslateblue = hls360_to_hls1(248, 39, 39)
__darkslategray = hls360_to_hls1(180, 25, 25)    #same as darkslategrey
__darkslategrey = hls360_to_hls1(180, 25, 25)    #same as darkslategray
__darkturquoise = hls360_to_hls1(181, 100, 41)
__darkviolet = hls360_to_hls1(282, 100, 41)
__deeppink = hls360_to_hls1(328, 100, 54)
__deepskyblue = hls360_to_hls1(195, 100, 50)
__dimgray = hls360_to_hls1(0, 0, 41)    #same as dimgrey
__dimgrey = hls360_to_hls1(0, 0, 41)    #same as dimgray
__dodgerblue = hls360_to_hls1(210, 100, 56)
__firebrick = hls360_to_hls1(0, 68, 42)
__floralwhite = hls360_to_hls1(40, 100, 97)
__forestgreen = hls360_to_hls1(120, 61, 34)
__fuchsia = hls360_to_hls1(300, 100, 50)    #same as magenta
__gainsboro = hls360_to_hls1(0, 0, 86)
__ghostwhite = hls360_to_hls1(240, 100, 99)
__gold = hls360_to_hls1(51, 100, 50)
__goldenrod = hls360_to_hls1(43, 74, 49)
__gray = hls360_to_hls1(0, 0, 50)    #same as grey
__grey = hls360_to_hls1(0, 0, 50)    #same as gray
__green = hls360_to_hls1(120, 100, 25)
__greenyellow = hls360_to_hls1(84, 100, 59)
__honeydew = hls360_to_hls1(120, 100, 97)
__hotpink = hls360_to_hls1(330, 100, 71)
__indianred = hls360_to_hls1(0, 53, 58)
__indigo = hls360_to_hls1(275, 100, 25)
__ivory = hls360_to_hls1(60, 100, 97)
__khaki = hls360_to_hls1(54, 77, 75)
__lavender = hls360_to_hls1(240, 67, 94)
__lavenderblush = hls360_to_hls1(340, 100, 97)
__lawngreen = hls360_to_hls1(90, 100, 49)
__lemonchiffon = hls360_to_hls1(54, 100, 90)
__lightblue = hls360_to_hls1(195, 53, 79)
__lightcoral = hls360_to_hls1(0, 79, 72)
__lightcyan = hls360_to_hls1(180, 100, 94)
__lightgoldenrodyellow = hls360_to_hls1(60, 80, 90)
__lightgray = hls360_to_hls1(0, 0, 83)    #same as lightgrey
__lightgrey = hls360_to_hls1(0, 0, 83)    #same as lightgray
__lightgreen = hls360_to_hls1(120, 73, 75)
__lightpink = hls360_to_hls1(351, 100, 86)
__lightsalmon = hls360_to_hls1(17, 100, 74)
__lightseagreen = hls360_to_hls1(177, 70, 41)
__lightskyblue = hls360_to_hls1(203, 92, 75)
__lightslategray = hls360_to_hls1(210, 14, 53)    #same as lightslategrey
__lightslategrey = hls360_to_hls1(210, 14, 53)    #same as lightslategray
__lightsteelblue = hls360_to_hls1(214, 41, 78)
__lightyellow = hls360_to_hls1(60, 100, 94)
__lime = hls360_to_hls1(120, 100, 50)
__limegreen = hls360_to_hls1(120, 61, 50)
__linen = hls360_to_hls1(30, 67, 94)
__maroon = hls360_to_hls1(0, 100, 25)
__mediumaquamarine = hls360_to_hls1(160, 51, 60)
__mediumblue = hls360_to_hls1(240, 100, 40)
__mediumorchid = hls360_to_hls1(288, 59, 58)
__mediumpurple = hls360_to_hls1(260, 60, 65)
__mediumseagreen = hls360_to_hls1(147, 50, 47)
__mediumslateblue = hls360_to_hls1(249, 80, 67)
__mediumspringgreen = hls360_to_hls1(157, 100, 49)
__mediumturquoise = hls360_to_hls1(178, 60, 55)
__mediumvioletred = hls360_to_hls1(322, 81, 43)
__midnightblue = hls360_to_hls1(240, 64, 27)
__mintcream = hls360_to_hls1(150, 100, 98)
__mistyrose = hls360_to_hls1(6, 100, 94)
__moccasin = hls360_to_hls1(38, 100, 85)
__navajowhite = hls360_to_hls1(36, 100, 84)
__navy = hls360_to_hls1(240, 100, 25)
__oldlace = hls360_to_hls1(39, 85, 95)
__olive = hls360_to_hls1(60, 100, 25)
__olivedrab = hls360_to_hls1(80, 60, 35)
__orange = hls360_to_hls1(39, 100, 50)
__orangered = hls360_to_hls1(16, 100, 50)
__orchid = hls360_to_hls1(302, 59, 65)
__palegoldenrod = hls360_to_hls1(55, 67, 80)
__palegreen = hls360_to_hls1(120, 93, 79)
__paleturquoise = hls360_to_hls1(180, 65, 81)
__palevioletred = hls360_to_hls1(340, 60, 65)
__papayawhip = hls360_to_hls1(37, 100, 92)
__peachpuff = hls360_to_hls1(28, 100, 86)
__peru = hls360_to_hls1(30, 59, 53)
__pink = hls360_to_hls1(350, 100, 88)
__plum = hls360_to_hls1(300, 47, 75)
__powderblue = hls360_to_hls1(187, 52, 80)
__purple = hls360_to_hls1(300, 100, 25)
__red = hls360_to_hls1(0, 100, 50)
__rosybrown = hls360_to_hls1(0, 25, 65)
__royalblue = hls360_to_hls1(225, 73, 57)
__saddlebrown = hls360_to_hls1(25, 76, 31)
__salmon = hls360_to_hls1(6, 93, 71)
__sandybrown = hls360_to_hls1(28, 87, 67)
__seagreen = hls360_to_hls1(146, 50, 36)
__seashell = hls360_to_hls1(25, 100, 97)
__sienna = hls360_to_hls1(19, 56, 40)
__silver = hls360_to_hls1(0, 0, 75)
__skyblue = hls360_to_hls1(197, 71, 73)
__slateblue = hls360_to_hls1(248, 53, 58)
__slategray = hls360_to_hls1(210, 13, 50)    #same as slategrey
__slategrey = hls360_to_hls1(210, 13, 50)    #same as slategray
__snow = hls360_to_hls1(0, 100, 99)
__springgreen = hls360_to_hls1(150, 100, 50)
__steelblue = hls360_to_hls1(207, 44, 49)
__tan = hls360_to_hls1(34, 44, 69)
__teal = hls360_to_hls1(180, 100, 25)
__thistle = hls360_to_hls1(300, 24, 80)
__tomato = hls360_to_hls1(9, 100, 64)
__turquoise = hls360_to_hls1(174, 72, 56)
__violet = hls360_to_hls1(300, 76, 72)
__wheat = hls360_to_hls1(39, 77, 83)
__white = hls360_to_hls1(0, 100, 100)
__whitesmoke = hls360_to_hls1(0, 0, 96)
__yellow = hls360_to_hls1(60, 100, 50)
__yellowgreen = hls360_to_hls1(80, 61, 50)