import random


def volcano(peopleAmount, boatAmount):
    if (boatAmount<=0):
        return 0
    return peopleAmount

def coldNight(peoplAmount, blanketAmount):
    if(blanketAmount<=0):
        return 0
    return peoplAmount

def bearAttack(peopleAmount, swordAmount):
    if(swordAmount<=0):
        return 0
    return peopleAmount

def treeDisease(treeAmount, superTreeAmount):
    return (treeAmount*-1)+(superTreeAmount*-2)


def randomDisaster(peopleAmount, coconutAmount,boatAmount, blanketAmount, swordAmount, treeAmount, superTreeAmount):
    event= random.randint(1, 3)

    if event==1:
        peopleAmount=volcano(peopleAmount, boatAmount)

    elif event==2:
        peopleAmount=coldNight(peopleAmount,blanketAmount)
    elif event==3:
        peopleAmount=bearAttack(peopleAmount,swordAmount)
    elif event==4:
        coconutAmount+=treeDisease(treeAmount,superTreeAmount)

    return peopleAmount, coconutAmount