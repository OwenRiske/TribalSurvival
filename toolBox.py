import random

import pygame

import display
import settings


def feed(peopleAmount, coconutCount):
    if(peopleAmount>coconutCount):
        peopleAmount-=peopleAmount-coconutCount
        coconutCount=0
    else:
        coconutCount-=peopleAmount
    return peopleAmount, coconutCount

def buyPerson(peopleAmount, coconutCount, boatAmount, blanketAmount, medicineAmount, activeSwordAmount):

    if(coconutCount>=1):
        card=random.randint(1,4)
        if(card==1):
            boatAmount+=1
        elif(card==2):
            blanketAmount+=1
        elif (card == 3):
            medicineAmount += 1
        elif (card == 4):
            activeSwordAmount += 1
        return peopleAmount+1, coconutCount-1, boatAmount,blanketAmount,medicineAmount,activeSwordAmount
    return peopleAmount,coconutCount,boatAmount,blanketAmount,medicineAmount,activeSwordAmount

def tradeButtons(peopleAmount,coconutAmount,boatAmount,medicineAmount,blanketAmount,swordAmount,treeAmount,superTreeAmount,spearAmount,netAmount):

    #trade arrays
    giveInTrade = []
    takeInTrade = []

    # trade window
    window = display.rect((165, 85, 25), settings.width * 0.5, settings.height * 0.5, settings.width * 0.96,
                          settings.height * 0.96, 0)
    display.rect((0, 0, 0), settings.width * 0.5, settings.height * 0.5, settings.width * 0.96,
                 settings.height * 0.96, settings.width // 400)

    #trade window text
    display.text("GIVE",settings.width//12,settings.width*0.5,settings.height*0.575,(0,0,0))
    display.text("TAKE",settings.width//12,settings.width*0.5,settings.height*0.1,(0,0,0))
    #give resource buttons
    giveBoat=display.button("Give Boat",settings.width*0.225,settings.width//5,settings.width*0.149,settings.height*0.88,(0,0,0))
    giveSword=display.button("Give Sword",settings.width*0.225,settings.width//5,settings.width*0.385,settings.height*0.88,(0,0,0))
    giveBlanket=display.button("Give Blanket",settings.width*0.225,settings.width//5,settings.width*0.62,settings.height*0.88,(0,0,0))
    giveMedicine=display.button("Give Medicine",settings.width*0.225,settings.width//6,settings.width*0.855,settings.height*0.88,(0,0,0))
    giveTree=display.button("Give Tree",settings.width*0.225,settings.width//5,settings.width*0.149,settings.height*0.7075,(0,0,0))
    giveSuperTree=display.button("Give Super Tree",settings.width*0.225,settings.width//7,settings.width*0.385,settings.height*0.7075,(0,0,0))
    giveSpear=display.button("Give Spear",settings.width*0.225,settings.width//5,settings.width*0.62,settings.height*0.7075,(0,0,0))
    giveNet=display.button("Give Net",settings.width*0.225,settings.width//4,settings.width*0.855,settings.height*0.7075,(0,0,0))

    takeBoat = display.button("Take Boat", settings.width * 0.225, settings.width // 5, settings.width * 0.149,
                              settings.height * 0.25, (0, 0, 0))
    takeSword = display.button("Take Sword", settings.width * 0.225, settings.width // 5, settings.width * 0.385,
                               settings.height * 0.25, (0, 0, 0))
    takeBlanket = display.button("Take Blanket", settings.width * 0.225, settings.width // 5, settings.width * 0.62,
                                 settings.height * 0.25, (0, 0, 0))
    takeMedicine = display.button("Take Medicine", settings.width * 0.225, settings.width // 6, settings.width * 0.855,
                                  settings.height * 0.25, (0, 0, 0))
    takeTree = display.button("Take Tree", settings.width * 0.225, settings.width // 5, settings.width * 0.149,
                              settings.height * 0.425, (0, 0, 0))
    takeSuperTree = display.button("Take Super Tree", settings.width * 0.225, settings.width // 7,
                                   settings.width * 0.385, settings.height * 0.425, (0, 0, 0))
    takeSpear = display.button("Take Spear", settings.width * 0.225, settings.width // 5, settings.width * 0.62,
                               settings.height * 0.425, (0, 0, 0))
    takeNet = display.button("Take Net", settings.width * 0.225, settings.width // 4, settings.width * 0.855,
                             settings.height * 0.425, (0, 0, 0))

    #reset button
    reset=display.button("Reset Trade", settings.width * 0.2, settings.width // 6, settings.width * 0.855,
                             settings.height * 0.1, (0, 0, 0))
    trade=display.button("Trade", settings.width * 0.2, settings.width // 6, settings.width * 0.75,
                             settings.height * 0.1, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if giveMedicine.collidepoint(event.pos):
                print("")
            elif window.collidepoint(event.pos):
                return




    return giveTree,giveSuperTree,giveMedicine,giveBlanket,giveBoat,giveSword,giveSpear,giveNet,takeTree,takeSuperTree,takeMedicine,takeBlanket,takeBoat,takeSpear,takeNet, reset




def resourcesForWindow(boatAmount, blanketAmount, medicineAmount, activeSwordAmount, unactiveSwordAmount, treeAmount, superTreeAmount,spearAmount, netAmount):
    display.text(f"Boats: {boatAmount}", settings.width // 20, settings.width - settings.width // 6.5,
                 settings.height // 12, (255, 255, 255))
    display.text(f"Blankets: {blanketAmount}", settings.width // 20, settings.width - settings.width // 5.3,
                 settings.height // 6.75, (255, 255, 255))
    display.text(f"Medicines: {medicineAmount}", settings.width // 20, settings.width - settings.width // 5,
                 settings.height // 4.75, (255, 255, 255))
    display.text(f"Unused Swords: {activeSwordAmount}", settings.width // 20, settings.width - settings.width // 3.75,
                 settings.height // 3.7, (255, 255, 255))
    display.text(f"Used Swords: {unactiveSwordAmount}", settings.width // 20, settings.width - settings.width // 4.25,
                 settings.height // 3, (255, 255, 255))
    display.text(f"Coconut Trees: {treeAmount}", settings.width // 20, settings.width - settings.width // 4,
                 settings.height // 2.5, (255, 255, 255))
    display.text(f"Super Coconut Trees: {superTreeAmount}", settings.width // 20, settings.width - settings.width // 3,
                 settings.height // 2.15, (255, 255, 255))
    display.text(f"Spears: {spearAmount}", settings.width // 20, settings.width - settings.width // 6,
                 settings.height // 1.9, (255, 255, 255))
    display.text(f"Nets: {netAmount}", settings.width // 20, settings.width - settings.width // 7.5,
                 settings.height // 1.675, (255, 255, 255))


def tradeValue(peopleAmount, coconutAmount, treeAmount, superTreeAmount, blanketAmount, medicineAmount, swordAmount, spearAmount, netAmount):
    return peopleAmount*2+coconutAmount+treeAmount*3+superTreeAmount*5+blanketAmount*2+medicineAmount+swordAmount*3+spearAmount*3+netAmount*3

def absoluteValue(input):
    if(input<0):
        input*=-1
    return input

def positiveOnly(input):
    if(input<0):
        input=0
    return input