from PIL import Image, ImageColor
image1 = 'IMG_1974.jpg'
image2 = 'Pittsburgh.jpg'
image3 = "/Users/kristasmith/Pictures/WP1/11-1.jpg"
image4 = "/Users/kristasmith/Desktop/Screen.png"
image5 = "/Users/kristasmith/Pictures/KBphotos/IMG_9146.jpg"
rj = "/Users/kristasmith/Desktop/RJ1.png"


from collections import Counter
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import math
import random
import numpy as np
from plotly.colors import make_colorscale

def round_colors(colors):
    k = list(colors.keys())[0]
    rounded_colors = {}
    for r in range(0,250, 10):
        for g in range(0,250, 10):
            for b in range(0,250, 10): 
                temp = []
                for ri in range(-5,5):
                    for bi in range(-5,5):
                        for gi in range(-5,5):
                            if len(k) == 4:
                                temp.append(colors[(r+ri, g+gi, b+bi, 255)])
                            else:
                                temp.append(colors[(r+ri, g+gi, b+bi)])
                if sum(temp)>0:
                    rounded_colors[(r,g,b)] = sum(temp)
    return rounded_colors

def make_array1(n):
    array = np.zeros((n,n))
    for r in range(n):
        for c in range(n):
            if r==c==0:
                array[r,c] = 0
            elif r-1 < 0:
                array[r,c] = array[r, c-1] + (c)
            else:
                array[r,c] = array[r-1, c] + (c+r+1)
    array[n-1,n-1] = int(array[n-1,n-1])
    return array

def make_array2(n):
    array = np.zeros((n,n))
    for r in range(n):
        for c in range(n):
            array[r,c] = (r**2 + c**2)**.5
    return array

def make_array3(n):
    center = int(n/2)
    
    array = np.zeros((n,n))
    for r in range(n):
        for c in range(n):
            array[r,c] = ((center-r)**2 + (center-c)**2)**.5
    return array

def make_array4(n):
    center = int(n/2)
    array_max = n**2
    array = np.zeros((n,n))
    for r in range(n):
        for c in range(n):
            array[r,c] = array_max - ((center-r)**2 + (center-c)**2)**.5
    return array

def make_color_map_and_array(colors, 
                             threshold = 30, 
                             make_sorted = False,
                             sort_key = 2, 
                             num_colors = None):
    top_colors = [x[0] for x in colors.items() if x[1]>threshold]
#     top_colors = [x[0] for x in top_colors]
    top_colors = [ImageColor.getrgb(x) for x in top_colors]
#     top_colors = [(x[0]/255, x[1]/255, x[2]/255)  for x in top_colors]
#     try:
#         top_colors = [(x[0]/255, x[1]/255, x[2]/255, x[3]/255)  for x in top_colors]
#     except IndexError:
#         top_colors = [(x[0]/255, x[1]/255, x[2]/255)  for x in top_colors]
    if num_colors == None:
        num_colors = len(top_colors)
    try:
        if make_sorted:
            select_col = sorted(random.sample(top_colors, num_colors), key = lambda x: x[sort_key])
        else:
            select_col =random.sample(top_colors, num_colors)
    except ValueError:
        num_colors = len(top_colors)
        if make_sorted:
            select_col = sorted(random.sample(top_colors, num_colors), key = lambda x: x[sort_key])
        else:
            select_col =random.sample(top_colors, num_colors)
    cm = [[x, f'rgb{y}'] for (x, y) in zip(np.linspace(0,1, len(select_col)), select_col)]
    return cm

#             (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])