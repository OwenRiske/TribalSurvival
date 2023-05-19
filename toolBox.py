import random
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