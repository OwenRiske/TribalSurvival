import game
import settings
import display
import pygame
import options



quitting=False
pygame.init()
while True:
    settings.screen.fill((225,225,225))
    startButton = display.button("START", settings.width * 0.3225, settings.width*0.25, settings.width * 0.5, settings.height * 0.375, (0, 0, 0))
    optionButton = display.button("OPTIONS", settings.width * 0.3225, settings.width*0.25, settings.width * 0.5, settings.height * 0.6, (0, 0, 0))
    quitButton = display.button("QUIT", settings.width * 0.3225, settings.width*0.25, settings.width * 0.5, settings.height * 0.825, (0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.collidepoint(event.pos):
                game.startGame()
            elif optionButton.collidepoint(event.pos):
                options.optionsMenu()
            elif quitButton.collidepoint(event.pos):
                quitting=True

    if quitting:
        break



    pygame.display.flip()
