import pygame

#เรียกใช้งาน pygame
pygame.init()

#ขนาดหน้าจอ
SCREEN_W = 1000
SCREEN_H = 600
pygame.display.set_mode((SCREEN_W, SCREEN_H))
#สั่งให้แสดงผลหน้าจอขนาดตามที่เรากำหนด

#ไอคอนและชื่อโปรแกรม
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("JustType")

#การกดปิดจบการทำงาน
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
