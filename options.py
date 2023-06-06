#Owen Riske

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
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    settingAlterMenu()

        settings.save()
        pygame.display.flip()

def settingAlterMenu():
    pygame.init()
    optionMenu="Misc"

    menuPage=1

    while True:
        settings.screen.fill((250, 250, 250))

        exitButton=exitSquare(settings.width*0.045,settings.height*0.05,settings.width*0.05,(250,250,250))


        if optionMenu=="Misc":
            smallerBoatLikelyHoodButton, biggerBoatLikelyHoodButton=display.adjustableNum("Boat Trade Likely Hood", str(settings.likelyHoodOfTradeWithBoat),settings.height*0.075,(0,0,0))
        elif optionMenu=="Disasters":

            smallerBearKillHoodButton,biggerBearKillHoodButton=display.adjustableNum("Bear Attack Kill", str(settings.peopleKilledInBearAttack), settings.height*0.075, (0,0,0))

            smallerBearLikelyHoodButton,biggerBearLikelyHoodButton=display.adjustableNum("Bear Likely Hood",str(settings.bearAttackLikelyHood),settings.height*0.175,(0,0,0))

            smallerVolcanoLikelyHoodButton, biggerVolcanoLikelyHoodButton=display.adjustableNum("Volcano Likely Hood", str(settings.volcanoLikelyhood),settings.height*0.275,(0,0,0))

            smallerColdNightLikelyHoodButton, biggerColdNightLikelyHoodButton=display.adjustableNum("Cold Night Likely Hood", str(settings.coldNightLikelyhood),settings.height*0.375,(0,0,0))
            smallerTreeDiseaseLikelyHoodButton, biggerTreeDiseaseLikelyHoodButton=display.adjustableNum("Tree Disease Likely Hood", str(settings.treeDiseaseLikelyhood),settings.height*0.475,(0,0,0))
            smallerFishDiseaseLikelyHoodButton, biggerFishDiseaseLikelyHoodButton=display.adjustableNum("Fish Disease Likely Hood", str(settings.fishDiseaseLikelyhood),settings.height*0.575,(0,0,0))
            smallerAnimalDiseaseLikelyHoodButton, biggerAnimalDiseaseLikelyHoodButton=display.adjustableNum("Animal Disease Likely Hood", str(settings.animalDiseaseLikelyhood),settings.height*0.675,(0,0,0))

        elif optionMenu=="Trade":
            if menuPage==1:
                smallerPeopleValue, biggerPeopleValue=display.adjustableNum("People Value", str(settings.peopleValue),settings.height*0.075,(0,0,0))
                smallerCoconutValue, biggerCoconutValue=display.adjustableNum("Coconut Value", str(settings.coconutValue),settings.height*0.175,(0,0,0))
                smallerBoatValue, biggerBoatValue=display.adjustableNum("Boat Value", str(settings.boatValue),settings.height*0.275,(0,0,0))
                smallerMedicineValue, biggerMedicineValue=display.adjustableNum("Medicine Value", str(settings.medicineValue),settings.height*0.375,(0,0,0))
                smallerBlanketValue, biggerBlanketValue=display.adjustableNum("Blanket Value", str(settings.blanketValue),settings.height*0.475,(0,0,0))

            elif menuPage==2:
                smallerSwordValue, biggerSwordValue = display.adjustableNum("Sword Value", str(settings.swordValue),
                                                                          settings.height * 0.075, (0, 0, 0))
                smallerSpearValue, biggerSpearValue = display.adjustableNum("Spear Value", str(settings.spearValue),
                                                                          settings.height * 0.175, (0, 0, 0))
                smallerNetValue, biggerNetValue = display.adjustableNum("Net Value", str(settings.netValue),
                                                                          settings.height * 0.275, (0, 0, 0))
                smallerTreeValue, biggerTreeValue = display.adjustableNum("Tree Value", str(settings.TreeValue),
                                                                          settings.height * 0.375, (0, 0, 0))
                smallerSuperTreeValue, biggerSuperTreeValue=display("Super Tree Value", str(settings.superTreeValue),settings.height(0.475), (0,0,0))
            else:
                menuPage=1

            smallerPage, biggerPage=display.adjustableNum("Trade Value Page", str(menuPage),settings.height*0.675,(0,0,0))
        elif optionMenu=="Yeild":
            smallerTreeYeild, biggerTreeYeild=display.adjustableNum("Tree Yield", str(settings.treeYeild),settings.height*0.075,(0,0,0))
            smallerTreeTurn, biggerTreeTurn=display.adjustableNum("Tree Turns Per Yield",str(settings.treeTurnsForYeild),settings.height*0.175,(0,0,0))
            smallerSuperTreeYeild, biggerSuperTreeYeild=display.adjustableNum("Super Tree Yield", str(settings.superTreeYeild),settings.height*0.275,(0,0,0))
            smallerSuperTreeTurn, biggerSuperTreeTurn=display.adjustableNum("Super Tree Turns Per Yield",str(settings.superTreeTurnsForYeild),settings.height*0.375,(0,0,0))
            smallerSpearYeild, biggerSpearYeild=display.adjustableNum("Spear Yield", str(settings.spearValue),settings.height*0.475,(0,0,0))
            smallerSpearTurn, biggerSpearTurn=display.adjustableNum("Spear Turns Per Yield",str(settings.spearTurnsForYeild),settings.height*0.575,(0,0,0))
            smallerNetYeild, biggerNetYeild=display.adjustableNum("Net Yield", str(settings.netYeild),settings.height*0.675,(0,0,0))
            smallerNetTurn, biggerNetTurn=display.adjustableNum("Net Turns Per Yield",str(settings.netTurnsForYeild),settings.height*0.775,(0,0,0))
















        TradeValueButton=display.button("Trade Value",settings.width*0.245,settings.width*0.24,settings.width*0.125,settings.height*0.895, (0,0,0))
        DisastersButton=display.button("Disaster",settings.width*0.245,settings.width*0.24,settings.width*0.375,settings.height*0.895, (0,0,0))
        MiscButton=display.button("Misc.",settings.width*0.245,settings.width*0.24,settings.width*0.875,settings.height*0.895, (0,0,0))
        YeildButton=display.button("Coconut Yeilds",settings.width*0.245,settings.width*0.1975,settings.width*0.625,settings.height*0.895, (0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if optionMenu == "Misc":
                    settings.likelyHoodOfTradeWithBoat=display.adjustableNumButtonCollidePoint(smallerBoatLikelyHoodButton,biggerBoatLikelyHoodButton,settings.likelyHoodOfTradeWithBoat,event)

                elif optionMenu == "Disaster":
                    settings.peopleKilledInBearAttack=display.adjustableNumButtonCollidePoint(smallerBearKillHoodButton, biggerBearKillHoodButton,settings.peopleKilledInBearAttack, event)

                    settings.bearAttackLikelyHood=display.adjustableNumButtonCollidePoint(smallerBearLikelyHoodButton,biggerBearLikelyHoodButton,settings.bearAttackLikelyHood,event)

                    settings.volcanoLikelyhood=display.adjustableNumButtonCollidePoint(smallerVolcanoLikelyHoodButton,biggerVolcanoLikelyHoodButton,settings.volcanoLikelyhood,event)

                    settings.coldNightLikelyhood=display.adjustableNumButtonCollidePoint(smallerColdNightLikelyHoodButton,biggerColdNightLikelyHoodButton,settings.coldNightLikelyhood,event)

                    settings.treeDiseaseLikelyhood=display.adjustableNumButtonCollidePoint(smallerTreeDiseaseLikelyHoodButton,biggerTreeDiseaseLikelyHoodButton,settings.treeDiseaseLikelyhood,event)

                    settings.fishDiseaseLikelyhood=display.adjustableNumButtonCollidePoint(smallerFishDiseaseLikelyHoodButton,biggerFishDiseaseLikelyHoodButton,settings.fishDiseaseLikelyhood,event)

                    settings.animalDiseaseLikelyhood=display.adjustableNumButtonCollidePoint(smallerAnimalDiseaseLikelyHoodButton, biggerAnimalDiseaseLikelyHoodButton,settings.animalDiseaseLikelyhood, event)

                elif optionMenu == "Trade":
                    if menuPage==1:
                        settings.peopleValue=display.adjustableNumButtonCollidePoint(smallerPeopleValue,biggerPeopleValue,settings.peopleValue,event)

                        settings.coconutValue=display.adjustableNumButtonCollidePoint(smallerCoconutValue,biggerCoconutValue,settings.coconutValue,event)

                        settings.boatValue=display.adjustableNumButtonCollidePoint(smallerBoatValue,biggerBoatValue,settings.boatValue,event)

                        settings.medicineValue=display.adjustableNumButtonCollidePoint(smallerMedicineValue,biggerMedicineValue, settings.medicineValue, event)

                        settings.blanketValue=display.adjustableNumButtonCollidePoint(smallerBlanketValue,biggerBlanketValue,settings.blanketValue,event)
                    elif menuPage==2:
                        settings.swordValue=display.adjustableNumButtonCollidePoint(smallerSwordValue, biggerSwordValue,settings.swordValue,event)

                        settings.spearValue=display.adjustableNumButtonCollidePoint(smallerSpearValue,biggerSpearValue,settings.spearValue,event)

                        settings.netValue=display.adjustableNumButtonCollidePoint(smallerNetValue,biggerNetValue,settings.netValue,event)

                        settings.treeValue=display.adjustableNumButtonCollidePoint(smallerTreeValue,biggerTreeValue,settings.treeValue)

                    menuPage = display.adjustableNumButtonCollidePointWithMax(smallerPage, biggerPage, menuPage, 2,
                                                                              event)


                elif optionMenu == "Yeild":

                    #settings.superTreeValue=display.adjustableNumButtonCollidePoint(smallerSuperTreeValue,biggerSuperTreeValue,settings.superTreeValue,event)

                    settings.treeYeild=display.adjustableNumButtonCollidePoint(smallerTreeYeild,biggerTreeYeild,settings.treeYeild,event)

                    settings.treeTurnsForYeild=display.adjustableNumButtonCollidePoint(smallerTreeTurn,biggerTreeTurn,settings.treeTurnsForYeild,event)

                    settings.superTreeYeild=display.adjustableNumButtonCollidePoint(smallerSuperTreeYeild,biggerSuperTreeYeild,settings.superTreeYeild,event)

                    settings.superTreeTurnsForYeild=display.adjustableNumButtonCollidePoint(smallerSuperTreeTurn,biggerSuperTreeTurn,settings.superTreeTurnsForYeild, event)

                    settings.spearYeild=display.adjustableNumButtonCollidePoint(smallerSpearYeild,biggerSpearYeild,settings.spearYeild,event)

                    settings.spearTurnsForYeild=display.adjustableNumButtonCollidePoint(smallerSpearTurn,biggerSpearTurn, settings.spearYeild,event)

                    settings.netYeild=display.adjustableNumButtonCollidePoint(smallerNetYeild,biggerNetYeild,settings.netYeild,event)

                    settings.netTurnsForYeild=display.adjustableNumButtonCollidePoint(smallerNetTurn,biggerNetTurn,settings.netTurnsForYeild,event)

                if TradeValueButton.collidepoint(event.pos):
                    optionMenu = "Trade"
                elif DisastersButton.collidepoint(event.pos):
                    optionMenu = "Disasters"
                elif MiscButton.collidepoint(event.pos):
                    optionMenu = "Misc"
                elif YeildButton.collidepoint(event.pos):
                    optionMenu = "Yeild"

                elif exitButton.collidepoint(event.pos):
                    return






        pygame.display.flip()
