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

pygame.init()

while True:
    # set background
    screen = settings.screen
    screen.fill(display.colour("white"))

    display.background("background.png")








    buyPerson = display.button("Buy Person", settings.width // 2.4, settings.width // 3,
                               settings.width - settings.width // 1.3, settings.height // 1.2, (0, 0, 0))
    doneTurn = display.button("Done", settings.width // 2.4, settings.width // 3, settings.width // 1.3,
                              settings.height // 1.2, (0, 0, 0))

    if resourceWindowOpen:
        resourceWindow = display.rect((165,85,25), settings.width // 2, settings.height // 2, settings.width - settings.width // 25, settings.height - settings.height // 25, 0)
        display.text(f"Boats: {boatAmount}", settings.width // 20, settings.width-settings.width//6.5, settings.height // 12,(255, 255, 255))
        display.text(f"Blankets: {blanketAmount}", settings.width // 20, settings.width-settings.width // 5.3, settings.height // 6.75,(255, 255, 255))
        display.text(f"Medicines: {medicineAmount}", settings.width // 20, settings.width-settings.width // 5, settings.height // 4.75,(255, 255, 255))
        display.text(f"Unused Swords: {activeSwordAmount}", settings.width // 20, settings.width-settings.width // 3.75, settings.height // 3.7,(255, 255, 255))
        display.text(f"Used Swords: {unactiveSwordAmount}", settings.width // 20, settings.width-settings.width // 4.25, settings.height // 3,(255, 255, 255))
        display.text(f"Coconut Trees: {treeAmount}", settings.width // 20, settings.width-settings.width // 4, settings.height // 2.5,(255, 255, 255))
        display.text(f"Super Coconut Trees: {superTreeAmount}", settings.width // 20, settings.width-settings.width // 3, settings.height // 2.15,(255, 255, 255))
        display.text(f"Spears: {spearAmount}", settings.width // 20, settings.width-settings.width // 6, settings.height //1.9,(255, 255, 255))
        display.text(f"Nets: {netAmount}", settings.width // 20, settings.width-settings.width // 7.5, settings.height // 1.675,(255, 255, 255))





    else:
        resourceButton=display.button("Check Resources", settings.width//2.5,settings.width//5,settings.width//1.255, settings.height//7, (0,0,0))

    display.text(f"People: {peopleAmount}", settings.width // 20, settings.width // 6.5, settings.height // 12, (0, 0, 0))
    display.text(f"Coconut: {coconutAmount}", settings.width // 20, settings.width // 6.5, settings.height // 6.75,(0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buyPerson.collidepoint(event.pos):
                peopleAmount,coconutAmount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount=toolBox.buyPerson(peopleAmount,coconutAmount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount)
            elif doneTurn.collidepoint(event.pos):
                peopleAmount,coconutAmount=disaster.randomDisaster(peopleAmount,coconutAmount,boatAmount,blanketAmount,activeSwordAmount+unactiveSwordAmount,treeAmount,superTreeAmount)
                peopleAmount,coconutAmount=toolBox.feed(peopleAmount,coconutAmount)
            elif resourceWindowOpen==False and resourceButton.collidepoint(event.pos):
                resourceWindowOpen=True
            elif resourceWindowOpen and resourceWindow.collidepoint(event.pos)==False:
                resourceWindowOpen=False
                print("hello")

    pygame.display.flip()
