import os

from PIL import Image
from kp import KandinskyUniverse, RandomKandinskyFigure, SimpleObjectAndShape, ShapeOnShapes


if (__name__ == '__main__'):

    print('Welcome to the Kandinsky Figure Generator')
    u = KandinskyUniverse.SimpleUniverse()




    randomKFgenerator = RandomKandinskyFigure.Random (u,4,4)
    kfs = randomKFgenerator.true_kf (50)
    os.makedirs("../test/randomkf", exist_ok=True)

   
    print("the pattern is: ", randomKFgenerator.humanDescription())
    
    kfs = randomKFgenerator.true_kf (50)
    os.makedirs("../test/randomkf", exist_ok=True)
    i = 0
    for kf in kfs:
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        filename = "../test/randomkf/%06d" % i
        image.save (filename+".png")
        i = i + 1
        print (i)

    os.makedirs("../test/onered/true", exist_ok=True)
    os.makedirs("../test/onered/false", exist_ok=True)

    redobjects = SimpleObjectAndShape.ContainsRedObjects(u,4,4)
    print("the pattern is: ", redobjects.humanDescription())
   
    kfs = redobjects.true_kf (50)
    i = 0
    for kf in kfs:
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        filename = "../test/onered/true/%06d" % i
        image.save (filename+".png")
        i = i + 1 
    
    kfs = redobjects.false_kf (50)   
    i = 0 
    for kf in kfs:
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        filename = "../test/onered/false/%06d" % i
        image.save (filename+".png")
        i = i + 1        

    os.makedirs("../test/onetriangle/true", exist_ok=True)
    os.makedirs("../test/onetriangle/false", exist_ok=True)

    triangleobjects = SimpleObjectAndShape.ContainsTriangles(u,4,4)
    print("the pattern is: ", triangleobjects.humanDescription())
   
    kfs = triangleobjects.true_kf (50)
    i = 0
    for kf in kfs:
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        filename = "../test/onetriangle/true/%06d" % i
        image.save (filename+".png")
        i = i + 1 
    
    kfs = triangleobjects.false_kf (50)   
    i = 0 
    for kf in kfs:
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        filename = "../test/onetriangle/false/%06d" % i
        image.save (filename+".png")
        i = i + 1        