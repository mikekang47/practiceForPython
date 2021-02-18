import pygame

pygame.init() #반드시 호출

#화면 크기 설정

screen_width = 480
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Demo game")

background = pygame.image.load("/Users/mikekang/work/practiceForPython/pygame_basic/background.png")

character = pygame.image.load("/Users/mikekang/work/practiceForPython/pygame_basic/character.jpg")
character_size = character.get_rect().size #이미지 크기 구해옴
character_width = character_size[0] #캐릭터 가로크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = (screen_width  / 2) - (character_width / 2) #화면 가로 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height



running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하면
           running = False #게임이 끝남
   screen.blit(background, (0,0))

   screen.blit(character, (character_x_pos, character_y_pos))

   pygame.display.update()



pygame.quit()
