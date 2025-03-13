import sys
import termios
import tty
import select
import time
from screen import draw_frame, end_screen
from tetromino import Tetromino


class Game:
    WIDTH = 12
    HEIGTH = 20
    INITIAL_SPEED = 1.0
    MIN_SPEED = 0.05

    def __init__(self):
        self.player = Tetromino()
        self.next = Tetromino()
        self.matrix = [['.' for _ in range(Game.WIDTH)] for _ in range(Game.HEIGTH)]

        self.should_quit = False
        self.user_input = None
        self.speed = Game.INITIAL_SPEED
        self.last_move_down_time = time.time()
        self.score = 0

    def check_input(self):
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            key = sys.stdin.read(1)
            # Flushing input buffer makes it a lot better but still needs fixing if key is pressed and held for too long...
            termios.tcflush(sys.stdin, termios.TCIFLUSH)
            return key
        return None

    def check_rows(self):
        rows = 0
        for y, line in enumerate(self.matrix):
            if '.' not in line:
                del self.matrix[y]
                self.matrix.insert(0, ['.' for _ in range(Game.WIDTH)])
                rows += 1

        self.score += int(rows * 1.9) # 1 row - Score: 1 | 2 row - Score: 3 | 3 row - Score: 5...
        if rows > 0:
            self.update_speed()

    def update_speed(self):
        if self.score >= 50:
            return
        self.speed = Game.MIN_SPEED + (Game.INITIAL_SPEED - Game.MIN_SPEED) * ((50 - self.score) / 50)

    def new_tetromino(self):
        for point in self.player.shape:
            self.matrix[point[1]][point[0]] = 'X'
        
        self.check_rows()
        self.player = self.next
        self.next = Tetromino()
        self.last_move_down_time = time.time()

    def game_loop(self):
        key = self.check_input()
        if key:
            if key == 'q':
                self.game_over()
            if key == 'a':
                self.player.move_left(self.matrix)
            if key == 'd':
                self.player.move_right(self.matrix)
            if key == 's':
                self.player.move_down(self)
            if key == "k":
                self.player.rotate_right(self.matrix)
            if key == "l":
                self.player.rotate_left(self.matrix)
            if key == "w":
                self.player.drop(self)
            if key == "t":
                self.score += 1
                self.update_speed()
        
        if time.time() - self.last_move_down_time >= self.speed:
            moved_down = self.player.move_down(self)
            if not moved_down:
                is_game_over = False
                for point in self.player.shape:
                    if point[1] < 0:
                        is_game_over = True
                        break
                        
                if is_game_over:
                    self.game_over()
                else:    
                    self.new_tetromino()
            self.last_move_down_time = time.time()
            
        draw_frame(self)


    def game_over(self):
        self.should_quit = True        


    def run(self):
        # Set terminal to raw mode
        tty.setcbreak(sys.stdin)
        while not self.should_quit:
            self.game_loop()
            time.sleep(0.05)
        end_screen(self.score)
