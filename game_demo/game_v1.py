class GridGame:
    def __init__(self, size=5):
        self.size = size
        self.grid = [["." for _ in range(size)] for _ in range(size)]
        self.x = size // 2
        self.y = size // 2
        self.grid[self.x][self.y] = "X"
    
    def move(self, direction):
        self.grid[self.x][self.y] = "."
        if direction == "up" and self.x > 0:
            self.x -= 1
        elif direction == "down" and self.x < self.size - 1:
            self.x += 1
        elif direction == "left" and self.y > 0:
            self.y -= 1
        elif direction == "right" and self.y < self.size - 1:
            self.y += 1
        else:
            print("Cannot move outside the grid.")
        self.grid[self.x][self.y] = "X"
    
    def display(self):
        print("\n".join([" ".join(row) for row in self.grid]))
    
    def ask_move(self):
        move = input("Enter your move (up, down, left, right or quit to exit): ").strip().lower()
        if move == "quit":
            print("Game over.")
            return  # Exit the recursive loop
        self.move(move)
        self.display()  # Reprint the grid after the move
        self.ask_move()  # Recursively ask for the next move

def main():
    game = GridGame()
    game.display()  # Print the initial grid
    game.ask_move()  # Start the game loop

if __name__ == "__main__":
    main()
