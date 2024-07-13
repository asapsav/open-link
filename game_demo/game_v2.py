import tkinter as tk
from PIL import Image, ImageTk

class GridGameGUI:
    def __init__(self, master, size=14, player_image_path='game_demo/sama_face.png', background_image_path='game_demo/sf_map.jpeg'):
        self.master = master
        self.size = size
        self.player_image_path = player_image_path
        self.background_image_path = background_image_path
        self.x = size // 2
        self.y = size // 2
        self.player_images = {}  # Dictionary to hold image references
        self.init_ui()
        
    def init_ui(self):
        # Create a canvas for the background and the grid
        self.canvas = tk.Canvas(self.master, width=700, height=700)  # Adjust size as needed
        self.canvas.pack(fill="both", expand=True)
        
        # Load and add the background image
        bg_image = Image.open(self.background_image_path)
        bg_image = bg_image.resize((700, 700), Image.ANTIALIAS)  # Adjust size as needed
        self.bg_photo_image = ImageTk.PhotoImage(bg_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo_image)
        
        # Add grid cells on top of the background
        self.create_widgets()
        
    def create_widgets(self):
        cell_size = 700 // self.size  # Adjust cell size based on canvas size and grid size
        for i in range(self.size):
            for j in range(self.size):
                self.create_cell(i, j, cell_size)
                
    def create_cell(self, i, j, cell_size):
        is_player = i == self.x and j == self.y
        if is_player:
            player_image = Image.open(self.player_image_path).resize((cell_size, cell_size), Image.ANTIALIAS)
            self.player_photo_image = ImageTk.PhotoImage(player_image)  # Convert to PhotoImage
            self.canvas.create_image(j * cell_size, i * cell_size, anchor="nw", image=self.player_photo_image)
        
    def update_grid(self):
        self.canvas.delete("all")  # Clear the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo_image)  # Redraw the background
        self.create_widgets()  # Redraw the grid elements
        
    def move(self, direction):
        if direction == "up" and self.x > 0:
            self.x -= 1
        elif direction == "down" and self.x < self.size - 1:
            self.x += 1
        elif direction == "left" and self.y > 0:
            self.y -= 1
        elif direction == "right" and self.y < self.size - 1:
            self.y += 1
        self.update_grid()

def on_key_press(event, game):
    key = event.keysym.lower()
    if key in ["up", "down", "left", "right"]:
        game.move(key)

def main():
    root = tk.Tk()
    root.title("Grid Game")
    game = GridGameGUI(root, size=14, player_image_path='game_demo/sama_face.png', background_image_path='game_demo/sf_map.jpeg')  # Update paths as needed
    root.bind("<Key>", lambda event: on_key_press(event, game))
    root.mainloop()

if __name__ == "__main__":
    main()
