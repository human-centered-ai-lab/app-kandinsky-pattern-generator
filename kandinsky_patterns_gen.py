"""
    Kandinsky patterns generator

    :author: Anna Saranti
    :copyright: © 2019 HCI-KDD (ex-AI) group
    :date: 2019-11-13
"""

import numpy as np
import os
import math
import random

from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageChops

WIDTH = 120
MINSIZE = 20
MAXSIZE = 40

kandinsky_colors = ["red", "yellow", "blue"]
kandinsky_numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]


def square(d, cx, cy, s, f):
    """
    Square

    :param d:
    :param cx:
    :param cy:
    :param s:
    :param f:
    :return:
    """
    s = 0.7 * s
    d.rectangle(((cx - s / 2, cy - s / 2), (cx + s / 2, cy + s / 2)), fill=f)


def circle(d, cx, cy, s, f):
    """
    Circle: correct the size to  the same area as an square

    :param d:
    :param cx:
    :param cy:
    :param s:
    :param f:
    :return:
    """

    s = 0.7 * s * 4 / math.pi
    d.ellipse(((cx - s / 2, cy - s / 2), (cx + s / 2, cy + s / 2)), fill=f)


def triangle(d, cx, cy, s, f):
    """
    Triangle: correct the size to  the same area as an square

    :param d:
    :param cx:
    :param cy:
    :param s:
    :param f:
    :return:
    """

    r = math.radians(30)

    s = 0.7 * s * 3 * math.sqrt(3) / 4
    dx = s * math.cos(r) / 2
    dy = s * math.sin(r) / 2
    d.polygon([(cx, cy - s / 2), (cx + dx, cy + dy), (cx - dx, cy + dy)], fill=f)


kandinsky_shapes = [square, circle, triangle]


def kandinsky_figure(shapes, subsampling=1):
    """


    :param shapes:
    :param subsampling: Factor by which the height and width of the images are multiplied
    :return:
    """

    image = Image.new(
        "RGBA", (subsampling * WIDTH, subsampling * WIDTH), (220, 220, 220, 255)
    )

    d = ImageDraw.Draw(image)
    for shape in shapes:
        shape["shape"](
            d,
            subsampling * shape["cx"],
            subsampling * shape["cy"],
            subsampling * shape["size"],
            shape["color"],
        )
    if subsampling > 1:
        image = image.resize((WIDTH, WIDTH), Image.BICUBIC)
    return image


def overlaps(shapes):
    """


    :param shapes:
    :return:
    """

    image = Image.new("L", (WIDTH, WIDTH), 0)
    sumarray = np.array(image)
    d = ImageDraw.Draw(image)

    for s in shapes:
        image = Image.new("L", (WIDTH, WIDTH), 0)
        d = ImageDraw.Draw(image)
        s["shape"](d, s["cx"], s["cy"], s["size"], 10)
        sumarray = sumarray + np.array(image)

    sumimage = Image.fromarray(sumarray)
    return sumimage.getextrema()[1] > 10


def combine_figures(n, f):
    """


    :param n:
    :param f:
    :return:
    """

    images = []
    for i in range(n):
        shapes = f()
        while overlaps(shapes):
            shapes = f()
        image = kandinsky_figure(shapes, 4)
        images.append(image)

    allimages = Image.new(
        "RGBA", (WIDTH * n + 20 * (n - 1), WIDTH), (255, 255, 255, 255)
    )
    for i in range(n):
        allimages.paste(images[i], (WIDTH * i + 20 * (i), 0))
    return allimages


def random_shapes(min_shape_nr: int, max_shape_nr: int) -> list:
    """
    Generate a random number of shapes between [min_shape_nr, max_shape_nr] with a random color each.

    :param min_shape_nr: Minimum number of generated shapes
    :param max_shape_nr: Maximum number of generated shapes
    :return: List with all generated shapes
    """

    shapes_nr = random.randint(min_shape_nr, max_shape_nr)
    shapes = []
    for shape_idx in range(shapes_nr):

        cx = random.randint(MAXSIZE / 2, WIDTH - MAXSIZE / 2)
        cy = random.randint(MAXSIZE / 2, WIDTH - MAXSIZE / 2)

        size = random.randint(MINSIZE, MAXSIZE)
        random_color_idx = random.randint(0, 2)
        random_shape_idx = random.randint(0, 2)

        shape = {
            "shape": kandinsky_shapes[random_shape_idx],
            "cx": cx,
            "cy": cy,
            "size": size,
            "color": kandinsky_colors[random_color_idx],
        }
        shapes.append(shape)

    return shapes

DELTASIZE = MAXSIZE - MINSIZE
SMALLSIZECHECK = MINSIZE + DELTASIZE / 3
BIGSIZECHECK = MAXSIZE - DELTASIZE / 3


def description_color_shape_size(shapes: list, prefix: str="") -> str:
    """
    Compute description of color, shape and size of a list of shapes.
    The color, shape and size of the shapes are gathered and concatenated

    :param shapes: List of shapes that will be described
    :param prefix: Prefix of description
    :return:
    """

    descrition = prefix
    multiple_shape = False  # Bool: Is a shape already described ?

    for shape in shapes:

        if multiple_shape:
            descrition = descrition + " and " + prefix

        size_str = ""

        if shape["size"] < SMALLSIZECHECK:
            size_str = "small"
        if shape["size"] > BIGSIZECHECK:
            size_str = "big"
        if len(size_str) > 0:
            descrition = descrition + size_str + " "

        descrition = descrition + shape["color"] + " " + shape["shape"].__name__
        multiple_shape = True

    return descrition


def describe_numbers(shapes: list):
    """
    TODO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    :param shapes:
    :return:
    """

    descrition = description_color_shape_size(shapes, "one ")
    # lets look if we find some patterns
    ns = {}
    nc = {}
    for s in kandinsky_shapes:
        ns[s] = 0
    for s in kandinsky_colors:
        nc[s] = 0
    for s in shapes:
        ns[s["shape"]] += 1
        nc[s["color"]] += 1
    maxcolor = ""
    maxshape = ""
    maxnumcolor = 0
    maxnumshap = 0
    for c in kandinsky_colors:
        if nc[c] > maxnumcolor:
            maxnumcolor = nc[c]
            maxcolor = c
    for s in kandinsky_shapes:
        if ns[s] > maxnumshap:
            maxnumshap = ns[s]
            maxshape = s.__name__

    if maxnumcolor > 1 or maxnumshap > 1:
        if maxnumcolor >= maxnumshap:
            descrition = kandinsky_numbers[maxnumcolor] + " " + maxcolor + " shapes"
        else:
            descrition = kandinsky_numbers[maxnumshap] + " " + maxshape + "s"

        if (maxnumcolor == maxnumshap) and (maxnumcolor == len(shapes)):
            descrition = (
                kandinsky_numbers[maxnumshap] + " " + maxcolor + " " + maxshape + "s"
            )

    return descrition


def descPairs(shapes):
    """
    Describe pairs: thats not perfect, it e.g. does not describe two pairs, or a pair, if some other shape has 3 objects

    :param shapes:
    :return:
    """

    descrition = ""
    ns = {}
    for s in kandinsky_shapes:
        ns[s] = 0
    for s in shapes:
        ns[s["shape"]] += 1
    maxshape = ""
    maxnumshap = 0
    for s in kandinsky_shapes:
        if ns[s] > maxnumshap:
            maxnumshap = ns[s]
            maxshape = s.__name__
    if maxnumshap == 2:
        descrition = "a pair of " + maxshape + "s"
    return descrition


########################################################################################################################
# [1.] Generate Captions ===============================================================================================
########################################################################################################################
f = lambda: random_shapes(6, 8)
shapes = f()
while overlaps(shapes) or len(descPairs(shapes)) == 0:
    shapes = f()

print(description_color_shape_size(shapes))
print(describe_numbers(shapes))
print(descPairs(shapes))

kandinsky_figure(shapes, 4)
