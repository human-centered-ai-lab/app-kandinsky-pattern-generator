import os

from PIL import Image
from aot import KandinskyUniverse, RandomKandinskyFigure, SimpleObjectAndShapeRules


if (__name__ == '__main__'):

    print('Welcome to the Kandinsky Figure Generator')
    u = KandinskyUniverse.SimpleUniverse()
 
    randomKFgenerator = RandomKandinskyFigure.Random (u,40,40)
    print("the pattern is: ", randomKFgenerator.humanDescription())
    
    kfs = randomKFgenerator.true_kf (20)
    os.makedirs("../test/randomkf", exist_ok=True)
    i = 0
    for kf in kfs:
        image = KandinskyUniverse.kandinskyFigureAsImage (kf, 600, 4)
        filename = "../test/randomkf/%06d" % i
        image.save (filename+".png")
        i = i + 1

    os.makedirs("../test/onered/t", exist_ok=True)
    os.makedirs("../test/onered/f", exist_ok=True)

    redobjects = SimpleObjectAndShapeRules.ContainsRedObjects(u,4,4)
    print("the pattern is: ", redobjects.humanDescription())
   
    kfs = redobjects.true_kf (20)
    i = 0
    for kf in kfs:
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        filename = "../test/onered/t/%06d" % i
        image.save (filename+".png")
        i = i + 1 
    
    kfs = redobjects.false_kf (20)   
    i = 0 
    for kf in kfs:
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        filename = "../test/onered/f/%06d" % i
        image.save (filename+".png")
        i = i + 1        

    os.makedirs("../test/onetriangle/t", exist_ok=True)
    os.makedirs("../test/onetriangle/f", exist_ok=True)

    triangleobjects = SimpleObjectAndShapeRules.ContainsTriangles(u,4,4)
    print("the pattern is: ", triangleobjects.humanDescription())
   
    kfs = triangleobjects.true_kf (20)
    i = 0
    for kf in kfs:
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        filename = "../test/onetriangle/t/%06d" % i
        image.save (filename+".png")
        i = i + 1 
    
    kfs = triangleobjects.false_kf (20)   
    i = 0 
    for kf in kfs:
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        filename = "../test/onetriangle/f/%06d" % i
        image.save (filename+".png")
        i = i + 1        