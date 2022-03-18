from pygame import *

win_largo=700
win_ancho=500

class GameSprite(sprite.Sprite):
    def __init__(self, ima, x, y, v, a, l):
        super().__init__()
        self.image=transform.scale(image.load(ima), (a, l))
        self.speed=v
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.n=0
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class pelota(GameSprite):
    def __init__(self, ima, x, y, v, a, l):
        super().__init__(ima, x, y, v, a, l)

class pala(GameSprite):
    def __init__(self, ima, x, y, v, a, l):
        super().__init__(ima, x, y, v, a, l)
    def update_izq(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]and self.rect.y>40:
            self.rect.y -= self.speed
        if keys_pressed[K_s]and self.rect.y<360:
            self.rect.y += self.speed
        window.blit(self.image,(self.rect.x,self.rect.y))
    def update_der(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]and self.rect.y>40:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]and self.rect.y<360:
            self.rect.y += self.speed
        window.blit(self.image,(self.rect.x,self.rect.y))
            

window = display.set_mode((win_largo, win_ancho))
display.set_caption("Ping-Pong")
background=transform.scale(image.load("fond_campo.jpg"), (win_largo,win_ancho))
jugador_1 = pala("fond_azul.png", 70, 200, 2, 10, 100)
jugador_2 = pala("fond_rojo.png", 625, 200, 2, 10, 100)
pelota = pelota("pelota.png",320, 230, 1, 40, 40 )

speed_x=1
speed_y=1
game = True
finish=False
while game:
    window.blit(background,(0, 0))
    jugador_1.update_izq()
    jugador_2.update_der()
    
    pelota.rect.y+=speed_y
    pelota.rect.x+=speed_x
    if pelota.rect.y==430 or pelota.rect.y==40:
        speed_y *= -1
    if sprite.collide_rect(jugador_1, pelota) or sprite.collide_rect(jugador_2, pelota):
        speed_x *= -1
    
    pelota.reset()
    for e in event.get():
        if e.type == QUIT:
            game=False
    display.update()