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
        self.image = pygame.image.load("xe.png")
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
        self.image = pygame.image.load("rocket1.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = random.randint(0, 10+SCREEN_WIDTH - self.width)
        self.y = -self.height
        self.speed = 5


    def update(self):
        self.y += self.speed


    def draw(self):
        screen.blit(self.image, (self.x, self.y))






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
        if random.randint(1, 40) == 1:
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
                    level = min(level + 1, 10)  # Giới hạn cấp độ tối đa là 10
                    level_music.play()
                    display_level(level)
                   
            # Check for collision
            if car.x < obstacle.x + obstacle.width and car.x + car.width > obstacle.x and car.y < obstacle.y + obstacle.height and car.y + car.height > obstacle.y:
                running = False


        # Draw car
        car.draw()


        # Display score
        font = pygame.font.Font(None, 40)
        score_text = font.render(f"SCORE: {score}", True, GREEN)
        level_text = font.render(f"LV: {level}", True, RED)
        screen.blit(score_text, (18, 7))
        screen.blit(level_text, (18, 50))


        pygame.display.flip()
        clock.tick(60)
    game_over_screen(score)


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


# Main menu function
def main_menu():
    menu_running = True


    while menu_running:
        screen.fill(WHITE)
       
        font = pygame.font.Font(None,77)
        title_text = font.render("GO THROUGH OBTACLES", True, YELLOW)
        title_text1 = font.render("GO THROUGH OBTACLES", True, BLACK)
        screen.blit(title_text1, (SCREEN_WIDTH // 1.989 - title_text1.get_width() // 2, SCREEN_HEIGHT // 2 - title_text1.get_height() // 2 - 42))
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - title_text.get_height() // 2 - 50))
       
       
        font = pygame.font.Font(None, 36)
        start_text = font.render("----Press 'SPACE' to Start----", True, BLACK)
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 - start_text.get_height() // 2 + 50))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()


        pygame.display.flip()


    pygame.quit()


if __name__ == "__main__":
    main_menu()








