import pygame

pygame.init()

clock = pygame.time.Clock()
Running = True

pygame.display.set_caption("Unnamed Program")

display_width = 700
display_height = 700
# does this work
display = pygame.display.set_mode((display_width,display_height))

while Running:
    display.fill((0,0,0))
    pygame.draw.rect(display, (255,255,255), pygame.Rect(200,200,200,200),2)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            Running = False

    clock.tick(120)

pygame.quit()
quit()