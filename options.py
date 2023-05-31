import pygame
import display
import settings

def exitSquare(x,y,size, colour):
    output=display.rect(colour,x,y,size,size,0)
    display.text("x",size,x,y,(0,0,0))
    return output

def optionsMenu():

    pygame.init()

    while True:
        settings.screen.fill((250,250,250))

        exitButton=exitSquare(settings.width*0.045,settings.height*0.05,settings.width*0.05,(250,250,250))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.collidepoint(event.pos):
                    return


        pygame.display.flip()