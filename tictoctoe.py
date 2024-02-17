from turtle import Turtle, Screen
import time

class TicTacToe:
    def __init__(self, screen: Screen) -> None:

        """
        Initialize the TicTacToe class with the given screen, and set up the initial game state.
        """

        self.screen: Screen = screen
        self.board: list = [[0]*3 for _ in range(3)]
        self.turn: int = 1
        self.game_over: bool = False
        self.winner_turtle: Turtle = Turtle()
        self.winner_turtle.hideturtle()
        self.winner_turtle.color('green')
        self.winner_turtle.penup()
        self.winner_turtle.goto(0, 200)
    
    def draw_x(self, x: int, y: int) -> bool:

        """
        Draw an X on the board at the specified grid position (x, y) if the game is not over. 
        The function returns True if the X is successfully drawn, and False otherwise.
        
        Parameters:
        - x (int): The x-coordinate of the grid position.
        - y (int): The y-coordinate of the grid position.
        
        Returns:
        - bool: True if the X is successfully drawn, False otherwise.
        """

        if self.game_over:
            return
        try:
            positions = self.get_grid_position(x, y)       
            if self.board[positions[0]][positions[1]] == 0:
                if positions:
                    self.board[positions[0]][positions[1]] = self.turn
                
                if -150 < x < -50 and 50 < y < 150:
                    x, y = -100, 100
                elif -50 < x < 50 and 50 < y < 150:
                    x, y = 0, 100
                elif 50 < x < 150 and 50 < y < 150:
                    x, y = 100, 100
                elif -150 < x < -50 and -50 < y < 50:
                    x, y = -100, 0
                elif -50 < x < 50 and -50 < y < 50:
                    x, y = 0, 0
                elif 50 < x < 150 and -50 < y < 50:
                    x, y = 100, 0
                elif -150 < x < -50 and -150 < y < -50:
                    x, y = -100, -100
                elif -50 < x < 50 and -150 < y < -50:
                    x, y = 0, -100
                elif 50 < x < 150 and -150 < y < -50:
                    x, y = 100, -100
                else:
                    return False
                
                turtle: Turtle = Turtle(visible=False)
                turtle.color('white')
                turtle.speed(0)
                turtle.penup()
                turtle.goto(-50+x, 50+y)
                turtle.pendown()
                turtle.goto(50+x, -50+y)
                turtle.penup()
                turtle.goto(-50+x, -50+y)
                turtle.pendown()
                turtle.goto(50+x, 50+y)
                self.check_winner()
                return True
        except:
            print('Something went wrong')
            

    def draw_o(self, x: int, y: int) -> bool:

        """
        Draw an 'O' on the game board at the given x, y position if the game is not over.

        Parameters:
            x (int): The x-coordinate of the position to draw the 'O'.
            y (int): The y-coordinate of the position to draw the 'O'.

        Returns:
            bool: True if the 'O' was successfully drawn, False otherwise.
        """
        if self.game_over:
            return
        
        try:
            positions = self.get_grid_position(x, y)
            if self.board[positions[0]][positions[1]] == 0:
                if positions:
                    self.board[positions[0]][positions[1]] = self.turn
            
                if -150 < x < -50 and 50 < y < 150:
                    x, y = -100, 100
                elif -50 < x < 50 and 50 < y < 150:
                    x, y = 0, 100
                elif 50 < x < 150 and 50 < y < 150:
                    x, y = 100, 100
                elif -150 < x < -50 and -50 < y < 50:
                    x, y = -100, 0
                elif -50 < x < 50 and -50 < y < 50:
                    x, y = 0, 0
                elif 50 < x < 150 and -50 < y < 50:
                    x, y = 100, 0
                elif -150 < x < -50 and -150 < y < -50:
                    x, y = -100, -100
                elif -50 < x < 50 and -150 < y < -50:
                    x, y = 0, -100
                elif 50 < x < 150 and -150 < y < -50:
                    x, y = 100, -100
                else:
                    return False
                
                turtle: Turtle = Turtle(visible=False)
                turtle.color('white')
                turtle.speed(0)
                turtle.penup()
                turtle.goto(0+x, -50+y)
                turtle.pendown()
                turtle.circle(50)
                self.check_winner()
                return True

        except:
            print('Something went wrong')

    def draw(self, x: int, y: int) -> None:
        """
        Draws either an 'X' or an 'O' at the specified position based on the current turn. 

        Args:
            x (int): The x-coordinate of the position to draw the symbol.
            y (int): The y-coordinate of the position to draw the symbol.

        Returns:
            None
        """
        if self.turn == 1:
            self.turn: int = 2
            success: bool = self.draw_x(x, y)
        else:
            self.turn: int = 1
            success: bool = self.draw_o(x, y)
        
        if success:
            time.sleep(0.2)
        
    def player(self) -> None:
        """
        A method that handles player input by calling the draw method when the screen is clicked.
        """
        self.screen.onscreenclick(self.draw)

    def get_grid_position(self, x: int, y: int) -> tuple[int, int] | None:
        """
        Get the grid position based on the clicked coordinates.
        """
        if -150 < x < -50:
            grid_x = 0
        elif -50 < x < 50:
            grid_x = 1
        elif 50 < x < 150:
            grid_x = 2
        else:
            return None
        
        if 50 < y < 150:
            grid_y = 0
        elif -50 < y < 50:
            grid_y = 1
        elif -150 < y < -50:
            grid_y = 2
        else:
            # Clicked outside the grid
            return None
        
        return grid_x, grid_y

    def check_winner(self) -> None:
        """
        Check if there is a winner.
        """
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != 0:
                self.game_over: bool = True
                self.winner_turtle.write(f"Player {row[0]} wins!", align="center", font=("Arial", 24, "bold"))
                return
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != 0:
                self.game_over: bool = True
                self.winner_turtle.write(f"Player {self.board[0][col]} wins!", align="center", font=("Arial", 24, "bold"))
                return
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            self.game_over: bool = True
            self.winner_turtle.write(f"Player {self.board[0][0]} wins!", align="center", font=("Arial", 24, "bold"))
            return
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != 0:
            self.game_over: bool = True
            self.winner_turtle.write(f"Player {self.board[0][2]} wins!", align="center", font=("Arial", 24, "bold"))
            return


