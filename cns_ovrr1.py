class circle:
    def __init__(self):         #original constructor
        print("Drawing circle-default constructor")
class sqr(circle):
    def __init__(self):      #overridden constructor
        print("drawing square--default constructor")
        super().__init__()
#main program
s=sqr()