import pygame

WIDTH = 700
HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("robot as sprites")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/rocket_ship.png")
        self.rect = self.image.get_rect()

    def move_player(self,keys_pressed):
        if keys_pressed[pygame.K_w]:
            self.rect.move_ip(0,-5)
        if keys_pressed[pygame.K_a]:
            self.rect.move_ip(-5,0)
        if keys_pressed[pygame.K_s]:
            self.rect.move_ip(0,5)
        if keys_pressed[pygame.K_d]:
            self.rect.move_ip(5,0)

sprite_group = pygame.sprite.Group()

def start_game():
    #creating object of our player class
    
    rocket = Player()
    #adding sprite to the group
    sprite_group.add(rocket)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        rocket.move_player(keys_pressed)
        screen.fill((255,255,255))
        sprite_group.draw(screen)
        pygame.display.update()
start_game()