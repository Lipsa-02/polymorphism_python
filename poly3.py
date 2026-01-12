#area of figures using oops concept
class circle:
    def area(self):
        self.r=float(input("enter the radius:"))
        self.ar=3.14*self.r**2
        print("Area of circle:",self.ar)
class sqr:
    def area(self):
        self.a=float(input("enter the side of square:"))
        self.ar=self.a**2
        print("Area of square is :",self.ar)
class rect(circle,sqr):
    def area(self):
        self.l=float(input("enter length of the rectangle:"))
        self.b=float(input("enter breadth of rectangle:"))
        self.ar=self.l * self.b
        print("Area of rectangle is: ",self.ar)
        super().area()
        sqr.area(self)
#main program
r=rect()
r.area()