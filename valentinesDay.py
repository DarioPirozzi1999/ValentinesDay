import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("valentines day card")

img=pygame.image.load(r"Games\images\valentinesBg.jpg")
img2= pygame.image.load(r"Games\images\ladybug.png")
image = pygame.transform.scale(img, (WIDTH,HEIGHT))
image2= pygame.transform.scale(img2, (WIDTH/2,HEIGHT/2))


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    font = pygame.font.SysFont("Times New Roman", 50)
    text = font.render("Happy Valentines Day", True, (255,255,255))
    text2 = font.render("LY Nourtje", True, (255,255,255))
    display_surface.blit(image, (0,0))
    display_surface.blit(image2, (100,25))
    display_surface.blit(image2, (300,450))
    display_surface.blit(text, (75,300))
    pygame.display.update()
    time.sleep(2)
    
    display_surface.blit(image, (0,0))
    display_surface.blit(text2, (150, 300))

    pygame.display.update()
    time.sleep(2)