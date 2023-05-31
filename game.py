import pygame

import toolBox
import display
import settings
import disaster


def startGame():
    turn=1

    #starting resources
    peopleAmount=0
    coconutAmount=2
    boatAmount=0
    medicineAmount=0
    blanketAmount=0
    activeSwordAmount=0
    unactiveSwordAmount=0
    treeAmount=1
    superTreeAmount=0
    spearAmount=0
    netAmount=0

    #makes it so the player gets a random resource
    peopleAmount,coconutAmount,boatAmount,blanketAmount,netAmount,activeSwordAmount=toolBox.buyPerson(peopleAmount,coconutAmount,boatAmount,blanketAmount,netAmount,activeSwordAmount)

    disasters=[]

    turn=1

    pygame.init()


    display.image_resize("background.png",settings.width,settings.height)

    while True:
        # set background
        display.image("image/newbackground.png",0,0)



        buyPerson = display.button("Buy Person", settings.width*0.3225, settings.width // 4,settings.width*0.17, settings.height*0.885, (0, 0, 0))
        tradeButton= display.button("Trade", settings.width*0.3225, settings.width // 4,settings.width*0.5, settings.height * 0.125, (0, 0, 0))
        doneTurn = display.button("Done", settings.width *0.3225, settings.width // 4, settings.width*0.5,settings.height *0.885, (0, 0, 0))
        quitButton=display.button("Quit",settings.width*0.3225,settings.width*0.25,settings.width*0.83,settings.height*0.885,(0,0,0))
        # display button for the resource window
        resourceButton = display.button("Check Resources", settings.width * 0.3225, settings.width // 5,
                                        settings.width * 0.83, settings.height * 0.125, (0, 0, 0))


        toolBox.peopleAndCoconuts(peopleAmount, coconutAmount)




        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buyPerson.collidepoint(event.pos):
                    peopleAmount,coconutAmount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount=toolBox.buyPerson(peopleAmount,coconutAmount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount)
                elif doneTurn.collidepoint(event.pos):
                    #disasters execpt for bear attack
                    #for every 2 people that doesn't have a blanket one will die but if everyone has a blanket it gets removed
                    if peopleAmount//2>blanketAmount and disasters.count("cold night")>0:
                        #
                        disasters.remove("cold night")
                    else:
                        peopleAmount=disaster.coldNight(peopleAmount, blanketAmount, disasters)

                    peopleAmount, disasters=disaster.volcano(peopleAmount, boatAmount, disasters)

                    #clear disasters that have already been fulfilled
                    if disasters.count("bear attack")>0:
                        disasters.remove("bear attack")
                    if disasters.count("volcano")>0:
                        disasters.remove("volcano")

                    peopleAmount,coconutAmount=toolBox.feed(peopleAmount,coconutAmount)
                    coconutAmount, disasters=toolBox.generateCoconuts(coconutAmount,treeAmount,superTreeAmount,spearAmount,netAmount,turn, disasters)
                    disasters.append(disaster.disaster())
                    turn+=1
                    #bear attack results

                    peopleAmount=disaster.bearAttack(peopleAmount,unactiveSwordAmount+activeSwordAmount, disasters)

                elif resourceButton.collidepoint(event.pos):
                    toolBox.resourcesForWindow(peopleAmount, coconutAmount, boatAmount, blanketAmount, medicineAmount, activeSwordAmount, unactiveSwordAmount, treeAmount, superTreeAmount, spearAmount, netAmount)
                elif tradeButton.collidepoint(event.pos):
                    peopleAmount,coconutAmount,boatAmount,medicineAmount,blanketAmount,activeSwordAmount,treeAmount,superTreeAmount,spearAmount,netAmount=toolBox.tradeButtons(peopleAmount,coconutAmount,boatAmount,medicineAmount,blanketAmount,unactiveSwordAmount+activeSwordAmount,treeAmount,superTreeAmount,spearAmount,netAmount)

                elif quitButton.collidepoint(event.pos):
                    return

        #player loses
        if peopleAmount<=0:
            return


        pygame.display.flip()