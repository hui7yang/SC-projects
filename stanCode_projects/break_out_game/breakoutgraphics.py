"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao
--------------------------------------------
Author: Hui-Chi Yang
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10      # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 5.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        self.brick_num = brick_rows*brick_cols

        # Create a paddle.
        self.paddle_w = paddle_width
        self.p = GRect(paddle_width, paddle_height)
        self.p_o = self.window.height-paddle_offset
        self.p.x = (self.window.width-self.p.width)/2
        self.p.y = self.p_o
        self.p.filled = True
        self.window.add(self.p)

        # Center a filled ball in the graphical window.
        self.b_r = ball_radius
        self.b = GOval(2*ball_radius, 2*ball_radius)
        self.b.filled = True
        self.b.fill_color = 'gold'
        self.b.color = 'gold'
        self.set_ball_position()
        self.window.add(self.b)

        # inform the player to click to start this game
        self.label_start = GLabel('C L I C K   T O   S T A R T')
        self.label_start.x = (self.window.width - self.label_start.width) / 2 - 45
        self.label_start.y = 600
        self.label_start.color = 'orangered'
        self.label_start.font = 'courier-15'
        self.window.add(self.label_start)

        # add "score" to this game
        self.score = 0
        self.score_name = GLabel('SCORE / ')
        self.score_name.x = 10
        self.score_name.y = self.p_o + self.b.height + self.b.height

        self.score_name.font = 'courier-12'
        self.window.add(self.score_name)

        # Default initial velocity for the ball.
        self.__dx = random.randint(0, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        self.set_ball_velocity()

        # Initialize our mouse listeners.
        onmousemoved(self.move_paddle)
        onmouseclicked(self.ball_drop)

        self.moving = False

        # Ball life
        self.ball_1 = GOval(self.b_r * 2 - 5, self.b_r * 2 - 5, x=self.window.width - self.window.width * 1 / 6, y=self.p_o + self.b.height)
        self.ball_1.filled = True
        self.ball_1.color = 'gold'
        self.ball_1.fill_color = 'gold'
        self.window.add(self.ball_1)

        self.ball_2 = GOval(self.b_r * 2 - 5, self.b_r * 2 - 5, x=self.ball_1.x + 20, y=self.p_o + self.b.height)
        self.ball_2.filled = True
        self.ball_2.color = 'gold'
        self.ball_2.fill_color = 'gold'
        self.window.add(self.ball_2)

        self.ball_3 = GOval(self.b_r * 2 - 5, self.b_r * 2 - 5, x=self.ball_2.x + 20, y=self.p_o + self.b.height)
        self.ball_3.filled = True
        self.ball_3.color = 'gold'
        self.ball_3.fill_color = 'gold'
        self.window.add(self.ball_3)

        # Draw bricks.
        start_x = 0
        start_y = 0
        for j in range(brick_rows):
            for i in range(brick_cols):
                brick = GRect(brick_width, brick_height, x=start_x, y=start_y+brick_offset)
                if j < (brick_rows/5):
                    brick.filled = True
                    brick.fill_color = 'mediumvioletred'
                    brick.color = 'mediumvioletred'
                    self.window.add(brick)
                    start_x = brick.x + brick_width + brick_spacing
                elif (brick_rows/5) <= j < (brick_rows/5)*2:
                    brick.filled = True
                    brick.fill_color = 'crimson'
                    brick.color = 'crimson'
                    self.window.add(brick)
                    start_x = brick.x + brick_width + brick_spacing
                elif (brick_rows/5)*2 <= j < (brick_rows/5)*3:
                    brick.filled = True
                    brick.fill_color = 'orangered'
                    brick.color = 'orangered'
                    self.window.add(brick)
                    start_x = brick.x + brick_width + brick_spacing
                elif (brick_rows/5)*3 <= j < (brick_rows/5)*4:
                    brick.filled = True
                    brick.fill_color = 'darkorange'
                    brick.color = 'darkorange'
                    self.window.add(brick)
                    start_x = brick.x + brick_width + brick_spacing
                else:
                    brick.filled = True
                    brick.fill_color = 'orange'
                    brick.color = 'orange'
                    self.window.add(brick)
                    start_x = brick.x + brick_width + brick_spacing
            start_y += brick_height + brick_spacing
            start_x = 0
    '''
    def elongate(self):
        self.p = GRect(self.p.width+10, self.p.height)
        self.p.filled = True
        self.p.fill_color = 'gold'
        self.p.color = 'gold'
        #self.window.remove(self.p)
        #self.window.add(self.p)
        #self.window.remove()
    '''
    # add score
    def sum_score(self):
        self.score += 10
        self.score_name.text = 'SCORE / ' + str(self.score)

    # check object collision using the ball's four coordinates
    def collision_check(self):
        obj1 = self.window.get_object_at(self.b.x, self.b.y)
        obj2 = self.window.get_object_at(self.b.x, self.b.y + self.b_r * 2)
        obj3 = self.window.get_object_at(self.b.x + self.b_r * 2, self.b.y)
        obj4 = self.window.get_object_at(self.b.x + self.b_r * 2, self.b.y + self.b_r * 2)

        if obj1 is not None:  # there is something at obj1 -> collide
            return obj1  # return obj1 to the "collision_check" function -> go to "breakout.py" and see how it works
        elif obj2 is not None:
            return obj2
        elif obj3 is not None:
            return obj3
        elif obj4 is not None:
            return obj4
        else:
            return None

    # the ball drops when the mouse clicked
    # but if the ball drops exceed the limit (game over), it won't drop again
    # have the ability to sense if the game is already started = double clicked does no effect during the game
    def ball_drop(self, event):
        self.moving = True
        self.set_ball_velocity()
        self.window.remove(self.label_start)

    # getter for dx
    def get_dx(self):
        return self.__dx

    # getter for dy
    def get_dy(self):
        return self.__dy

    # define the ball's velocity
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # when the mouse moves, the paddle moves
    def move_paddle(self, mouse):
        # mouse always set at a fixed height(paddle offset)
        self.p.y = self.p_o
        # mouse drags out of the window(left)
        if mouse.x - self.p.width/2 < 0:
            self.p.x = 0
        # mouse drags out of the window(right)
        elif mouse.x + self.p.width/2 > self.window.width:
            self.p.x = self.window.width - self.p.width
        # mouse drags inside the window
        else:
            self.p.x = mouse.x - self.p.width/2

    # the ball's initial position and game reset position
    def set_ball_position(self):
        self.b.x = (self.window.width-self.b.width)/2
        self.b.y = (self.window.height-self.b.height)/2

    # show game over if the ball falls out (NUM_LIVES) times
    def game_over(self):
        label = GLabel('G A M E   O V E R')
        label.x = (self.window.width-label.width)/2-23
        label.y = self.window.height/2
        label.font = 'courier-15-bold'
        # self.window.remove(self.brick)
        self.window.add(label)

    def you_win(self):
        label = GLabel('Y O U   W I N !')
        label.x = (self.window.width-label.width)/2-25
        label.y = self.window.height/2
        label.font = 'courier-15-bold'
        self.window.add(label)




