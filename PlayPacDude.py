import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
FPS = 60

def DrawLevel():
  pass


def main():
  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        run = False
  pygame.quit()



if __name__ == "__main__":
  main()