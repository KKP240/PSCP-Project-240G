import pygame
from pygame import mixer

class Mainmenu:
    """MainPage"""
    def __init__(self):
        #เรียกใช้งาน pygame, audio
        pygame.init()
        mixer.init()

        #หน้าจอโปรแกรม
        self.screen_w = 1280
        self.screen_h = 720
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))

        #ขัอความและฟอนต์
        self.fontcolor_mainmenu = (247, 127, 0)
        self.sys_font = pygame.font.SysFont("capriolaregular", 108)
        self.message_text = self.sys_font.render("JustType", True, self.fontcolor_mainmenu)

        #ไอคอนและชื่อโปรแกรม
        self.icon = pygame.image.load("images/icon.png")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("JustType")

        #background image
        self.background_image = pygame.image.load("images/gamebackground.jpg")

        #ตัว cartoon วิ่ง
        self.cartoon_img = pygame.image.load("images/cartoon.png")
        self.cartoon_img = pygame.transform.scale(self.cartoon_img, (100, 100))

        #ปุ่ม Start
        self.start_button = pygame.Rect(540, 380, 200, 50)
        self.font_button = pygame.font.SysFont("capriolaregular", 36)
        self.text_startbutton = self.font_button.render("Start", True, (255, 255, 255))
        self.text_rect = self.text_startbutton.get_rect(center=self.start_button.center)

        #เสียง mainmenu audio
        mixer.music.load("audio/mainmenu.mp3")
        mixer.music.set_volume(0.3)
        mixer.music.play(loops=1)

        self.runspeed = 0
        self.running = True

    def runprogram(self):
        """runprogram"""
        while self.running:
            for event in pygame.event.get():
                #กากบาทปิดจบการทำงาน
                if event.type == pygame.QUIT:
                    self.running = False
                #กด ESC ปิดจบการทำงาน
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.start_button.collidepoint(event.pos):
                        nextpage = Typingpage()
                        nextpage.runprogram()

            self.screen.blit(self.background_image, (-100,-200))
            self.screen.blit(self.cartoon_img, (self.runspeed, (self.screen_h)-130))
            self.screen.blit(self.message_text, (420, 180))
            pygame.draw.rect(self.screen, (0, 128, 255), self.start_button)
            self.screen.blit(self.text_startbutton, self.text_rect)
            self.runspeed += 0.18
            pygame.display.flip()
        pygame.quit()

class Typingpage:
    """TypingTestPage"""
    def __init__(self):
        pygame.init()

        #หน้าจอโปรแกรม
        self.screen_w = 1280
        self.screen_h = 720
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))

        #ขัอความและฟอนต์
        self.fontcolor_mainmenu = (180, 180, 179)
        self.sys_font = pygame.font.SysFont("capriolaregular", 108)
        self.message_text = self.sys_font.render("JustType", True, self.fontcolor_mainmenu)

        #ไอคอนและชื่อโปรแกรม
        self.icon = pygame.image.load("images/icon.png")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("JustType")

        self.running = True

    def runprogram(self):
        """runprogram"""
        while self.running:
            for event in pygame.event.get():
                #กากบาทปิดจบการทำงาน
                if event.type == pygame.QUIT:
                    self.running = False
                #กด ESC ปิดจบการทำงาน
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.screen.blit(self.message_text, (420, 200))
            pygame.display.flip()
            mixer.music.stop()
        pygame.quit()

if __name__ == "__main__":
    game = Mainmenu()
    game.runprogram()
