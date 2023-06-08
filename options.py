#Owen Riske

import pygame
import display
import settings

#x for exitting the window
def exitSquare(x,y,size, colour):
    output=display.rect(colour,x,y,size,size,0)
    display.text("x",size,x,y,(0,0,0))
    return output

#default options
def optionsMenu():


    pygame.init()
    #loop
    while True:
        #background image
        display.background("optionMenu.png")
        #button to exit option window
        exitButton=exitSquare(settings.width*0.08,settings.height*0.08,settings.width*0.05,(245,190,90))

        #increase and decrease buttons for screen size, (change screen size by 1 times the number displayed with variable)
        smallerScreenButton,biggerScreenButton=display.adjustableNum("Screen Size", str(settings.width),settings.height*0.5,(0,0,0))
        smallerScreenButtonx10 = display.button("<<", settings.width * 0.1, settings.width * 0.25, settings.width * 0.27,settings.height * 0.5, (0, 0, 0))
        smallerScreenButtonx100 = display.button("<<<", settings.width * 0.1, settings.width * 0.25, settings.width * 0.165,settings.height * 0.5, (0, 0, 0))
        biggerScreenButtonx10 = display.button(">>", settings.width * 0.1, settings.width * 0.25,settings.width * 0.7275, settings.height * 0.5, (0, 0, 0))
        biggerScreenButtonx100 = display.button(">>>", settings.width * 0.1, settings.width * 0.25,settings.width * 0.83, settings.height * 0.5, (0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #exit button
                if exitButton.collidepoint(event.pos):
                    return
                #shrink screen size
                elif smallerScreenButton.collidepoint(event.pos):
                    settings.width -= 1
                    settings.changeScreenSize()
                #shrink screen size by 10
                elif smallerScreenButtonx10.collidepoint(event.pos):
                    settings.width-=10
                    settings.changeScreenSize()
                #shrink screen size by 100
                elif smallerScreenButtonx100.collidepoint(event.pos):
                    settings.width -= 100
                    settings.changeScreenSize()
                #increase screen size
                elif biggerScreenButton.collidepoint(event.pos):
                    settings.width+=1
                    settings.changeScreenSize()
                #increase screen size by 10
                elif biggerScreenButtonx10.collidepoint(event.pos):
                    settings.width+=10
                    settings.changeScreenSize()

                #increase screen size by 100
                elif biggerScreenButtonx100.collidepoint(event.pos):
                    settings.width+=100
                    settings.changeScreenSize()
            #if user inputs o then show admin options
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    settingAlterMenu()

        pygame.display.flip()

def settingAlterMenu():
    pygame.init()

    #determines which menu will be displayed
    optionMenu="Misc"

    #which page on the menu display is open (only for trade)
    menuPage=1

    while True:
        # background image
        display.background("optionMenu.png")

        # button to exit option window
        exitButton = exitSquare(settings.width * 0.08, settings.height * 0.08, settings.width * 0.05, (245, 190, 90))

        #if menu is misc then show the misc options
        if optionMenu=="Misc":
            #determines the likelyhoodofTrade
            smallerBoatLikelyHoodButton, biggerBoatLikelyHoodButton=display.adjustableNum("Boat Trade Likely Hood", str(settings.likelyHoodOfTradeWithBoat),settings.height*0.075,(0,0,0))

        #if menu is disasters then show disaster options
        elif optionMenu=="Disasters":
            #determines amount of people per bear attack
            smallerBearKillHoodButton,biggerBearKillHoodButton=display.adjustableNum("Bear Attack Kill", str(settings.peopleKilledInBearAttack), settings.height*0.075, (0,0,0))
            #determines likely hood of bear attack
            smallerBearLikelyHoodButton,biggerBearLikelyHoodButton=display.adjustableNum("Bear Likely Hood",str(settings.bearAttackLikelyHood),settings.height*0.175,(0,0,0))

            #determines likely hood of volcano
            smallerVolcanoLikelyHoodButton, biggerVolcanoLikelyHoodButton=display.adjustableNum("Volcano Likely Hood", str(settings.volcanoLikelyhood),settings.height*0.275,(0,0,0))

            #determines likely hood of cold night
            smallerColdNightLikelyHoodButton, biggerColdNightLikelyHoodButton=display.adjustableNum("Cold Night Likely Hood", str(settings.coldNightLikelyhood),settings.height*0.375,(0,0,0))

            #determines likely hood of tree disease
            smallerTreeDiseaseLikelyHoodButton, biggerTreeDiseaseLikelyHoodButton=display.adjustableNum("Tree Disease Likely Hood", str(settings.treeDiseaseLikelyhood),settings.height*0.475,(0,0,0))

            #determines likely hood of fish disease
            smallerFishDiseaseLikelyHoodButton, biggerFishDiseaseLikelyHoodButton=display.adjustableNum("Fish Disease Likely Hood", str(settings.fishDiseaseLikelyhood),settings.height*0.575,(0,0,0))

            #determines likely hood of fish disease
            smallerAnimalDiseaseLikelyHoodButton, biggerAnimalDiseaseLikelyHoodButton=display.adjustableNum("Animal Disease Likely Hood", str(settings.animalDiseaseLikelyhood),settings.height*0.675,(0,0,0))

            #determines likely hood of clear day
            smallerClearDayLikelyHoodButton, biggerClearDayLikelyHoodButton=display.adjustableNum("Warm Day Likely Hood", str(settings.clearDayLikelyhood),settings.height*0.775, (0,0,0))

        #if menu is trade then show trade options
        elif optionMenu=="Trade":
            #show trade option based on what page the user is on
            if menuPage==1:

                #determine people value
                smallerPeopleValue, biggerPeopleValue=display.adjustableNum("People Value", str(settings.peopleValue),settings.height*0.075,(0,0,0))

                #determine coconut value
                smallerCoconutValue, biggerCoconutValue=display.adjustableNum("Coconut Value", str(settings.coconutValue),settings.height*0.175,(0,0,0))

                #determine boat value
                smallerBoatValue, biggerBoatValue=display.adjustableNum("Boat Value", str(settings.boatValue),settings.height*0.275,(0,0,0))

                #determine medicine value
                smallerMedicineValue, biggerMedicineValue=display.adjustableNum("Medicine Value", str(settings.medicineValue),settings.height*0.375,(0,0,0))

                #determine blanket value
                smallerBlanketValue, biggerBlanketValue=display.adjustableNum("Blanket Value", str(settings.blanketValue),settings.height*0.475,(0,0,0))

            #other option menu for trade
            elif menuPage==2:
                #determine sword value
                smallerSwordValue, biggerSwordValue = display.adjustableNum("Sword Value", str(settings.swordValue),settings.height * 0.075, (0, 0, 0))

                #determine spear value
                smallerSpearValue, biggerSpearValue = display.adjustableNum("Spear Value", str(settings.spearValue),settings.height * 0.175, (0, 0, 0))

                #determine net value
                smallerNetValue, biggerNetValue = display.adjustableNum("Net Value", str(settings.netValue),settings.height * 0.275, (0, 0, 0))

                #determine tree value
                smallerTreeValue, biggerTreeValue = display.adjustableNum("Tree Value", str(settings.treeValue), settings.height * 0.375, (0, 0, 0))

                #determine super Tree value
                smallerSuperTreeValue, biggerSuperTreeValue=display.adjustableNum("Super Tree Value", str(settings.superTreeValue),settings.height*0.475, (0,0,0))
            #if menuPage is not one of the two set it to one
            else:
                menuPage=1

            #determines which page you are on
            smallerPage, biggerPage=display.adjustableNum("Trade Value Page", str(menuPage),settings.height*0.675,(0,0,0))

        #if menu is yeild then show coconut generator options
        elif optionMenu=="Yeild":
            #determines the yeild and amount of turn it will take to get the yeild for tree
            smallerTreeYeild, biggerTreeYeild=display.adjustableNum("Tree Yield", str(settings.treeYeild),settings.height*0.075,(0,0,0))
            smallerTreeTurn, biggerTreeTurn=display.adjustableNum("Tree Turns Per Yield",str(settings.treeTurnsForYeild),settings.height*0.175,(0,0,0))

            #determines the yeild and amount of turn it will take to get the yeild for super tree
            smallerSuperTreeYeild, biggerSuperTreeYeild=display.adjustableNum("Super Tree Yield", str(settings.superTreeYeild),settings.height*0.275,(0,0,0))
            smallerSuperTreeTurn, biggerSuperTreeTurn=display.adjustableNum("Super Tree Turns Per Yield",str(settings.superTreeTurnsForYeild),settings.height*0.375,(0,0,0))

            #determines the yeild and amount of turn it will take to get the yeild for spear
            smallerSpearYeild, biggerSpearYeild=display.adjustableNum("Spear Yield", str(settings.spearValue),settings.height*0.475,(0,0,0))
            smallerSpearTurn, biggerSpearTurn=display.adjustableNum("Spear Turns Per Yield",str(settings.spearTurnsForYeild),settings.height*0.575,(0,0,0))

            #determines the yeild and amount of turn it will take to get the yeild for net
            smallerNetYeild, biggerNetYeild=display.adjustableNum("Net Yield", str(settings.netYeild),settings.height*0.675,(0,0,0))
            smallerNetTurn, biggerNetTurn=display.adjustableNum("Net Turns Per Yield",str(settings.netTurnsForYeild),settings.height*0.775,(0,0,0))


        #buttons to change which menu window the user is seeing
        #trade button
        TradeValueButton=display.button("Trade Value",settings.width*0.245,settings.width*0.2325,settings.width*0.125,settings.height*0.895, (0,0,0))
        #disasters button
        DisastersButton=display.button("Disaster",settings.width*0.245,settings.width*0.24,settings.width*0.375,settings.height*0.895, (0,0,0))
        #misc button
        MiscButton=display.button("Misc.",settings.width*0.245,settings.width*0.24,settings.width*0.875,settings.height*0.895, (0,0,0))
        #yeild button
        YeildButton=display.button("Coconut Yeilds",settings.width*0.245,settings.width*0.185,settings.width*0.625,settings.height*0.895, (0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if option menu misc then
                if optionMenu == "Misc":
                    #allow change to trade likely hood
                    settings.likelyHoodOfTradeWithBoat=display.adjustableNumButtonCollidePoint(smallerBoatLikelyHoodButton,biggerBoatLikelyHoodButton,settings.likelyHoodOfTradeWithBoat,event)

                #if option menu disaster then
                elif optionMenu == "Disaster":
                    #allow change to amount of people dying in a bear attack
                    settings.peopleKilledInBearAttack=display.adjustableNumButtonCollidePoint(smallerBearKillHoodButton, biggerBearKillHoodButton,settings.peopleKilledInBearAttack, event)

                    #allow change to bear attack likely hood
                    settings.bearAttackLikelyHood=display.adjustableNumButtonCollidePoint(smallerBearLikelyHoodButton,biggerBearLikelyHoodButton,settings.bearAttackLikelyHood,event)

                    #allow change to volcano likely hood
                    settings.volcanoLikelyhood=display.adjustableNumButtonCollidePoint(smallerVolcanoLikelyHoodButton,biggerVolcanoLikelyHoodButton,settings.volcanoLikelyhood,event)

                    #allow change to cold night likely hood
                    settings.coldNightLikelyhood=display.adjustableNumButtonCollidePoint(smallerColdNightLikelyHoodButton,biggerColdNightLikelyHoodButton,settings.coldNightLikelyhood,event)

                    #allow change to tree disease likely hood
                    settings.treeDiseaseLikelyhood=display.adjustableNumButtonCollidePoint(smallerTreeDiseaseLikelyHoodButton,biggerTreeDiseaseLikelyHoodButton,settings.treeDiseaseLikelyhood,event)

                    #allow change to fish disease likely hood
                    settings.fishDiseaseLikelyhood=display.adjustableNumButtonCollidePoint(smallerFishDiseaseLikelyHoodButton,biggerFishDiseaseLikelyHoodButton,settings.fishDiseaseLikelyhood,event)

                    #allow change to animal disease likely hood
                    settings.animalDiseaseLikelyhood=display.adjustableNumButtonCollidePoint(smallerAnimalDiseaseLikelyHoodButton, biggerAnimalDiseaseLikelyHoodButton,settings.animalDiseaseLikelyhood, event)

                elif optionMenu == "Trade":
                    if menuPage==1:
                        # allow change to people value likely hood
                        settings.peopleValue=display.adjustableNumButtonCollidePoint(smallerPeopleValue,biggerPeopleValue,settings.peopleValue,event)

                        # allow change to coconut value likely hood
                        settings.coconutValue=display.adjustableNumButtonCollidePoint(smallerCoconutValue,biggerCoconutValue,settings.coconutValue,event)

                        # allow change to boat value likely hood
                        settings.boatValue=display.adjustableNumButtonCollidePoint(smallerBoatValue,biggerBoatValue,settings.boatValue,event)

                        # allow change to medicine value likely hood
                        settings.medicineValue=display.adjustableNumButtonCollidePoint(smallerMedicineValue,biggerMedicineValue, settings.medicineValue, event)

                        # allow change to blanket value likely hood
                        settings.blanketValue=display.adjustableNumButtonCollidePoint(smallerBlanketValue,biggerBlanketValue,settings.blanketValue,event)

                    elif menuPage==2:
                        # allow change to sword value likely hood
                        settings.swordValue=display.adjustableNumButtonCollidePoint(smallerSwordValue, biggerSwordValue,settings.swordValue,event)

                        # allow change to spear value likely hood
                        settings.spearValue=display.adjustableNumButtonCollidePoint(smallerSpearValue,biggerSpearValue,settings.spearValue,event)

                        # allow change to net value likely hood
                        settings.netValue=display.adjustableNumButtonCollidePoint(smallerNetValue,biggerNetValue,settings.netValue,event)

                        # allow change to tree value likely hood
                        settings.treeValue=display.adjustableNumButtonCollidePoint(smallerTreeValue,biggerTreeValue,settings.treeValue, event)

                        # allow change to super tree value likely hood
                        settings.superTreeValue=display.adjustableNumButtonCollidePoint(smallerSuperTreeValue,biggerSuperTreeValue,settings.superTreeValue, event)

                    #allow change to menu Page
                    menuPage = display.adjustableNumButtonCollidePointWithMax(smallerPage, biggerPage, menuPage, 2,
                                                                              event)

                #if option menu yeild then
                elif optionMenu == "Yeild":

                    #allow change to yeild and turn per yeild for tree
                    settings.treeYeild=display.adjustableNumButtonCollidePoint(smallerTreeYeild,biggerTreeYeild,settings.treeYeild,event)
                    settings.treeTurnsForYeild=display.adjustableNumButtonCollidePoint(smallerTreeTurn,biggerTreeTurn,settings.treeTurnsForYeild,event)

                    #allow change to yeild and turn per yeild for super
                    settings.superTreeYeild=display.adjustableNumButtonCollidePoint(smallerSuperTreeYeild,biggerSuperTreeYeild,settings.superTreeYeild,event)
                    settings.superTreeTurnsForYeild=display.adjustableNumButtonCollidePoint(smallerSuperTreeTurn,biggerSuperTreeTurn,settings.superTreeTurnsForYeild, event)

                    #allow change to yeild and turn per yeild for spear
                    settings.spearYeild=display.adjustableNumButtonCollidePoint(smallerSpearYeild,biggerSpearYeild,settings.spearYeild,event)
                    settings.spearTurnsForYeild=display.adjustableNumButtonCollidePoint(smallerSpearTurn,biggerSpearTurn, settings.spearYeild,event)

                    #allow change to yeild and turn per yeild for net
                    settings.netYeild=display.adjustableNumButtonCollidePoint(smallerNetYeild,biggerNetYeild,settings.netYeild,event)
                    settings.netTurnsForYeild=display.adjustableNumButtonCollidePoint(smallerNetTurn,biggerNetTurn,settings.netTurnsForYeild,event)

                #change option window
                #trade option window
                if TradeValueButton.collidepoint(event.pos):
                    optionMenu = "Trade"
                #disasters option widnow
                elif DisastersButton.collidepoint(event.pos):
                    optionMenu = "Disasters"
                #misc option window
                elif MiscButton.collidepoint(event.pos):
                    optionMenu = "Misc"
                #yeild option window
                elif YeildButton.collidepoint(event.pos):
                    optionMenu = "Yeild"
                #exit setting options
                elif exitButton.collidepoint(event.pos):
                    return




        #save all the changes to the settings
        settings.save()
        pygame.display.flip()
