import copy
from random import randint

class Tetromino:
    def __init__(self):
        self.shape = []
        n = randint(0, 6)
        if n == 0:
            self._tetromino_cube()
            self.type = "cube"
        elif n == 1:
            self._tetromino_L()
            self.type = "L"
        elif n == 2:
            self._tetromino_L_2()
            self.type = "L_2"
        elif n == 3:
            self._tetromino_T()
            self.type = "T"
        elif n == 4:
            self._tetromino_I()
            self.type = "I"
        elif n == 5:
            self._tetromino_S()
            self.type = "S"
        elif n == 6:
            self._tetromino_Z()
            self.type = "Z"

    def _tetromino_cube(self):
        self.shape.append([1, -2])
        self.shape.append([1, -1])
        self.shape.append([2, -2])
        self.shape.append([2, -1])

    def _tetromino_L(self):
        self.shape.append([0, -1])
        self.shape.append([0, -2])
        self.shape.append([0,  0])
        self.shape.append([1,  0])

    def _tetromino_L_2(self):
        self.shape.append([1, -1])
        self.shape.append([1, -2])
        self.shape.append([1,  0])
        self.shape.append([0,  0]) 

    def _tetromino_T(self):
        self.shape.append([1, -2])
        self.shape.append([0, -1])
        self.shape.append([1, -1])
        self.shape.append([2, -1])

    def _tetromino_I(self):
        self.shape.append([6, -3])
        self.shape.append([6, -4])
        self.shape.append([6, -2])
        self.shape.append([6, -1])

    def _tetromino_Z(self):
        self.shape.append([1, -1])
        self.shape.append([2, -1])
        self.shape.append([0, -2])
        self.shape.append([1, -2])

    def _tetromino_S(self):
        self.shape.append([0, -1])
        self.shape.append([1, -1])
        self.shape.append([1, -2])
        self.shape.append([2, -2])

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