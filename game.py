#Owen Riske

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
    peopleAmount,coconutAmount,boatAmount,blanketAmount,netAmount,activeSwordAmount=toolBox.buyPerson(peopleAmount,coconutAmount,boatAmount,blanketAmount,netAmount,activeSwordAmount, treeAmount,superTreeAmount,spearAmount,netAmount)

    #array for the disaster that the user will get
    disasters=[]

    #keep track of turns
    turn=1

    pygame.init()


    while True:
        # set background
        display.background("newbackground.png")


        #button for the game menu
        #button for getting people
        buyPerson = display.button("Buy Person", settings.width*0.3225, settings.width // 4,settings.width*0.17, settings.height*0.885, (0, 0, 0))
        #button for trade
        tradeButton= display.button("Trade", settings.width*0.3225, settings.width // 4,settings.width*0.5, settings.height * 0.125, (0, 0, 0))
        #end turn button
        doneTurn = display.button("Done", settings.width *0.3225, settings.width // 4, settings.width*0.5,settings.height *0.885, (0, 0, 0))
        #quit game button
        quitButton=display.button("Quit",settings.width*0.3225,settings.width*0.25,settings.width*0.83,settings.height*0.885,(0,0,0))
        # display button for the resource window
        resourceButton = display.button("Check Resources", settings.width * 0.3225, settings.width // 5,settings.width * 0.83, settings.height * 0.125, (0, 0, 0))

        #display the coconut amount and people amount
        toolBox.peopleAndCoconuts(peopleAmount, coconutAmount)




        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #acquire person
                if buyPerson.collidepoint(event.pos):
                    peopleAmount,coconutAmount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount, treeAmount, superTreeAmount, spearAmount, netAmount=toolBox.buyPerson(peopleAmount,coconutAmount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount, treeAmount, superTreeAmount, spearAmount, netAmount)
                elif doneTurn.collidepoint(event.pos):
                    #disasters execpt for bear attack
                    #for every 2 people that doesn't have a blanket one will die but if everyone has a blanket it gets removed
                    if peopleAmount//2<=blanketAmount and disasters.count("cold night")>0:
                        #remove cold night form list of disaster
                        disasters.remove("cold night")
                    else:
                        #lose people
                        peopleAmount=disaster.coldNight(peopleAmount, blanketAmount, disasters)

                    #do the volcano disaster
                    peopleAmount, disasters=disaster.volcano(peopleAmount, boatAmount, disasters)

                    #clear disasters that have already been fulfilled
                    if disasters.count("bear attack")>0:
                        disasters.remove("bear attack")
                    if disasters.count("volcano")>0:
                        disasters.remove("volcano")

                    #feed people
                    peopleAmount,coconutAmount=toolBox.feed(peopleAmount,coconutAmount)
                    #generate coconuts
                    coconutAmount, disasters=toolBox.generateCoconuts(coconutAmount,treeAmount,superTreeAmount,spearAmount,netAmount,turn, disasters)
                    #add disasters
                    disasters.append(disaster.disaster())
                    turn+=1
                    #bear attack results
                    peopleAmount=disaster.bearAttack(peopleAmount,unactiveSwordAmount+activeSwordAmount, disasters)

                #dispaly reource window
                elif resourceButton.collidepoint(event.pos):
                    toolBox.resourcesForWindow(peopleAmount, coconutAmount, boatAmount, blanketAmount, medicineAmount, activeSwordAmount, unactiveSwordAmount, treeAmount, superTreeAmount, spearAmount, netAmount)
                #start trade
                elif tradeButton.collidepoint(event.pos):
                    peopleAmount,coconutAmount,boatAmount,medicineAmount,blanketAmount,activeSwordAmount,treeAmount,superTreeAmount,spearAmount,netAmount=toolBox.tradeButtons(peopleAmount,coconutAmount,boatAmount,medicineAmount,blanketAmount,unactiveSwordAmount+activeSwordAmount,treeAmount,superTreeAmount,spearAmount,netAmount)

                #quit game
                elif quitButton.collidepoint(event.pos):
                    return

        #player loses
        if peopleAmount<=0:
            return


        pygame.display.flip()
