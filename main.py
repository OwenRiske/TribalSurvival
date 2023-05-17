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

pygame.init()

while True:
    # set background
    screen = settings.screen
    screen.fill(display.colour("white"))

    display.background("background.png")


    display.image(f"image/newbackground.png", 0, 0)



    display.text(f"People: {peopleAmount}",settings.width//20,settings.width//7, settings.height//10,(0,0,0))
    display.text(f"Coconut: {coconutAmount}", settings.width//20,settings.width-settings.width//7, settings.height//10,(0,0,0))




    buyPerson=display.button("Buy Person",settings.width//2.4,settings.width//3,settings.width-settings.width//1.3,settings.height//1.2, (0,0,0))
    doneTurn=display.button("Done",settings.width//2.4,settings.width//3,settings.width//1.3,settings.height//1.2, (0,0,0))



    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buyPerson.collidepoint(event.pos):
                peopleAmount,coconutAmount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount=toolBox.buyPerson(peopleAmount,coconutAmount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount)
            elif doneTurn.collidepoint(event.pos):
                peopleAmount,coconutAmount=disaster.randomDisaster(peopleAmount,coconutAmount,boatAmount,blanketAmount,activeSwordAmount+unactiveSwordAmount,treeAmount,superTreeAmount)
                peopleAmount,coconutAmount=toolBox.feed(peopleAmount,coconutAmount)

    pygame.display.flip()
