"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao
--------------------------------------------
Author: Hui-Chi Yang
"""
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():

    graphics = BreakoutGraphics()

    # get dx, dy from "breakoutgraphics.py" (since they are internal use only)
    dx = graphics.get_dx()
    dy = graphics.get_dy()

    count = 0  # the number the player breaks the brick
    score = 0
    while True:
        if graphics.moving is True:
            global NUM_LIVES
            graphics.b.move(dx, dy)
            # wall rebound (except the downside wall)
            if graphics.b.x < 0 or graphics.b.x + graphics.b.width > graphics.window.width:
                dx = -dx
            if graphics.b.y < 0:
                dy = -dy
            if graphics.b.y > graphics.window.height:
                graphics.set_ball_position()
                graphics.set_ball_velocity()
                dx = graphics.get_dx()
                graphics.moving = False
                NUM_LIVES -= 1
                score -= 50
                if NUM_LIVES == 2:
                    graphics.window.remove(graphics.ball_1)
                if NUM_LIVES == 1:
                    graphics.window.remove(graphics.ball_2)
                # check if the player exceeds the limit of missing the ball from the paddle
                if NUM_LIVES <= 0:
                    graphics.window.remove(graphics.b)
                    graphics.window.remove(graphics.ball_3)
                    graphics.game_over()
                    break

            # check for ball/paddle collision
            # get the return value from collision_check (obj1234 or None)
            if graphics.collision_check() is not None:
                # obj1234 is the paddle -> change the ball's direction
                if graphics.collision_check() == graphics.p:
                    if dy > 0:
                        dy = - dy

                else:
                    # obj1234 is ball lives in the right corner -> do not change direction and reserve it
                    if graphics.collision_check().y == graphics.p_o + graphics.b.height:
                        pass

                    # obj1234 is the brick -> change the ball's direction and remove the brick
                    if graphics.collision_check().y < graphics.p_o + graphics.b.height:
                        dy = - dy
                        graphics.window.remove(graphics.collision_check())
                        count += 1
                        graphics.sum_score()
                        # break the bricks and increase player's score
                        score += 10
                        print(score)
                        # check if the player breaks all the bricks
                        if count == graphics.brick_num:
                            graphics.window.remove(graphics.b)
                            graphics.you_win()
                            break

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
