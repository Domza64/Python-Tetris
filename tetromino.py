import copy
from random import randint

class Tetromino:
    TETROMINOS = {
        "C": [[1, -2], [1, -1], [2, -2], [2, -1]],
        "L": [[0, -1], [0, -2], [0,  0], [1,  0]],
        "L_2": [[3, -1], [3, -2], [3,  0], [2, 0]],
        "T": [[1, -2], [0, -1], [1, -1], [2, -1]],
        "I": [[6, -3], [6, -4], [6, -2], [6, -1]],
        "S": [[0, -1], [1, -1], [1, -2], [2, -2]],
        "Z": [[1, -1], [2, -1], [0, -2], [1, -2]]
    }

    def __init__(self):
        n = randint(0, len(Tetromino.TETROMINOS) - 1)
        key = list(Tetromino.TETROMINOS.keys())[n]
        self.type = key
        self.shape = copy.deepcopy(Tetromino.TETROMINOS[key])

    def can_move_to(self, game_matrix, new_pos):
        can_move_flag = True

        for point in new_pos:
            if point[0] < 0 or point[0] > 11:
                can_move_flag = False
                break
            if point[1] > 19: # Todo - Not hardcode this value
                can_move_flag = False
                break 
            if game_matrix[point[1]][point[0]] != '.' and point[1] >= 0:
                can_move_flag = False
                break

        return can_move_flag

    def rotate_right(self, game_matrix):
        px, py = self.shape[0]
        new_shape = [[px + (y - py), py - (x - px)] for x, y in self.shape]

        if self.can_move_to(game_matrix, new_shape):
            self.shape = new_shape

    def rotate_left(self, game_matrix):
        px, py = self.shape[0]
        new_shape = [[px + (y - py) * -1, py - (x - px) * -1] for x, y in self.shape]

        if self.can_move_to(game_matrix, new_shape):
            self.shape = new_shape

    def move_down(self, game):
        new_shape = copy.deepcopy(self.shape)
        
        for point in new_shape:
            point[1] += 1

        if self.can_move_to(game.matrix, new_shape):
            self.shape = new_shape
            return True
        else:
            return False
        
    def drop(self, game):
        while self.move_down(game):
            pass


    def move_right(self, game_matrix):
        new_shape = copy.deepcopy(self.shape)

        for point in new_shape:
            point[0] += 1

        if self.can_move_to(game_matrix, new_shape):
            self.shape = new_shape
            
    
    def move_left(self, game_matrix):
        new_shape = copy.deepcopy(self.shape)
        
        for point in new_shape:
            point[0] -= 1

        if self.can_move_to(game_matrix, new_shape):
            self.shape = new_shape
            

    def __str__(self):
        tetromino_string = ""
        for line in self.shape:
            tetromino_string += "".join(str(point) for point in line) + "\n"
        return tetromino_string