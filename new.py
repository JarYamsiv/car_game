import pygame,sys,math

pygame.init()
WIDTH=1024
HEIGHT=768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
is_blue = True
x = 30.0
y = 30.0
clock=pygame.time.Clock()
BLACK=(0,0,0)

class CAR(object):
    def __init__(self,position_initial):
        self.x=position_initial[0]
        self.y=position_initial[1]
        self.vx=0.0
        self.vy=0.0
        self.position=(x,y)
        self.angle=0.0
        self.v=0.0
        self.color=(255,0,10)
        self.car_body_original=pygame.image.load('car.png')
        self.car_body=self.car_body_original.copy()
    def update(self):
        if self.vx>0:
            self.vx-=0.075
        if self.vx<0:
            self.vx+=0.075
        if self.vx<0.1 and self.vx>-0.1:
            self.vx=0.0
        if self.x+self.vx<WIDTH-60 and self.x+self.vx>0:
            self.x+=self.vx
        else:
            self.vx=-1*self.vx

        self.car_body=pygame.transform.rotate(self.car_body_original,self.angle)

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, 60, 60))

    def get_inp(self,keys):
        if keys[pygame.K_UP]:
            if self.vx<10:
                self.vx+=0.5
        if keys[pygame.K_DOWN]:
            if self.vx>-10:
                self.vx-=0.5


if __name__=="__main__":
    bmw=CAR((100,100))
    while not done:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                #is_blue = not is_blue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        pressed = pygame.key.get_pressed()
        bmw.get_inp(pressed)
        bmw.update()
        screen.fill(BLACK)
        bmw.draw(screen)
        pygame.display.flip()
