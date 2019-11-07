import pygame

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
w = 1
w_dir = 1

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.draw.circle(screen, (0, w, 0), (320, 240), 50)
#     pygame.display.update()
#     w+=w_dir
#     if w ==255:
#         w_dir = -w_dir
#     if w == 0:
#         w_dir = -w_dir
#
# clock.tick(60)
screen = pygame.display.set_mode((640, 480))
a= 10
b=20
c=30
d=40
e=50
ar= 1
br=1
cr=1
dr=1
er=1
running = True
r = 0
g = 150
b = 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.circle(screen, (0, 150, 250), (50, 250), a)
    pygame.draw.circle(screen, (0, 150, 250), (150, 250), b)
    pygame.draw.circle(screen, (0, 150, 250), (250, 250), c)
    pygame.draw.circle(screen, (0, 150, 250), (350, 250), d)
    pygame.draw.circle(screen, (0, 150, 250), (450, 250), e)
    a+=ar
    if a == 50:
        ar= ar*-1
    if a == 2:
        ar = 1


    pygame.display.update()
    r = r + 1
    g = g + 1
    b = b + 1
pygame.quit()











