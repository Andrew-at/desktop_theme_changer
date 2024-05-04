import turtle

bob = turtle.Turtle()

# sets the color of the pen to red
# background to black
bob.color("red")
turtle.Screen().bgcolor("black")

# generates a square with length sides
def square(t, length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)
    print(bob)
    
# generates a polygon with n sides
def polygon(t, length, n):
    for i in range(n):
        bob.fd(length)
        bob.lt(360 / n)
    print(bob)

# generates a circle with r radius
def circle(t, r, length):
    for i in range(r):
        bob.fd(length)
        bob.lt((360 / r))
    print(bob)

# generates a daisy
def daisy(t, length):
    for i in range(9):
        bob.fd(length)
        bob.rt(120)
        bob.color("red")
        for i in range(8):
            bob.fd(length)
            bob.lt(-20)
            bob.color("orange")

    print(bob)

# generates a nautilus
def nautilus(t):
    size = 1
    while (True):
        for i in range(4):
            bob.fd(size)
            bob.rt(90)
            size = size + 1
        bob.rt(10)

# generates a  turbine shape
def turbine(t, length):
    for i in range(16):
        bob.fd(length)
        bob.lt(-45)
        for i in range(5):
            bob.fd(length)
            bob.rt(2)
            for i in range(8):
                bob.fd(length)
                bob.rt(-94)
                for i in range(16):
                    bob.fd(length)
                    bob.lt(10)
    print(bob)

def fibonacci(t, length):
    if length == 0:
        return 0
    elif length == 1:
        return 1
    else:
        return fibonacci(t, length-1) + fibonacci(t, length-2)

# coming back to this one later
'''
def arc(t, r, length, angle):
    bob = t
    for i in range(r):
        bob.fd(length)
        bob.lt((angle))
    print(bob)
'''
#nautilus(bob)
# polygon(bob,50, 5)
# circle(bob, 50, 10)
# arc(bob, 20, 10, 360)
# turbine(bob, 10)
# daisy(bob, 20)

input1 = ''
while input1 != 'q':
    input1 = input("Please c, p, a or s for shapebuilder: ")
    print("c = circle, p = polygon, a = arc, s = square")
    print("Press 'q' to quit.")

    if input1 == 'c':
        circle(bob, r=10, length=20)

    elif input1 == 'p':
        polygon(bob, length=40,n=7)

    elif input1 == 's':
        square(bob, length=40)

    elif input1 == 'f':
        fibonacci(bob, length=10)

turtle.mainloop()
