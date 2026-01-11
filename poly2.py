class circle:
    def draw(self):
        print("Drawing circle")
class rect(circle):
    def draw(self):
        print("drawing rectangle")
        #super().draw()
class sqr(rect):
    def draw(self):
        print("drawing square")
        super().draw()
#main program
s= sqr()
s.draw()