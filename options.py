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

        display.text("Screen Size",settings.width*0.05,settings.width*0.5,settings.height*0.35,(0,0,0))
        display.text(str(settings.width),settings.width*0.05,settings.width*0.5,settings.height*0.5,(0,0,0))
        smallerScreenButton = display.button("<", settings.width * 0.1, settings.width * 0.25, settings.width * 0.375,settings.height * 0.5, (0, 0, 0))
        smallerScreenButtonx10 = display.button("<<", settings.width * 0.1, settings.width * 0.25, settings.width * 0.27,settings.height * 0.5, (0, 0, 0))
        smallerScreenButtonx100 = display.button("<<<", settings.width * 0.1, settings.width * 0.25, settings.width * 0.165,settings.height * 0.5, (0, 0, 0))
        biggerScreenButton = display.button(">", settings.width * 0.1, settings.width * 0.25, settings.width * 0.625,
                                             settings.height * 0.5, (0, 0, 0))
        biggerScreenButtonx10 = display.button(">>", settings.width * 0.1, settings.width * 0.25,
                                                settings.width * 0.7275, settings.height * 0.5, (0, 0, 0))
        biggerScreenButtonx100 = display.button(">>>", settings.width * 0.1, settings.width * 0.25,
                                                 settings.width * 0.83, settings.height * 0.5, (0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.collidepoint(event.pos):
                    return
                elif smallerScreenButton.collidepoint(event.pos):
                    settings.width -= 1
                    settings.changeScreenSize()

                elif smallerScreenButtonx10.collidepoint(event.pos):
                    settings.width-=10
                    settings.changeScreenSize()

                elif smallerScreenButtonx100.collidepoint(event.pos):
                    settings.width -= 100
                    settings.changeScreenSize()

                elif biggerScreenButton.collidepoint(event.pos):
                    settings.width+=1
                    settings.changeScreenSize()

                elif biggerScreenButtonx10.collidepoint(event.pos):
                    settings.width+=10
                    settings.changeScreenSize()

                elif biggerScreenButtonx100.collidepoint(event.pos):
                    settings.width+=100
                    settings.changeScreenSize()

        settings.save()
        pygame.display.flip()