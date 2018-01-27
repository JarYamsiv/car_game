import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30.0
y = 30.0
car = pygame.image.load('car.png')
clock=pygame.time.Clock()
BLACK=(0,0,0)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        done =True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 0.05
        if pressed[pygame.K_DOWN]: y += 0.05
        if pressed[pygame.K_LEFT]: x -= 0.05
        if pressed[pygame.K_RIGHT]: x += 0.05

        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        screen.fill(BLACK)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        pygame.display.flip()
