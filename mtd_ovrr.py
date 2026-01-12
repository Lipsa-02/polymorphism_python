class circle:
    def draw(self):
        print("drawing circle")
class rect:
    def draw(self):
        print("drawing rectangle")
class square(rect,circle):
    def draw(self):
        print("drawing square")
        rect.draw(self)
        circle.draw(self)
#main
s= square()
s.draw()