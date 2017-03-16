#CS1 31 Ismael Garrido CircleWithLine.py


from graphics import*
from math import*

def Info():
    print("This program computes the intersection of a circle with a horizontal")
    print("line and prints out the information textually and graphically")
    print("The radius cannot be greater that 50")

def getInfo():
    while True:
        r = int(input("Please enter the radius of the circle: "))
        if r > 50:
            print("Invalid entry. Please try again")
            continue
        else:
            return r

def getYinter():
    y = input ("Please enter the y intercep: ")
    y = float(y)
    return y

def getXinter(r, y):
    x = sqrt((r**2 - y**2))
    x = float(x)
    return x
   
def createWin():
    r = getInfo()
    y = getYinter()
    x = getXinter(r, y)
    
    win = GraphWin("Cicle Interceptions", 800,800)
    win.setBackground("whitesmoke")
    win.setCoords( -50, -50, 50, 50)               

    center = Point(0 , 0)
    circ = Circle( center , r )
    circ.setFill('cyan')
    circ.draw(win)

    line = Line(Point(-50, y), Point(50, y))
    line.draw(win)

    center1 = Point (x, y)
    circ1 = Circle(center1, 0.5)
    circ1.setFill('red')
    circ1.draw(win)

    center2 = Point(-x, y)
    circ2 = Circle (center2, 0.5)
    circ2.setFill('red')
    circ2.draw(win)

    Text(Point(30,45),"X-intercept= ").draw(win)
    Text(Point(-35,45),"-X-intercept= ").draw(win)
    output = Text(Point(40, 45), '')
    output1 = Text(Point(-25,45), '')
    output1.setText(int (-x))
    output.setText(int (x))
    output.draw(win)
    output1.draw(win)

    print("The points of interception are: ")
    print("X1 = ", x)
    print("X2 = -", x)
    
def main():
    Info()
    createWin()
    

main()


