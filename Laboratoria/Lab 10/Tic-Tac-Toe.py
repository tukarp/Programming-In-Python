# Simple Tic-Tac-Toe Game


# Move class
class Move(object):
    # Define constructor
    def __init__(self, x, y, sign):
        self.x = x  # X coordinate
        self.y = y  # Y coordinate
        self.sign = sign  # Sign of the player


# Player class
class Player(object):
    # Define constructor
    def __init__(self, name, sign):
        self.name = name  # Name of the player
        self.sign = sign  # Sign of the player

    # Get player move
    def get_move(self):
        # Print player name
        print(f"{self.name}:")
        # Get X and Y coordinates
        x, y = map(int, input().split())

        # Check if coordinates are correct
        while x > 2 or y > 2:
            # Print error message
            print("Wrong coordinates!")
            # Get X and Y coordinates
            x, y = map(int, input().split())

        # Return move
        return Move(x, y, self.sign)


# Grid class
class Grid(object):
    # Define constructor
    def __init__(self):
        # Create grid
        self.grid = [["_", "_", "_"] for i in range(3)]

    # Print grid
    def __str__(self):
        # Create grid state
        return self.get_state()

    # Get grid state
    def get_state(self):
        # Initialize state
        state = ""

        # Iterate over rows
        for row in self.grid:
            # Add row to state
            state += "".join(row) + "\n"
        # Return state
        return state

    # Get grid field
    def get_field(self, x, y):
        # Return field in grid
        return self.grid[x][y]

    # Set grid field
    def set_field(self, move):
        # Check if field is empty
        if self.get_field(move.x, move.y) != "_":
            # Print error message
            print("This field is not empty!")
            # Return False
            return False
        # Set field
        self.grid[move.x][move.y] = move.sign
        # Return True
        return True


# Game class
class Game(object):
    # Define constructor
    def __init__(self):
        # Create grid
        self.grid = Grid()
        # Initialize winning sign
        self.winning_sign = None

    # Play game
    def play(self, player_one, player_two):
        # Create players tuple
        players = (player_one, player_two)
        # Initialize current player
        current_player = 0

        # While game is not over
        while not self.game_over():
            # While move is not possible
            while not self.grid.set_field(
                    players[current_player].get_move()):
                # Pass
                pass
            # Switch current player
            current_player ^= 1

            # Print grid
            print(self.grid)
        # If winning sign is None
        if self.winning_sign is None:
            # Print draw message
            print("Draw!")
        # If winning sign is player one sign
        elif self.winning_sign == player_one.sign:
            # Print player one won message
            print(f"{player_one.name} has won!")
        # If winning sign is player two sign
        else:
            # Print player two won message
            print(f"{player_two.name} has won!")

    # Check if game is over
    def game_over(self):
        # For each row
        for row in range(3):
            # If signs in row are the same
            if self.grid.get_field(row, 0) == \
                    self.grid.get_field(row, 1) == \
                    self.grid.get_field(row, 2) and \
                    self.grid.get_field(row, 0) != '_':
                # Set winning sign
                self.winning_sign = self.grid.get_field(row, 0)
                # Return True
                return True
        # For each column
        for column in range(3):
            # If signs in columns are the same
            if self.grid.get_field(0, column) == \
                    self.grid.get_field(1, column) == \
                    self.grid.get_field(2, column) and \
                    self.grid.get_field(0, column) != '_':
                # Set winning sign
                self.winning_sign = self.grid.get_field(0, column)
                # Return True
                return True
        # if signs on diagonal are the same
        if self.grid.get_field(0, 0) == \
                self.grid.get_field(1, 1) == \
                self.grid.get_field(2, 2) and \
                self.grid.get_field(0, 0) != '_':
            # Set winning sign
            self.winning_sign = self.grid.get_field(0, 0)
            # Return True
            return True
        # if signs on other diagonal are the same
        if self.grid.get_field(2, 0) == \
                self.grid.get_field(1, 1) == \
                self.grid.get_field(0, 2) and \
                self.grid.get_field(2, 0) != '_':
            # Set winning sign
            self.winning_sign = self.grid.get_field(2, 0)
            # Return True
            return True
        # If next move is not possible
        if not self.is_next_move_possible():
            # Set winning sign to None
            self.winning_sign = None
            # Return True
            return True
        # Return False
        return False

    # Check if next move is possible
    def is_next_move_possible(self):
        # Return True if "_" is in grid state
        return "_" in self.grid.get_state()


# Define main function
def main():
    # Create game object
    game = Game()

    # Create player one
    player_one = Player("Player One", "X")
    player_two = Player("Player Two", "O")

    # Start game with given players
    game.play(player_one, player_two)


# Main function
if __name__ == "__main__":
    # Call main function
    main()
