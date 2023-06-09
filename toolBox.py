#Owen Riske

import random
import pygame
import display
import settings
import disaster

#generates coconuts based on which generators the user has
def generateCoconuts(coconutAmount, treeAmount, superTreeAmount, spearAmount, netAmount, turn, disasters):
    #get tree yeild if correct turn and no tree disease
    if whenDividingIsItAWholeNum(turn,settings.treeTurnsForYeild) and disasters.count("tree disease")<1:
        coconutAmount+=settings.treeYeild*treeAmount

    #get tree yeild if correct turn and no super tree disease
    elif whenDividingIsItAWholeNum(turn,settings.superTreeTurnsForYeild) and disasters.count("tree disease")<1:
        coconutAmount+=settings.superTreeYeild*superTreeAmount

    # get tree yeild if correct turn and no spear disease
    elif whenDividingIsItAWholeNum(turn,settings.spearTurnsForYeild) and disasters.count("animal disease")<1:
        coconutAmount+=settings.spearYeild*spearAmount

    #get tree yeild if correct turn and no net disease
    elif whenDividingIsItAWholeNum(turn,settings.netTurnsForYeild) and disasters.count("fish disease")<1:
        coconutAmount+=settings.netYeild*netAmount

    #remove disease disasters
    disaster.removeDisaster("tree disease",disasters)
    disaster.removeDisaster("animal disease",disasters)
    disaster.removeDisaster("fish disease",disasters)

    return coconutAmount, disasters


#remove required amounts based on the people amount and coconut amount
def feed(peopleAmount, coconutCount):
    #if there is more people then coconuts
    if(peopleAmount>coconutCount):
        #then remove the left over people
        peopleAmount-=peopleAmount-coconutCount
        #set coconut amount to 0
        coconutCount=0
    else:
        #otherwise subtract peopleamount from coconut amoutn
        coconutCount-=peopleAmount
    return peopleAmount, coconutCount

def buyPerson(peopleAmount, coconutCount, boatAmount, blanketAmount, medicineAmount, activeSwordAmount, treeAmount, superTreeAmount, spearAmount, netAmount):
    #if have enough coconuts to buy person then
    if(coconutCount>=1):
        #get random resource
        card=random.randint(1,8)
        #boat
        if(card==1):
            boatAmount+=1
        #blanket
        elif(card==2):
            blanketAmount+=1
        #medicine
        elif (card == 3):
            medicineAmount += 1
        #sword
        elif (card == 4):
            activeSwordAmount += 1
        #tree
        elif (card==5):
            treeAmount+=1
        #super tree
        elif (card==6):
            superTreeAmount+=1
        #spear
        elif (card==7):
            spearAmount+=1
        #net
        elif (card==8):
            netAmount+=1
        #return the resources and the people and coconuts
        return peopleAmount+1, coconutCount-1, boatAmount,blanketAmount,medicineAmount,activeSwordAmount
    return peopleAmount,coconutCount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount

def tradeButtons(peopleAmount,coconutAmount,boatAmount,medicineAmount,blanketAmount,swordAmount,treeAmount,superTreeAmount,spearAmount,netAmount):

    #trade arrays
    giveInTrade = []
    takeInTrade = []

    while True:
        # trade window
        window=displayWindow()

        #trade window text
        display.text("GIVE",settings.width//12,settings.width*0.5,settings.height*0.575,(0,0,0))
        display.text("TAKE",settings.width//12,settings.width*0.5,settings.height*0.1,(0,0,0))
        #give resource buttons
        giveBoat=display.button("Give Boat",settings.width*0.1775,settings.width*0.2,settings.width*0.125,settings.height*0.88,(0,0,0))
        giveSword=display.button("Give Sword",settings.width*0.1775,settings.width*0.182,settings.width*0.31,settings.height*0.88,(0,0,0))
        giveBlanket=display.button("Give Blanket",settings.width*0.1775,settings.width*0.16,settings.width*0.495,settings.height*0.88,(0,0,0))
        giveMedicine=display.button("Give Medicine",settings.width*0.1775,settings.width*0.145,settings.width*0.685,settings.height*0.88,(0,0,0))
        giveCoconut=display.button("Give Coconut",settings.width*0.1775,settings.width*0.145,settings.width*0.875,settings.height*0.88,(0,0,0))
        giveTree=display.button("Give Tree",settings.width*0.1775,settings.width*0.2,settings.width*0.125,settings.height*0.7075,(0,0,0))
        giveSuperTree=display.button("Give Super Tree",settings.width*0.1775,settings.width*0.125,settings.width*0.31,settings.height*0.7075,(0,0,0))
        giveSpear=display.button("Give Spear",settings.width*0.1775,settings.width*0.175,settings.width*0.495,settings.height*0.7075,(0,0,0))
        giveNet=display.button("Give Net",settings.width*0.1775,settings.width*0.175,settings.width*0.685,settings.height*0.7075,(0,0,0))
        givePerson=display.button("Give Person",settings.width*0.1775,settings.width*0.145,settings.width*0.875,settings.height*0.7075,(0,0,0))


        #giveCoconut=display

        #take resource buttons
        takeBoat = display.button("Take Boat", settings.width * 0.1775, settings.width*0.2, settings.width * 0.125,settings.height * 0.25, (0, 0, 0))
        takeSword = display.button("Take Sword", settings.width * 0.1775, settings.width*0.182, settings.width * 0.31,settings.height * 0.25, (0, 0, 0))
        takeBlanket = display.button("Take Blanket", settings.width * 0.1775, settings.width*0.16, settings.width * 0.495,  settings.height * 0.25, (0, 0, 0))
        takeMedicine = display.button("Take Medicine", settings.width * 0.1775, settings.width*0.145, settings.width * 0.685,   settings.height * 0.25, (0, 0, 0))
        takeCoconut=display.button("Give Coconut",settings.width*0.1775,settings.width*0.145,settings.width*0.875,settings.height*0.25,(0,0,0))
        takeTree = display.button("Take Tree", settings.width * 0.1775, settings.width*0.2, settings.width * 0.125,settings.height * 0.425, (0, 0, 0))
        takeSuperTree = display.button("Take Super Tree", settings.width * 0.1775, settings.width*0.125,    settings.width * 0.31, settings.height * 0.425, (0, 0, 0))
        takeSpear = display.button("Take Spear", settings.width * 0.1775, settings.width*0.175, settings.width * 0.495,settings.height * 0.425, (0, 0, 0))
        takeNet = display.button("Take Net", settings.width * 0.1775, settings.width*0.175, settings.width * 0.685,settings.height * 0.425, (0, 0, 0))
        takePerson=display.button("Take Person",settings.width*0.1775,settings.width*0.145,settings.width*0.875,settings.height*0.425,(0,0,0))

        #reset trade button
        resetButton = display.button("Reset Trade", settings.width * 0.2, settings.width // 6, settings.width * 0.855,settings.height * 0.1, (0, 0, 0))

        #proceed with trade button
        tradeButton=display.button("Trade", settings.width * 0.2, settings.width // 6, settings.width * 0.15,settings.height * 0.1, (0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #add tree to being given in trade
                if giveTree.collidepoint(event.pos) and treeAmount>0:
                    giveInTrade.append("tree")
                #add super tree to being given in trade
                elif giveSuperTree.collidepoint(event.pos) and superTreeAmount>0:
                    giveInTrade.append("super tree")
                #add boat to being given in trade
                elif giveBoat.collidepoint(event.pos) and boatAmount>0:
                    giveInTrade.append("boat")
                #add medicine to being given in trade
                elif giveMedicine.collidepoint(event.pos) and medicineAmount>0:
                    giveInTrade.append("medicine")
                # add blanket to being given in trade
                elif giveBlanket.collidepoint(event.pos) and blanketAmount>0:
                    giveInTrade.append("blanket")
                # add sword to being given in trade
                elif giveSword.collidepoint(event.pos) and swordAmount>0:
                    giveInTrade.append("sword")
                # add spear to being given in trade
                elif giveSpear.collidepoint(event.pos) and spearAmount>0:
                    giveSpear.append("spear")
                # add net to being given in trade
                elif giveNet.collidepoint(event.pos) and netAmount>0:
                    giveInTrade.append("net")
                # add people to being given in trade
                elif givePerson.collidepoint(event.pos) and peopleAmount>0:
                    giveInTrade.append("people")
                # add coconut to being given in trade
                elif giveCoconut.collidepoint(event.pos) and coconutAmount>0:
                    giveInTrade.append("coconut")
                # add tree to being taken in trade
                elif takeTree.collidepoint(event.pos):
                    takeInTrade.append("tree")
                # add super tree to being taken in trade
                elif takeSuperTree.collidepoint(event.pos):
                    takeInTrade.append("super tree")
                # add medicine to being taken in trade
                elif takeMedicine.collidepoint(event.pos):
                    takeInTrade.append("medicine")
                # add blanket to being taken in trade
                elif takeBlanket.collidepoint(event.pos):
                    takeInTrade.append("blanket")
                # add boat to being taken in trade
                elif takeBoat.collidepoint(event.pos):
                    takeInTrade.append("boat")
                # add sword to being taken in trade
                elif takeSword.collidepoint(event.pos):
                    takeInTrade.append("sword")
                # add spear to being taken in trade
                elif takeSpear.collidepoint(event.pos):
                    takeInTrade.append("spear")
                # add net to being taken in trade
                elif takeNet.collidepoint(event.pos):
                    takeInTrade.append("net")
                # add people to being taken in trade
                elif takePerson.collidepoint(event.pos):
                    takeInTrade.append("people")
                # add coconut to being taken in trade
                elif takeCoconut.collidepoint(event.pos):
                    takeInTrade.append("coconut")
                # reset trade
                elif resetButton.collidepoint(event.pos):
                    takeInTrade.clear()
                    giveInTrade.clear()
                #start trade
                elif tradeButton.collidepoint(event.pos):
                    # calculate whether the trade commences or not
                    if tradeAI(giveInTrade,takeInTrade):
                        #change the amount for the resources based on the trade
                        peopleAmount, coconutAmount, boatAmount, medicineAmount, blanketAmount, swordAmount, treeAmount, superTreeAmount, spearAmount, netAmount, takeInTrade, giveInTrade=trade(giveInTrade,takeInTrade,peopleAmount,coconutAmount,boatAmount,medicineAmount,blanketAmount,swordAmount,treeAmount,superTreeAmount,spearAmount,netAmount)
                #if user clicks off of trade window close it
                elif window.collidepoint(event.pos)==False:
                    return peopleAmount,coconutAmount,boatAmount,medicineAmount,blanketAmount,swordAmount,treeAmount,superTreeAmount,spearAmount,netAmount
        pygame.display.flip()



def trade(giveInTrade, takeInTrade, peopleAmount,coconutAmount,boatAmount,medicineAmount,blanketAmount,swordAmount,treeAmount,superTreeAmount,spearAmount,netAmount):
    #add the amount of resources user is getting in the trad and subtract the resources the user is giving up in the trade
    return peopleAmount+takeInTrade.count("people")-giveInTrade.count("people"),coconutAmount+takeInTrade.count("coconut")-giveInTrade.count("coconut"),boatAmount+takeInTrade.count("boat")-giveInTrade.count("boat"),medicineAmount+takeInTrade.count("medicine")-giveInTrade.count("medicine"),blanketAmount+takeInTrade.count("blanket")-giveInTrade.count("blanket"),swordAmount+takeInTrade.count("sword")-giveInTrade.count("sword"),treeAmount+takeInTrade.count("tree")-giveInTrade.count("tree"),superTreeAmount+takeInTrade.count("super tree")-giveInTrade.count("super tree"),spearAmount+takeInTrade.count("spear")-giveInTrade.count("spear"),netAmount+takeInTrade.count("net")-giveInTrade.count("net"),takeInTrade.clear(),giveInTrade.clear()




def resourcesForWindow(peopleAmount, coconutAmount, boatAmount, blanketAmount, medicineAmount, activeSwordAmount, unactiveSwordAmount, treeAmount, superTreeAmount,spearAmount, netAmount):

    while True:
        # resource window
        displayWindow()
        #display boat amount
        display.text(f"Boats: {boatAmount}", settings.width // 20, settings.width - settings.width // 6.5,settings.height // 12, (255, 255, 255))
        #display blanket amount
        display.text(f"Blankets: {blanketAmount}", settings.width // 20, settings.width - settings.width // 5.3,settings.height // 6.75, (255, 255, 255))
        #display medicine amount
        display.text(f"Medicines: {medicineAmount}", settings.width // 20, settings.width - settings.width // 5,settings.height // 4.75, (255, 255, 255))
        #display unused sword amount
        display.text(f"Unused Swords: {activeSwordAmount}", settings.width // 20, settings.width - settings.width // 3.75,settings.height // 3.7, (255, 255, 255))
        #display used sword amount
        display.text(f"Used Swords: {unactiveSwordAmount}", settings.width // 20, settings.width - settings.width // 4.25,settings.height // 3, (255, 255, 255))
        #display coconut tree amount
        display.text(f"Coconut Trees: {treeAmount}", settings.width // 20, settings.width - settings.width // 4,settings.height // 2.5, (255, 255, 255))
        #display super coconut tree amount
        display.text(f"Super Coconut Trees: {superTreeAmount}", settings.width // 20, settings.width - settings.width // 3,settings.height // 2.15, (255, 255, 255))
        #display spear amount
        display.text(f"Spears: {spearAmount}", settings.width // 20, settings.width - settings.width // 6,settings.height // 1.9, (255, 255, 255))
        #display net amount
        display.text(f"Nets: {netAmount}", settings.width // 20, settings.width - settings.width // 7.5,settings.height // 1.675, (255, 255, 255))
        #display the people and coconut amount
        peopleAndCoconuts(peopleAmount,coconutAmount)


        #if user clicks on screen close the resource window
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.flip()

#outputs whether the number after being divided is still a whole number
def whenDividingIsItAWholeNum(input, numCheckingFor):
    return input//numCheckingFor == input/numCheckingFor




def tradeAI(resourcesGiving, resourcesGetting):
    likelyHoodOfTrade=tradeValueFromArray(resourcesGiving)-tradeValueFromArray(resourcesGetting)-settings.likelyHoodOfTradeWithBoat

    #minium trade likelyhodd is 0
    if likelyHoodOfTrade<0:
        likelyHoodOfTrade=0

    #if the random number between 0 and trade likely hood is 0
    if random.randint(0,likelyHoodOfTrade)==0:
        #then return true
        return True
    else:
        #otherwise return false
        return False

#display for the resouce and trade window
def displayWindow():
    #inside of window
    window = display.rect((165, 85, 25), settings.width * 0.5, settings.height * 0.5, settings.width * 0.96,
                          settings.height * 0.96, 0)
    #border of window
    display.rect((0, 0, 0), settings.width * 0.5, settings.height * 0.5, settings.width * 0.96, settings.height * 0.96,
                 settings.width // 400)
    return window

#display the people and coconut amount in the top right corner
def peopleAndCoconuts(peopleAmount, coconutAmount):
    display.text(f"People: {peopleAmount}", settings.width * 0.05, settings.width * 0.15384,settings.height * 0.08333,(0, 0, 0))
    display.text(f"Coconut: {coconutAmount}", settings.width * 0.05, settings.width * 0.15384,settings.height * 0.148148,(0, 0, 0))

#return the value of the resources using trade value function
def tradeValueFromArray(inputArray):
    return tradeValue(inputArray.count("people"),inputArray.count("coconut"),inputArray.count("tree"),inputArray.count("super tree"),inputArray.count("boat"),inputArray.count("blanket"),inputArray.count("medicine"),inputArray.count("sword"),inputArray.count("spear"),inputArray.count("net"))

#multiply each resource to be traded by the value that has been set for each resource
def tradeValue(peopleAmount, coconutAmount, treeAmount, superTreeAmount, boatAmount, blanketAmount, medicineAmount, swordAmount, spearAmount, netAmount):
    return peopleAmount*settings.peopleValue+coconutAmount*settings.coconutValue+treeAmount*settings.treeValue+superTreeAmount*settings.superTreeValue+boatAmount*settings.boatValue+blanketAmount*settings.blanketValue+medicineAmount+swordAmount*settings.swordValue+spearAmount*settings.spearValue+netAmount*settings.netValue

#remove all of one element from array
def removeAllFromArray(array, elementToBeRemoved):
    tempArray=array.remove(elementToBeRemoved)
    while tempArray!=array:
        array=tempArray
        tempArray = array.remove(elementToBeRemoved)

    return array

#get the absolute value of the input
def absoluteValue(input):
    if(input<0):
        input*=-1
    return input

#output positive only numbers
def positiveOnly(input):
    if(input<0):
        input=0
    return input