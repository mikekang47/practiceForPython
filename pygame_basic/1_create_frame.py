import pygame

pygame.init() #반드시 호출

#화면 크기 설정

screen_width = 480
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Demo game")

running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하면
           running = False #게임이 끝남


pygame.quit()
