# Owen Riske

import game
import settings
import display
import pygame
import options

display.pygame_present("background.png", "Tribal Survival")

# boolean for determining to if the user is quitting
quitting = False

# initiate pygame
pygame.init()

#make the main menu image the correct size
display.image_resize(f"MainMenuBackground.png", settings.width * 2, settings.height)

#loop
while True:

    #main menu background
    display.image(f"newMainMenuBackground.png", 0, 0)
    #button to start game
    startButton = display.button("START", settings.width * 0.3225, settings.width * 0.25, settings.width * 0.5,settings.height * 0.375, (0, 0, 0))
    #button to show options
    optionButton = display.button("OPTIONS", settings.width * 0.3225, settings.width * 0.25, settings.width * 0.5, settings.height * 0.6, (0, 0, 0))
    #button to quit the game
    quitButton = display.button("QUIT", settings.width * 0.3225, settings.width * 0.25, settings.width * 0.5,settings.height * 0.825, (0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            #start button clicked start game
            if startButton.collidepoint(event.pos):
                game.startGame()
            #option button clicked display option menu
            elif optionButton.collidepoint(event.pos):
                options.optionsMenu()
            #tell program that the user is quitting if quit button clicked
            elif quitButton.collidepoint(event.pos):
                quitting = True
    #if quitting exit loop
    if quitting:
        break

    pygame.display.flip()
