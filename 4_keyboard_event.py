import pygame

pygame.init()  # 초기화 하는 작업(반드시 필요)
#  pygame.font.init() --> initializing speicific modules in pygame.

# 화면 크기 설정
screen_width = 1920
screen_height = 1020

# set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
# initialize a window or screen for display
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("My first Game")  # 게임 이름

# 배경이미지 불러오기
background = pygame.image.load(
    r"C:\python_workspace\python_application\game_py\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    r"C:\python_workspace\python_application\game_py\character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴(가로, 세로)
character_width = character_size[0]  # character_size의 첫번째 값.
character_height = character_size[1]  # character_size의 두번째 값.
character_x_pos = screen_width/2 - character_width/2  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# event loop --> enables the tabs( event loop이 있어야 창이 꺼지지 않는다.)--> 사용자의 동작을 검사함.
running = True  # 게임이 진행중인가?
while running:
    # pygame 을 쓰기 위해 무조건 ㄴ써야하는 내용 pygame.event.get(event.type)
    for event in pygame.event.get():  # 어떤 이벤트가 발생 하였는가?? 사용자가 키보드를 클릭하는지 ...등등 체크
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가??
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                # pass  # 실행코드가 없는것으로 다음 행동을 계속해서 진행시킨다.
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                # to_x += 0 --> to_x = to_x --> 가던 발향으로 쭉 감.
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                # to_y += 0

    character_x_pos += to_x
    character_y_pos += to_y
'''

# 가로 경계값 처리 1
    if character_x_pos < 0:
        character_x_pos = 0

    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

# 세로 경계값 처리 2
    if character_y_pos > screen_height-character_height:
        character_y_pos = screen_height-character_height

    elif character_y_pos < 0:
        character_y_pos = 0
'''

'''
        # 가로 경계값 처리 1
    if character_x_pos< 0 :
        character_x_pos = 0
    
    elif character_x_pos > screen_width - character_width  :
        character_x_pos = screen_width - character_width

# 세로 경계값 처리 2
    if character_y_pos > screen_height-character_height: 
        character_y_pos = screen_height-character_height

    elif character_y_pos < 0:
        character_y_pos = 0
'''

screen.blit(background, (0, 0))  # 배경 그리기

screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
# screen.fill(0,0,0) --> rgb 값을 넣어서 배경색 그리기
pygame.display.update()  # 개인화면을 다시 그리기 ( pygame 에서는 매 프레임마다 그려줘야 함.)
# pygame 종료
pygame.quit()
