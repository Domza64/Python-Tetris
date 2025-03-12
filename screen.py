import os
import copy

def draw_frame(game):
    os.system('cls' if os.name == 'nt' else 'clear')

    frame = copy.deepcopy(game.matrix)

    if game.player != None:
        #print(f"Player: \n{game.player}")
        for point in game.player.shape:
            if point[1] >= 0: # Tetrominos spawn above game matrix so don't render them until they enter the matrix
                frame[point[1]][point[0]] = 'X'

    for y, line in enumerate(frame):
        print(''.join(line), end="")
        if y == 1:
            print(" " * 4, f"Speed: {game.speed}")
        elif y == 2:
            print(" " * 4, f"Score: {game.score}")
        elif y == 4:
            print(" " * 4, "Controls:")
        elif y == 5:
            print(" " * 6, "Q - Quit")
        elif y == 6:
            print(" " * 6, "A - Move left")
        elif y == 7:
            print(" " * 6, "D - Move right")
        elif y == 8:
            print(" " * 6, "l - Rotate right")
        elif y == 9:
            print(" " * 6, "k - Rotate left")
        elif y == 11:
            print(" " * 4, f"Tetromino: {game.player.type}")
        else:
            print()

    print()

def end_screen(score):
    os.system('cls' if os.name == 'nt' else 'clear')
    print
    print("Game over!")
    print(f"Your score was: {score}")