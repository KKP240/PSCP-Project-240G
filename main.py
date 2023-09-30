import pygame
from pygame import mixer

#เรียกใช้งาน pygame, audio
pygame.init()
mixer.init()

#หน้าจอโปรแกรม
SCREEN_W = 1280
SCREEN_H = 720
pygame.display.set_mode((SCREEN_W, SCREEN_H))
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

#ขัอความและฟอนต์
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
fontcolor_mainmenu = (180, 180, 179)
sys_font = pygame.font.SysFont("capriolaregular", 108)
message_text = sys_font.render("JustType", True, fontcolor_mainmenu)

#ไอคอนและชื่อโปรแกรม
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("JustType")

#dinosaur ลอยไปมา
dinosaur_img = pygame.image.load("images/dinosaur.png")
dinosaur_img = pygame.transform.scale(dinosaur_img, (200, 300))

#ปุ่ม Start
start_button = pygame.Rect(540, 400, 200, 50)
font_button = pygame.font.SysFont("capriolaregular", 36)
text_startbutton = font_button.render("Start", True, (255, 255, 255))
text_rect = text_startbutton.get_rect(center=start_button.center)

#เสียง mainmenu audio
mixer.music.load("audio/mainmenu.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(loops=1)

flyspeed = 0
running = True
while running:
    for event in pygame.event.get():
        #กากบาทปิดจบการทำงาน
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #กด ESC ปิดจบการทำงาน
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                pass
    screen.blit(dinosaur_img, (flyspeed, 0))
    screen.blit(message_text, (420, 200))
    pygame.draw.rect(screen, (0, 128, 255), start_button)
    screen.blit(text_startbutton, text_rect)
    flyspeed += 0.2
    pygame.display.flip()
