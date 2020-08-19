import pygame
from constants import *
from paddle import Paddle
from ball import Ball
from inputs import handle_input

# initialize the game engine
pygame.init()

# create new window
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Air Hockey Pong")

left_paddle = Paddle(BLACK, 20, 100)
left_paddle.rect.x = 0
left_paddle.rect.y = 200

right_paddle = Paddle(BLACK, 20, 100)
right_paddle.rect.x = 680
right_paddle.rect.y = 200

ball = Ball(WHITE, 15, 15)
ball.rect.x = 450
ball.rect.y = 200

# list containing all sprites used in game
all_sprites_list = pygame.sprite.Group()

# add to the list of objects
all_sprites_list.add(left_paddle)
all_sprites_list.add(right_paddle)
all_sprites_list.add(ball)

# loop will continues until the user clicks out of game
done = True

# clock controls how fast the screen updates
clock = pygame.time.Clock()
# initialize player scores
player1_score = 0
player2_score = 0

# main program
while done:
    # user did something
    for event in pygame.event.get():
        # if user clicks to exit
        if event.type == pygame.QUIT:
            # update we are done so we exit this loop
            done = False

    # up and down movements of paddles
    handle_input(left_paddle, right_paddle)

    all_sprites_list.update()

    # check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 690:
        player1_score += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        player2_score += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    # find collisions between the ball and paddles
    if pygame.sprite.collide_mask(ball, left_paddle) or pygame.sprite.collide_mask(ball, right_paddle):
        ball.bounce()
    # fill screen with blue
    screen.fill(LIGHT_BLUE)
    # draw the net
    pygame.draw.line(screen, WHITE, (HALF_WIDTH, 0), (HALF_WIDTH, HEIGHT), 5)
    all_sprites_list.draw(screen)

    # display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(player1_score), 1, WHITE)
    screen.blit(text, (HALF_WIDTH - 100, 10))
    text = font.render(str(player2_score), 1, WHITE)
    screen.blit(text, (HALF_WIDTH + 75, 10))

    # update the screen with what we've drawn.
    pygame.display.flip()

    # limit to 60 frames per second
    clock.tick(60)

# exit main program loop and stop game
pygame.quit()
