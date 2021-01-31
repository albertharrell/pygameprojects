import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("DEMO")

# Set up sprites
paddle_rect = [300, 500, 50, 20]
paddle_color = (250, 0, 0)

ball_rect = [150, 150, 20, 20]
ball_color = (250, 250, 0)
ball_velocity = [10, 10]

brick_color = (250, 50, 0)
bricks = []

gameover = False
clock = pygame.time.Clock()


# Start game loop
while not gameover:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameover == True

#Keys that you can hold down:
keys = pygame.key.get_pressed()
if keys[pygame.K_m]:
    paddle_rect[0] += 5

#Actions that happen
#Move
ball_rect[0] += ball_velocity[0]
ball_rect[1] += ball_velocity[1]

if ball_rect[1] > 580:
    ball_velocity[1] = -10

#Handle collisions
if paddle_rect.colliderect(ball_rect):
    ball_velocity[1] *= -1

#clear the screen
screen.fill((0,0,0))

#Draw stuff
pygame.draw.ellipse(screen, ball_color, ball_rect)
pygame.draw.rect(screen, paddle_color, paddle_rect)

#Create the bricks
for row in range(3):
    for col in range(10):
        brick = pygame.Rect(col * 80 + 10, row * 40 + 60, 60, 20)
        bricks.append(brick)

#draw the bricks
for brink in bricks:
    pygame.draw.rect(screen, brick_color, brick)

#Delete bricks on collision
for brick in bricks.copy():
    if ball_rect.colliderect(brick):
        bricks.remove(brick)
        ball_velocity[1] *= -1

#Configure Score
font = pygame.font.SysFont(None, 72)
score_text = font.render(str(len(bricks)), True, (250,250,0))
screen.blit(score_text, (700,10))

#Show the new screen
pygame.display.flip()

pygame.quit()