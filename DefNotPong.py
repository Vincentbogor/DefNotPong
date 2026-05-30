import pygame
pygame.init()
pygame.font.init()
font1 = pygame.font.SysFont('Comic Sans MS', 50)
LOSE1 = font1.render('P1, You lose!', True, (255, 0, 0))
LOSE2 = font1.render('P2, You lose!', True, (0, 0, 255))

scene_len = 640
scene_hei = 360
scene_title = 'Legally distinct Pong'

bg_pic = 'galaxy.jpg'
ball_pic = 'JA Meme.jpg'
paddle_pic = 'paddle.png'
bgm = '554382_Machine-Forest.ogg'

scene = pygame.display.set_mode((scene_len, scene_hei))
scene.fill((255, 255, 255))
FPS = pygame.time.Clock()
back = pygame.transform.scale(pygame.image.load(bg_pic), (scene_len, scene_hei))

pygame.mixer.init()
pygame.mixer.music.load(bgm)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

GAME_RUN = True
GAME_FINISH = False

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, pic, x, y, len, hei, sped):
        super().__init__()
        self.len = len
        self.hei = hei
        self.image = pygame.transform.scale(pygame.image.load(pic), (self.len, self.hei))
        self.speed = sped
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        scene.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_p1(self):
        button = pygame.key.get_pressed()
        if button[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if button[pygame.K_s] and self.rect.y < scene_hei - self.hei:
            self.rect.y += self.speed
    def update_p2(self):
        button = pygame.key.get_pressed()
        if button[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if button[pygame.K_DOWN] and self.rect.y < scene_hei - self.hei:
            self.rect.y += self.speed
            
p1 = Player(paddle_pic, 10, 10, 50, 100, 20)
p2 = Player(paddle_pic, scene_len-60, 10, 50, 100, 20)
ball = GameSprite(ball_pic, scene_len/2, scene_hei/2, 50, 50, 5)
ball_sped_x = ball.speed
ball_sped_y = ball.speed

while GAME_RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUN = False
            
    if GAME_FINISH != True:
        scene.blit(back, (0, 0))
        p1.reset()
        p2.reset()
        ball.reset()
        p1.update_p1()
        p2.update_p2()
        
        ball.rect.x += ball_sped_x
        ball.rect.y += ball_sped_y
        if ball.rect.y < 0 or ball.rect.y > scene_hei-ball.hei:
            ball_sped_y *= -1
        
        if pygame.sprite.collide_rect(p1, ball) or pygame.sprite.collide_rect(p2, ball):
            ball_sped_x *= -1
            
        if ball.rect.x < 0-ball.len or ball.rect.x > scene_len:
            if ball.rect.x < 0:
                scene.blit(LOSE1, (40, 150))
            else:
                scene.blit(LOSE2, (300, 150))
            GAME_FINISH = True
        
    FPS.tick(60)
    pygame.display.update()

