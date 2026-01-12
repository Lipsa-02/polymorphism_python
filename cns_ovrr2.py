class circle:
    def __init__(self):
        print("drawing circle")   # original constructor
class sqr(circle):
    def __init__(self):
        print("drawing square")
        super().__init__()
class rect(sqr):
    def __init__(self):
        print("drawing rectangle")
        super().__init__()

#main program
s=rect()