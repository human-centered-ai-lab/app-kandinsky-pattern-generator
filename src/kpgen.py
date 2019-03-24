import os

from PIL import Image
from aot import KandinskyUniverse, SimpleObjectAndShapeRules


if (__name__ == '__main__'):
    print('Welcome in the Kandinsky Figure Generator')
    u = KandinskyUniverse.SimpleUniverse()
    redobjects = SimpleObjectAndShapeRules.ContainsRedObjects(u)
    print("the pattern is: ", redobjects.humanDescription())
 
    randomobjects = SimpleObjectAndShapeRules.RandomObjects (u)
    print("the pattern is: ", randomobjects.humanDescription())
    kfs = randomobjects.true_kf (100)
    os.makedirs("../test/randomkf", exist_ok=True)
    i = 0
    for kf in kfs:
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        filename = "../test/randomkf/%06d" % i
        image.save (filename+".png")
        i = i + 1