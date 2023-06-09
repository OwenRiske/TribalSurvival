import random
import settings


#volcano disaster
def volcano(peopleAmount, boatAmount, disasters):
    #if user doesn't have enough boats
    if (boatAmount<=0 and disasters.count("volcano")>0):
        #kill all the peopl
        return 0
    return peopleAmount, disasters

#cold night disaster
def coldNight(peoplAmount, blanketAmount, disasters):
    #if user doesn't have the necessary amount of blankets kill some people
    if blanketAmount<=peoplAmount//2 and disasters.count("cold night")>0:
        return peoplAmount//(2*disasters.count("cold night"))
    return peoplAmount

#bear attack disaster
def bearAttack(peopleAmount, swordAmount, disasters):
    #if user doesn't have enough swords
    if disasters.count("bear attack")>0 and swordAmount<=0:
        #then kill some people
        return peopleAmount-disasters.count("bear attack")
    return peopleAmount

#remove disaster from the disaster array
def removeDisaster(disasterToBeRemoved, disasters):
    if disasters.count(disasterToBeRemoved):
        disasters.remove(disasterToBeRemoved)

    return disasters

#randomly give the user a disaster
def disaster():
    #disaster picker
    disaster=random.randint(1,settings.volcanoLikelyhood+settings.bearAttackLikelyHood+settings.coldNightLikelyhood+settings.clearDayLikelyhood+settings.treeDiseaseLikelyhood+settings.animalDiseaseLikelyhood+settings.fishDiseaseLikelyhood)

    #volcano disaster
    if disaster<=settings.volcanoLikelyhood:
        return "volcano"
    #bear disaster
    elif disaster<=settings.bearAttackLikelyHood+settings.volcanoLikelyhood:
        return "bear attack"
    #cold night disaster
    elif disaster<=settings.coldNightLikelyhood+settings.bearAttackLikelyHood+settings.volcanoLikelyhood:
        return "cold night"
    #tree disease disaster
    elif disaster<=settings.treeDiseaseLikelyhood+settings.coldNightLikelyhood+settings.bearAttackLikelyHood+settings.volcanoLikelyhood:
        return "tree disease"
    #fish disease disaster
    elif disaster<=settings.fishDiseaseLikelyhood+settings.treeDiseaseLikelyhood+settings.coldNightLikelyhood+settings.bearAttackLikelyHood+settings.volcanoLikelyhood:
        return "fish disease"
    #animal disease disaster
    elif disaster<=settings.animalDiseaseLikelyhood+settings.fishDiseaseLikelyhood+settings.treeDiseaseLikelyhood+settings.coldNightLikelyhood+settings.bearAttackLikelyHood+settings.volcanoLikelyhood:
        return "animal disease"
    #clear day (no disaster)
    else:
        return "clear day"