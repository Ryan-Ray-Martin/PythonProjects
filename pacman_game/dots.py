from dot import Dot
from game_controller import GameController


class Dots:
    """A collection of dots."""
    def __init__(self, WIDTH, HEIGHT,
                 LEFT_VERT, RIGHT_VERT,
                 TOP_HORIZ, BOTTOM_HORIZ, game_controller):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TH = TOP_HORIZ
        self.BH = BOTTOM_HORIZ
        self.LV = LEFT_VERT
        self.RV = RIGHT_VERT
        self.SPACING = 75
        self.EAT_DIST = 60
        self.gc = game_controller
        # Initialize four rows of dots, based on spacing and width of the maze
        self.top_row = [Dot(self.SPACING * i, self.TH)
                        for i in range(self.WIDTH//self.SPACING + 1)]
        self.bottom_row = [Dot(self.SPACING * i, self.BH)
                           for i in range(self.WIDTH//self.SPACING + 1)]
        self.left_col = [Dot(self.LV, self.SPACING * i)
                         for i in range(self.HEIGHT//self.SPACING + 1)]
        self.right_col = [Dot(self.RV, self.SPACING * i)
                          for i in range(self.HEIGHT//self.SPACING + 1)]
        self.total = self.top_row + self.bottom_row + self.left_col \
            + self.right_col

    def display(self):
        """Calls each dot's display method"""
        for i in range(0, len(self.total)):
            self.total[i].display()

    # TODO:
    # PROBLEM 3: implement dot eating
    # BEGIN CODE CHANGES
    def eat(self, x_position, y_position):  # You might want/need to pass arguments here.
        for i in self.total:
            if abs(x_position - i.x) < self.EAT_DIST and abs(y_position - i.y)\
            < self.EAT_DIST:
                self.total.remove(i)
                
    # END CODE CHANGES

    def dots_left(self):
        """Returns the number of remaing dots in the collection"""
        return (len(self.total))
 
