import pygame

#system:
pygame.init()
screen = pygame.display.set_mode((1980, 1080))
clock = pygame.time.Clock()

#Player:
class Player:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.size = 20
        self.speed = 1
run = True
player = Player()
while run:
    pygame.display.update() #update

    screen.fill((34, 139, 34)) #fon

    clock.tick(60)

    pygame.draw.circle(screen, "Blue", (player.x, player.y), player.size) #draw player

    #player control:
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        player.y -= player.speed
    if key[pygame.K_DOWN]:
        player.y += player.speed
    if key[pygame.K_RIGHT]:
        player.x += player.speed
    if key[pygame.K_LEFT]:
        player.x -= player.speed

    #Quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

