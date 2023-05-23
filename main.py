import pygame

import toolBox
import disaster
import display
import settings

peopleAmount=2
coconutAmount=3
boatAmount=1
medicineAmount=0
blanketAmount=0
activeSwordAmount=0
unactiveSwordAmount=0
treeAmount=0
superTreeAmount=0
spearAmount=0
netAmount=0

resourceWindowOpen=False
tradeWindowOpen=False


pygame.init()

while True:
    # set background
    screen = settings.screen
    screen.fill(display.colour("white"))

    display.background("background.png")








    buyPerson = display.button("Buy Person", settings.width*0.3225, settings.width // 4,settings.width*0.17, settings.height*0.885, (0, 0, 0))
    tradeButton= display.button("Trade", settings.width*0.3225, settings.width // 4,settings.width*0.5, settings.height*0.885, (0, 0, 0))
    doneTurn = display.button("Done", settings.width *0.3225, settings.width // 4, settings.width*0.83,settings.height *0.885, (0, 0, 0))

    if resourceWindowOpen:
        #resource window
        window = display.rect((165,85,25), settings.width*0.5, settings.height*0.5, settings.width * 0.96, settings.height*0.96, 0)
        display.rect((0,0,0), settings.width*0.5, settings.height*0.5, settings.width * 0.96, settings.height*0.96, settings.width//400)
        #display resource quantities
        toolBox.resourcesForWindow(boatAmount,blanketAmount,medicineAmount,activeSwordAmount,unactiveSwordAmount,treeAmount,superTreeAmount,spearAmount,netAmount)
    else:
        #display button for the resource window
        resourceButton=display.button("Check Resources", settings.width *0.3225, settings.width//5, settings.width*0.83, settings.height*0.125, (0,0,0))

    if tradeWindowOpen:
        toolBox.tradeButtons(peopleAmount,coconutAmount,boatAmount,medicineAmount,blanketAmount,activeSwordAmount+unactiveSwordAmount,treeAmount,superTreeAmount)



    display.text(f"People: {peopleAmount}", settings.width // 20, settings.width // 6.5, settings.height // 12, (0, 0, 0))
    display.text(f"Coconut: {coconutAmount}", settings.width // 20, settings.width // 6.5, settings.height // 6.75,(0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buyPerson.collidepoint(event.pos):
                peopleAmount,coconutAmount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount=toolBox.buyPerson(peopleAmount,coconutAmount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount)
            elif doneTurn.collidepoint(event.pos):
                #peopleAmount,coconutAmount=disaster.randomDisaster(peopleAmount,coconutAmount,boatAmount,blanketAmount,activeSwordAmount+unactiveSwordAmount,treeAmount,superTreeAmount)
                peopleAmount,coconutAmount=toolBox.feed(peopleAmount,coconutAmount)
            elif resourceWindowOpen==False and resourceButton.collidepoint(event.pos):
                resourceWindowOpen=True
            elif resourceWindowOpen or tradeWindowOpen and window.collidepoint(event.pos)==False:
                resourceWindowOpen=False
                tradeWindowOpen=False
            elif tradeWindowOpen==False and tradeButton.collidepoint(event.pos):
                tradeWindowOpen=True


    pygame.display.flip()
