import os
import copy
import builtins

def print(*args, **kwargs):
    builtins.print("\033[92m", end="")  # ANSI code for green
    builtins.print(*args, **kwargs)
    builtins.print("\033[0m", end="")  # Reset color

TETRIS = """
 ████████╗███████╗████████╗██████╗ ██╗███████╗
 ╚══██╔══╝██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝
    ██║   █████╗     ██║   ██████╔╝██║███████╗
    ██║   ██╔══╝     ██║   ██╔══██╗██║╚════██║
    ██║   ███████╗   ██║   ██║  ██║██║███████║
    ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝
"""

def draw_frame(game):
    os.system('cls' if os.name == 'nt' else 'clear')

    frame = copy.deepcopy(game.matrix)
    border_char = "▓"
    empty_cell = " "
    block_char = "■"
    prediction_char = "+"

    # Add tetromino to frame
    if game.player is not None:
        for point in game.player.shape:
            # Draw prediction line
            temp_player = copy.deepcopy(game.player)
            moved_down = True
            while moved_down:
                moved_down = temp_player.move_down(game)

            for point in temp_player.shape:
                frame[point[1]][point[0]] = prediction_char

        for point in game.player.shape:
            if point[1] >= 0:  # Tetrominos spawn above game matrix so don't render them until they enter the matrix
                frame[point[1]][point[0]] = block_char
        

    # Title and score
    print(TETRIS)
    print(f"  Score: {game.score}   Speed: {game.speed:.2f}\n")

    
    # Top border
    width = len(frame[0])
    print("  " + border_char * (width + 2))

    # Draw game matrix with side borders
    for y, line in enumerate(frame):
        print(f"  {border_char}{''.join(line).replace('.', empty_cell)}{border_char}", end="")

        if y == 2:
            print("   Controls:")
        elif y == 3:
            print("   Q - Quit")
        elif y == 4:
            print("   A - Move left")
        elif y == 5:
            print("   D - Move right")
        elif y == 6:
            print("   L - Rotate right")
        elif y == 7:
            print("   K - Rotate left")
        elif y == 9 and game.player:
            print(f"   Tetromino: {game.player.type}")
        else:
            print()

    # Bottom border
    print("  " + border_char * (width + 2))
    print()

def end_screen(score):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Game Over!")
    print(f"\n  Your final score: {score}\n")