from pygame import *



FPS = 60
game = True
win_w = 1100
win_h = 700

player_size_w = 20
player_size_h = 200
ball_size = 50
ball_speed = 3

font.init()
main_win = display.set_mode((win_w,win_h))
display.set_caption('пинпонг')
clock = time.Clock()
background = transform.scale(image.load('fon.jpg'),(win_w,win_h))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        main_win.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y <= win_h - player_size_h:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y <= win_h - player_size_h:
            self.rect.y += self.speed



class Ball(GameSprite):
    def __init__(self,player_image,player_x,player_y,player_speed,w,h):
        super().__init__(player_image,player_x,player_y,player_speed,w,h)
        self.speed_x = self.speed
        self.speed_y = self.speed
    def update_ball(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.bottom > win_h:
            self.speed_y *= -1












ball = Ball('ball.png',275,525,ball_speed,ball_size,ball_size)
player_l = Player('racket.png',40,250,5,player_size_w,player_size_h)
player_r = Player('racket.png',1040,250,5,player_size_w,player_size_h)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.collide_rect(player_l,ball) or sprite.collide_rect(player_r,ball):
        ball.speed_x *= -1

    main_win.blit(background,(0,0))
    player_l.reset()
    player_l.update_l()
    player_r.reset()
    player_r.update_r()
    ball.reset()
    ball.update_ball()



    display.update()
    clock.tick(FPS)
