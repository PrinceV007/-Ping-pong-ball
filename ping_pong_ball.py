import pygame
import sys
pygame.init()
width = 800
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong Ball")
clock = pygame.time.Clock()
paddle_width = 10
paddle_height = 60
paddle1 = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle2 = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(width // 2 - 10, height // 2 - 10, 20, 20)
ball_speed_x = 3
ball_speed_y = 3
paddle_speed = 5

def move_paddle1(up, down):
    if up:
        paddle1.y -= paddle_speed
    if down:
        paddle1.y += paddle_speed

def move_paddle2(up, down):
    if up:
        paddle2.y -= paddle_speed
    if down:
        paddle2.y += paddle_speed
