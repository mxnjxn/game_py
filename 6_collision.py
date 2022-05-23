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

# FPS (Frame Per Second)
clock = pygame.time.Clock()

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

# 이동속도
character_speed = 0.6

# enemy 캐릭터
enemy = pygame.image.load(
    r"C:\python_workspace\python_application\game_py\enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴(가로, 세로)
enemy_width = enemy_size[0]  # character_size의 첫번째 값.
enemy_height = enemy_size[1]  # character_size의 두번째 값.
enemy_x_pos = screen_width/2 - enemy_width/2  # 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = screen_height/2 - enemy_height/2  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# event loop --> enables the tabs( event loop이 있어야 창이 꺼지지 않는다.)--> 사용자의 동작을 검사함.
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(60)  # dt --> delta  ()--> 안에 원하는 초당 프레임 수 넣기

    # 캐릭터가  100 만큼 이동을 해야함
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 10만큼 이동해야 함
    # 20 fps : 1초 동안에 20 번 동장 -> 1번에 5만큼 이동해야 함

    # ** print("fps : " + str(clock.get_fps()))  # ___.get_fps()

    # pygame 을 쓰기 위해 무조건 ㄴ써야하는 내용 pygame.event.get(event.type)
    for event in pygame.event.get():  # 어떤 이벤트가 발생 하였는가?? 사용자가 키보드를 클릭하는지 ...등등 체크
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가??
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                # pass  # 실행코드가 없는것으로 다음 행동을 계속해서 진행시킨다.
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                # to_x += 0 --> to_x = to_x --> 가던 발향으로 쭉 감.
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                # to_y += 0

# 프레임에 따라 캐릭터의 속도가 달라지지 않게 보정이 필요함
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

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

    # 충돌 처리를 위한 rect 정보 업데이트
    # 캐릭터 좌표와 크기 정보 --> 캐릭터 자체 이미지의 rect 정보는 항상 똑같은 곳을 가리키고 있다.
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    # 업데이트 안하면 enemy_x,y 에 대한 포지션이 rect에 들어가있지 아니하게 된다. 기본 height, width만 들어가 있다?
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 했어요.")
        running = False

    screen.blit(background, (0, 0))  # 배경 그리기 (좌표 설정)

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    # screen.fill(0,0,0) --> rgb 값을 넣어서 배경색 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

    pygame.display.update()  # 개인화면을 다시 그리기 ( pygame 에서는 매 프레임마다 그려줘야 함.)
# pygame 종료
pygame.quit()
