import pygame
import random
from sys import exit

pygame.init()
pygame.mixer.init()

# Music
background_music = "background.mp3"  # Đường dẫn đến nhạc nền
game_over_music = "gameover.mp3"     # Đường dẫn đến nhạc game over
traffic_music="traffic.mp3"
level_music= pygame.mixer.Sound("thangcap.mp3")
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1)  # -1 để phát lặp vô hạn
pygame.mixer.music.set_volume(0.5)
level_music.set_volume(3)
pygame.mixer.music.set_volume(0.21234)


# Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 720

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW=(250,172,2)
PINK=(252,3,227)

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GROUP 5")

# PICTURE
car_img = pygame.Surface((50, 100))
car_img.fill(GREEN)
obstacle_img = pygame.Surface((55, 100))
obstacle_img.fill(RED)


def display_level(level):
    font = pygame.font.Font(None, 200)
    for _ in range(6):  # Hiển thị nhấp nháy 6 lần
        # Xóa màn hình (chỉ cần phần giữa màn hình)
        # pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        
        # Hiển thị level
        level_text = font.render(f"LEVEL {level}", True, PINK if _ % 2 == 0 else WHITE)
        screen.blit(
            level_text,
            (SCREEN_WIDTH // 2 - level_text.get_width() // 2, SCREEN_HEIGHT // 2 - level_text.get_height() // 2),
        )
        pygame.display.flip()
        pygame.time.delay(250)  # Chờ 300ms



# Car class
class Car:
    def __init__(self):
        global selected_car_index
        self.image = pygame.image.load(car_images[selected_car_index][0])
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = 8.5
    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
    def move_right(self):
        if self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        
    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y < SCREEN_HEIGHT - self.height:
            self.y += self.speed
    
# Obstacle class
class Obstacle:
    def __init__(self):
        self.obstacle_images = [
            pygame.image.load("rocket1.png"),
            pygame.image.load("obstacle1.png"),
            pygame.image.load("obstacle2.png"),
            pygame.image.load("obstacle3.png"),
            pygame.image.load("obstacle4.png"),
        ]
    
        self.image = random.choice(self.obstacle_images)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = random.randint(0, 10+SCREEN_WIDTH - self.width)
        self.y = -self.height
        self.speed = random.randint(6, 12)

    def update(self):
        self.y += self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    
car_images = [
    ("xe1.png", pygame.image.load("xe1.png")),  # Hình ảnh xe 1
    ("xe2.png", pygame.image.load("xe2.png")),  # Hình ảnh xe 2
    ("xe3.png", pygame.image.load("xe3.png")),  # Hình ảnh xe 3
    ("xe4.png", pygame.image.load("xe4.png"))   # Hình ảnh xe 4
]
selected_car_index = 0  # Xe mặc định là xe đầu tiên




# Main game
def game():
    pygame.mixer.music.load(traffic_music)
    pygame.mixer.music.play(-1)  # -1 để phát lặp vô hạn

    running = True
    clock = pygame.time.Clock()
    car = Car()
    obstacles = []
    score = 0
    
    # 
    level = 1  # Bắt đầu từ level 1
    obstacle_speed_increment = 1  # Tăng tốc độ mỗi cấp độ
    

    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False



    # Load the image
    background_img = pygame.image.load("thongdiep.png")
    background_img = pygame.transform.scale(background_img, (800, 120))
    while running:
        screen.fill(BLACK)
        # Draw the image at (0, 600)
        screen.blit(background_img, (0, 600))
        # pygame.draw.rect(screen, WHITE, (0,600,800,120))
        pygame.draw.rect(screen, WHITE, (0,0,10,600))
        pygame.draw.rect(screen, YELLOW, (95,50-10,20,85))
        pygame.draw.rect(screen, YELLOW, (95,200-10,20,85))
        pygame.draw.rect(screen, YELLOW, (95,350-10,20,85))
        pygame.draw.rect(screen, YELLOW, (95,500-10,20,85))
        pygame.draw.rect(screen, WHITE, (200,0,10,600))
        pygame.draw.rect(screen, YELLOW, (305-10,50-10,20,85))
        pygame.draw.rect(screen, YELLOW, (305-10,200-10,20,85))
        pygame.draw.rect(screen, YELLOW, (305-10,350-10,20,85))
        pygame.draw.rect(screen, YELLOW, (305-10,500-10,20,85))
        pygame.draw.rect(screen, WHITE, (400,0,10,600))
        pygame.draw.rect(screen, YELLOW, (505-10,50-10,20,85))
        pygame.draw.rect(screen, YELLOW, (505-10,200-10,20,85))
        pygame.draw.rect(screen, YELLOW, (505-10,350-10,20,85))
        pygame.draw.rect(screen, YELLOW, (505-10,500-10,20,85))
        pygame.draw.rect(screen, WHITE, (600,0,10,600))
        pygame.draw.rect(screen, YELLOW, (690,50-10,20,85))
        pygame.draw.rect(screen, YELLOW, (690,200-10,20,85))
        pygame.draw.rect(screen, YELLOW, (690,350-10,20,85))
        pygame.draw.rect(screen, YELLOW, (690,500-10,20,85))
        pygame.draw.rect(screen, WHITE, (790,0,10,600))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car.move_left()
                    moving_left = True
                elif event.key == pygame.K_RIGHT:
                    car.move_right()
                    moving_right = True
                elif event.key == pygame.K_UP:
                    moving_up = True
                    car.move_up()
                elif event.key == pygame.K_DOWN:
                    moving_down = True
                    car.move_down()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moving_left = False
                elif event.key == pygame.K_RIGHT:
                    moving_right = False
                elif event.key == pygame.K_UP:
                    moving_up = False
                elif event.key == pygame.K_DOWN:
                    moving_down = False
            
        if moving_left:
                car.move_left()
        if moving_right:
                car.move_right()
        if moving_up:
                car.move_up()
        if moving_down:
                car.move_down()


        # Add new obstacles
        if random.randint(1, 37) == 1:
            new_obstacle = Obstacle()
            # Tăng tốc độ dựa trên cấp độ
            new_obstacle.speed += (level - 1) * obstacle_speed_increment
            obstacles.append(new_obstacle)

        # Update and draw obstacles
        for obstacle in obstacles[:]:
            obstacle.update()
            obstacle.draw()
            if obstacle.y > SCREEN_HEIGHT:
                obstacles.remove(obstacle)
                score += 1

                 # Tăng cấp độ mỗi 10 điểm
                if score % 17 == 0:
                    level = min(level + 1, 100)  # Giới hạn cấp độ tối đa là 10
                    level_music.play()
                    display_level(level)
                    
            # Check for collision
            if car.x < obstacle.x + obstacle.width and car.x + car.width > obstacle.x and car.y < obstacle.y + obstacle.height and car.y + car.height > obstacle.y:
                running = False

        # Draw car
        car.draw()

        # Display score
        score_font=pygame.font.Font("fonts/pixelfont.ttf",35)
        font = pygame.font.Font(None, 40)
        score_text = score_font.render(f"SCORE: {score}", True, GREEN)
        level_text = score_font.render(f"LV: {level}", True, RED)
        screen.blit(score_text, (18, -1))
        screen.blit(level_text, (18, 35))

        pygame.display.flip()
        clock.tick(60)
    game_over_screen(score)

def car_selection_menu():
    global selected_car_index
    selecting = True
    arrow_offset_left = 0  # Độ lún của mũi tên trái
    arrow_offset_right = 0  # Độ lún của mũi tên phải
    arrow_press_distance = 15  # Khoảng cách lún xuống
    arrow_frames = 5  # Số frame để hiệu ứng lún xuống diễn ra

    # Tải hình ảnh mũi tên và xe
    phai_img = pygame.image.load("phai.png")
    trai_img = pygame.image.load("trai.png")

    while selecting:
        # Vẽ nền và các phần tĩnh (chỉ cần vẽ một lần)
        screen.fill(BLACK)
        font = pygame.font.Font(None, 50)
        title_fonts = pygame.font.Font("fonts/pixelfont.ttf", 70)
        title_text = title_fonts.render("CHOOSE YOUR CAR", True, GREEN)
        instructions_text = font.render("---'ENTER'---", True, YELLOW)

        # Hiển thị tiêu đề và hướng dẫn
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))
        screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, SCREEN_HEIGHT - 100))

        # Hiển thị xe hiện tại
        car_image = car_images[selected_car_index][1]
        car_image = pygame.transform.scale(car_image, (100, 200))  # Tỷ lệ xe
        screen.blit(car_image, (SCREEN_WIDTH // 2 - car_image.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        # Vẽ mũi tên với độ lún
        screen.blit(trai_img, (95, 310 + arrow_offset_left))
        screen.blit(phai_img, (600, 310 + arrow_offset_right))

        # Lắng nghe sự kiện bàn phím
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Chuyển sang xe trước đó và lún mũi tên trái
                    selected_car_index = (selected_car_index - 1) % len(car_images)
                    for frame in range(arrow_frames):
                        arrow_offset_left = arrow_press_distance // (frame + 1)
                        screen.fill(BLACK)
                        # Vẽ lại giao diện sau khi có hiệu ứng
                        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))
                        screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, SCREEN_HEIGHT - 100))
                        screen.blit(car_image, (SCREEN_WIDTH // 2 - car_image.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
                        screen.blit(trai_img, (95, 310 + arrow_offset_left))
                        screen.blit(phai_img, (600, 310 + arrow_offset_right))
                        pygame.display.flip()
                        pygame.time.delay(10)
                    arrow_offset_left = 0

                elif event.key == pygame.K_RIGHT:  # Chuyển sang xe tiếp theo và lún mũi tên phải
                    selected_car_index = (selected_car_index + 1) % len(car_images)
                    for frame in range(arrow_frames):
                        arrow_offset_right = arrow_press_distance // (frame + 1)
                        screen.fill(BLACK)
                        # Vẽ lại giao diện sau khi có hiệu ứng
                        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))
                        screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, SCREEN_HEIGHT - 100))
                        screen.blit(car_image, (SCREEN_WIDTH // 2 - car_image.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
                        screen.blit(trai_img, (95, 310 + arrow_offset_left))
                        screen.blit(phai_img, (600, 310 + arrow_offset_right))
                        pygame.display.flip()
                        pygame.time.delay(10)
                    arrow_offset_right = 0

                elif event.key == pygame.K_RETURN:  # Chọn xe và bắt đầu game
                    selecting = False

        pygame.display.flip()


def game_over_screen(score):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(game_over_music)
    pygame.mixer.music.play()


    screen.fill(BLACK)
    font_large = pygame.font.Font(None, 120)
    font_small = pygame.font.Font(None, 36)

    # Hiển thị "Game Over"
    game_over_text = font_large.render("GAME OVER", True, RED)
    screen.blit(
        game_over_text,
        (
            SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
            SCREEN_HEIGHT // 2 - 100,
        ),
    )

    # Hiển thị điểm số
    score_text = font_small.render(f"Your Score: {score}", True, WHITE)
    screen.blit(
        score_text,
        (
            SCREEN_WIDTH // 2 - score_text.get_width() // 2,
            SCREEN_HEIGHT // 2,
        ),
    )

    # Hướng dẫn tiếp tục
    continue_text = font_small.render("Press 'R' to Restart or 'Q' to Quit", True, WHITE)
    screen.blit(
        continue_text,
        (
            SCREEN_WIDTH // 2 - continue_text.get_width() // 2,
            SCREEN_HEIGHT // 2 + 50,
        ),
    )
    pygame.display.flip()

    # Vòng lặp chờ người chơi quyết định
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Nhấn 'R' để chơi lại
                    waiting = False
                    game()
                elif event.key == pygame.K_q:  # Nhấn 'Q' để thoát
                    pygame.quit()
                    exit()

    print(f"Game Over! Your score is {score}.")

def draw_button(text, x, y, width, height, normal_color, hover_color, text_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, normal_color, (x, y, width, height))

    font = pygame.font.Font(None, 40)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect()
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(text_surf, text_rect)

    return pygame.Rect(x, y, width, height)

def button_click_effect(button_rect, action):
    original_y = button_rect.y
    press_distance = 20
    frames = 5

    for i in range(frames):
        button_rect.y += press_distance / frames
        screen.fill(BLACK)
        # Vẽ lại các phần tử khác của menu ở đây
        pygame.draw.rect(screen, GREEN, button_rect)
        pygame.display.flip()
        pygame.time.delay(20)

    for i in range(frames):
        button_rect.y -= press_distance / frames
        screen.fill(BLACK)
        # Vẽ lại các phần tử khác của menu ở đây
        pygame.draw.rect(screen, GREEN, button_rect)
        pygame.display.flip()
        pygame.time.delay(20)

    button_rect.y = original_y
    action()

# Main menu function
def main_menu():
    menu_running = True
    start_button = None
    quit_button = None

    while menu_running:
        traffic_img = pygame.image.load("trafficlight.png")
        xenen_img = pygame.image.load("xenen.png")
        screen.fill(BLACK)
        screen.blit(xenen_img, (300,600))
        screen.blit(traffic_img, (70,550))
        screen.blit(traffic_img, (630,550))
       
        title_text = font.render("GO THROUGH OBTACLES", True, YELLOW)
        title_text1 = font.render("GO THROUGH OBTACLES", True, WHITE)
        title_y = 100  # Đặt vị trí y của tiêu đề cao hơn
        screen.blit(title_text1, (SCREEN_WIDTH // 2 - title_text1.get_width() // 2 + 2, title_y + 2))
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 1.985, title_y))

        start_button = draw_button("START", 300, 300, 200, 50, WHITE, YELLOW, BLACK)
        quit_button = draw_button("QUIT", 300, 400, 200, 50, WHITE, YELLOW, BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    button_click_effect(start_button, lambda: None)
                    pygame.time.delay(500)  # Chờ 1 giây
                    car_selection_menu()
                    game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if start_button.collidepoint(event.pos):
                        button_click_effect(start_button, lambda: None)
                        pygame.time.delay(500)  # Chờ 1 giây
                        car_selection_menu()
                        game()
                    elif quit_button.collidepoint(event.pos):
                        button_click_effect(quit_button, lambda: None)
                        pygame.time.delay(500)  # Chờ 1 giây
                        pygame.quit()
                        exit()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main_menu()
