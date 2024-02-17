from turtle import Screen, Turtle
STARTING_POINTS = [(-50, 150, 90), (50, 150, 90), (-150, 50, 0), (-150, -50, 0)]
class Playground:
    def __init__(self) -> None:
        """
        Constructor for initializing the class. 
        No parameters are passed.
        Returns None.
        """
        self.screen: Screen = Screen()
        self.screen.bgcolor('black')
        self.screen.setup(width=600, height=600)
        self.draw_lines()
        self.screen.listen()

    def draw_lines(self) -> None:

        """
        Draws lines using Turtle to create a square shape with given starting points. No parameters. Returns None.
        """

        
        line = Turtle(visible=False)
        line.speed(6)
        line.penup()
        line.goto(-150, 150)
        line.pendown()
        line.color('white')
        for _ in range(4):
            line.forward(300)
            line.right(90)
        for points in STARTING_POINTS:
            self.parellels(points)

    def parellels(self,points: list) -> None:
        """
        Define a function to draw a line using Turtle from the first point to the second point with a given angle. 

        Args:
            self: the instance of the class
            points: a list of two coordinates representing the start and end points, and a third coordinate representing the angle

        Returns:
            None
        """
        line: Turtle = Turtle(visible=False)
        line.speed(6)
        line.penup()
        line.goto(points[0], points[1])
        line.pendown()
        line.color('white')
        line.right(points[2])
        line.forward(300)
