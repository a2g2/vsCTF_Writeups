from PIL import Image
# This Code is Quote from https://github.com/corax/writeups/blob/a9cecddd1c36794aa802de015299dcaa5fc9a0ab/zh3r0/RainbowHex.md
def hexahue_to_ascii(colors):
    """
    P = Purple
    R = Red
    G = Green
    Y = Yellow
    B = Blue
    C = Cyan
    b = black
    w = white
    g = gray/grey
    """

    hexahue = {
        "PRGYBC": "a",
        "RPGYBC": "b",
        "RGPYBC": "c",                                                                                                                                  
        "RGYPBC": "d",                                                                                                                                  
        "RGYBPC": "e",                                                                                                                                  
        "RGYBCP": "f",                                                                                                                                  
        "GRYBCP": "g",                                                                                                                                  
        "GYRBCP": "h",                                                                                                                                  
        "GYBRCP": "i",                                                                                                                                  
        "GYBCRP": "j",                                                                                                                                  
        "GYBCPR": "k",                                                                                                                                  
        "YGBCPR": "l",                                                                                                                                  
        "YBGCPR": "m",                                                                                                                                  
        "YBCGPR": "n",                                                                                                                                  
        "YBCPGR": "o",                                                                                                                                  
        "YBCPRG": "p",                                                                                                                                  
        "BYCPRG": "q",                                                                                                                                  
        "BCYPRG": "r",                                                                                                                                  
        "BCPYRG": "s",                                                                                                                                  
        "BCPRYG": "t",                                                                                                                                  
        "BCPRGY": "u",                                                                                                                                  
        "CBPRGY": "v",                                                                                                                                  
        "CPBRGY": "w",                                                                                                                                  
        "CPRBGY": "x",                                                                                                                                  
        "CPRGBY": "y",                                                                                                                                  
        "CPRGYB": "z",                                                                                                                                  
        "bwwbbw": ".",
        "wbbwwb": ",",
        "wwwwww": " ",
        "bbbbbb": " ",
        "bgwbgw": "0",
        "gbwbgw": "1",
        "gwbbgw": "2",
        "gwbgbw": "3",
        "gwbgwb": "4",
        "wgbgwb": "5",
        "wbggwb": "6",
        "wbgwgb": "7",
        "wbgwbg": "8",
        "bwgwbg": "9"
    }

    if colors in hexahue:
        return hexahue.get(colors)
    else:
        return '?'

def getHexahue(pixels, base_x, base_y):
    first = pixels[base_x + 5, base_y + 5]
    second = pixels[base_x + 15, base_y + 5]
    third = pixels[base_x + 5, base_y + 15]
    fourth = pixels[base_x + 15, base_y + 15]
    fifth = pixels[base_x + 5, base_y + 25]
    sixth = pixels[base_x + 15, base_y + 25]

    colors = [first, second, third, fourth, fifth, sixth]

    #print(colors)

    hexahue = ''
    for (red,green,blue) in colors:

        if red > 240 and green > 240 and blue < 100:
            hexahue += 'Y'
        elif red < 100 and green < 100 and blue > 240:
            hexahue += 'B'
        elif 0 == red  and green > 240 and blue == 0:
            hexahue += 'G'
        elif red < 100 and green > 240 and blue > 240: 
            hexahue += 'C'
        elif red > 240 and green < 100 and blue > 240:
            hexahue += 'P'
        elif red > 240 and green < 100 and blue < 100:
            hexahue += 'R'
        elif red < 100 and green < 100 and blue < 100:
            hexahue += 'b'
        elif red > 230 and green > 230 and blue > 230:
            hexahue += 'w'
        elif 50 < red < 150 and 50 < green < 150 and 50 < blue < 150:
            hexahue += 'g'
        else:
            hexahue += '?'

    # Any one we haven't solved?
    if '?' in hexahue:
        print(str(colors) + " => " + hexahue )

    #print(hexahue)
    return hexahue

img = Image.open("hexhuebad.png")
#given to us hexhuebad.png
pixels = img.load()
width, height = img.size

x = 10
y = 10

for i in range(3711):
    c = hexahue_to_ascii(getHexahue(pixels, x, y))
    print(c,end="")
    x += 30
#the original code analyzes multiple images thus modified accordingly.
#from the final output we can easily obtain the Flag.