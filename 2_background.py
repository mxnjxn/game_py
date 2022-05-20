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

# event loop --> enables the tabs( event loop이 있어야 창이 꺼지지 않는다.)--> 사용자의 동작을 검사함.
running = True  # 게임이 진행중인가?
while running:
    # pygame 을 쓰기 위해 무조건 ㄴ써야하는 내용 pygame.event.get(event.type)
    for event in pygame.event.get():  # 어떤 이벤트가 발생 하였는가?? 사용자가 키보드를 클릭하는지 ...등등 체크
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가??
            running = False  # 게임이 진행중이 아님
    screen.blit(background, (0, 0))  # 배경 그리기

    # screen.fill(0,0,0) --> rgb 값을 넣어서 배경색 그리기
    pygame.display.update()  # 개인화면을 다시 그리기 ( pygame 에서는 매 프레임마다 그려줘야 함.)
    # pygame 종료
pygame.quit()
