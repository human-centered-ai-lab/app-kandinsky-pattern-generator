from KandinskyUniverse import SimpleUniverse
from aot import SimpleObjectAndShapeRules


if (__name__ == '__main__'):
    print('Welcome in the Kandinsky Figure Generator')
    u = SimpleUniverse()
    redobjects = SimpleObjectAndShapeRules.ContainsRedObjects(u)
    print("the pattern is: ", redobjects.humanDescription())