import random
import settings


def volcano(peopleAmount, boatAmount, disasters):
    if (boatAmount<=0 and disasters.count("volcano")>0):
        return 0
    return peopleAmount, disasters

def coldNight(peoplAmount, blanketAmount, disasters):
    if blanketAmount<=peoplAmount//2 and disasters.count("cold night")>0:
        return peoplAmount//(2*disasters.count("cold night"))
    return peoplAmount

def bearAttack(peopleAmount, swordAmount, disasters):
    if disasters.count("bear attack")>0 and swordAmount<=0:
        return peopleAmount-disasters.count("bear attack"), removeDisasterFromTheArray(disasters, "bear attack")


def removeDisasterFromTheArray(disasters, disasterToBeRemoved):
    if disasters.count(disasterToBeRemoved)!=0:
        print(disasters.remove(6))
        return disasters.remove(disasterToBeRemoved)
    return disasters

def disaster():
    disaster=random.randint(1,settings.volcanoLikelyhood+settings.bearAttackLikelyHood+settings.coldNightLikelyhood+settings.clearDayLikelyhood+settings.treeDiseaseLikelyhood+settings.animalDiseaseLikelyhood+settings.fishDiseaseLikelyhood)

    if disaster<=settings.volcanoLikelyhood:
        return "volcano"
    elif disaster<=settings.bearAttackLikelyHood+settings.volcanoLikelyhood:
        return "bear attack"
    elif disaster<=settings.coldNightLikelyhood+settings.bearAttackLikelyHood+settings.volcanoLikelyhood:
        return "cold night"
    elif disaster<=settings.treeDiseaseLikelyhood+settings.coldNightLikelyhood+settings.bearAttackLikelyHood+settings.volcanoLikelyhood:
        return "tree disease"
    elif disaster<=settings.fishDiseaseLikelyhood+settings.treeDiseaseLikelyhood+settings.coldNightLikelyhood+settings.bearAttackLikelyHood+settings.volcanoLikelyhood:
        return "fish disease"
    elif disaster<=settings.animalDiseaseLikelyhood+settings.fishDiseaseLikelyhood+settings.treeDiseaseLikelyhood+settings.coldNightLikelyhood+settings.bearAttackLikelyHood+settings.volcanoLikelyhood:
        return "animal disease"
    else:
        return "clear day"