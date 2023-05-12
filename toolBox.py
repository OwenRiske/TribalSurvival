def feed(peopleAmount, coconutCount):
    if(peopleAmount>coconutCount):
        peopleAmount-=peopleAmount-coconutCount
        coconutCount=0
    else:
        coconutCount-=peopleAmount

    return peopleAmount, coconutCount


def absoluteValue(input):
    if(input<0):
        input*=-1
    return input

def positiveOnly(input):
    if(input<0):
        input=0
    return input