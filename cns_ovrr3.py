class circle:
    def __init__(self):
        print("drawing circle")
class sqr(circle):
    def __init__(self):
        print("drawing square")
class rect(sqr):
    def __init__(self):
        print("drawing rectangle")
        sqr.__init__(self)
        circle.__init__(self)
#main
r=rect()