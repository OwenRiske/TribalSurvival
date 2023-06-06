#Owen Riske

import pygame
import File

settingFile=File.file("settings")
options=File.read_file("settings")
print(options)
width=1080
height=width*0.75

screen=pygame.display.set_mode((width,height))

#increased likelyhood of trade with a boat
likelyHoodOfTradeWithBoat=int(options[1])

#resource value in trade
peopleValue=int(options[2])
coconutValue=int(options[3])
treeValue=int(options[4])
superTreeValue=int(options[5])
boatValue=int(options[6])
blanketValue=int(options[7])
medicineValue=int(options[8])
swordValue=int(options[9])
spearValue=int(options[10])
netValue=int(options[11])

#generator information
treeTurnsForYeild=int(options[12])
treeYeild=int(options[13])
superTreeTurnsForYeild=int(options[14])
superTreeYeild=int(options[15])
spearTurnsForYeild=int(options[16])
spearYeild=int(options[17])
netTurnsForYeild=int(options[18])
netYeild=int(options[19])

#disaster information
peopleKilledInBearAttack=int(options[20])
bearAttackLikelyHood=int(options[21])
treeDiseaseLikelyhood=int(options[22])
fishDiseaseLikelyhood=int(options[23])
animalDiseaseLikelyhood=int(options[24])
volcanoLikelyhood=int(options[25])
coldNightLikelyhood=int(options[26])
clearDayLikelyhood=int(options[27])



def changeScreenSize():
    pygame.display.set_mode((width,height))

def save():
    settingFile.truncate(0)
    settingFile.writelines(f"{likelyHoodOfTradeWithBoat}\n{peopleValue}\n{coconutValue}\n{treeValue}\n{superTreeValue}\n{boatValue}\n{blanketValue}\n{medicineValue}\n{swordValue}\n{spearValue}\n{netValue}\n{treeTurnsForYeild}\n{treeYeild}\n{superTreeTurnsForYeild}\n{superTreeYeild}\n{spearTurnsForYeild}\n{spearYeild}\n{netTurnsForYeild}\n{netYeild}\n{peopleKilledInBearAttack}\n{bearAttackLikelyHood}\n{treeDiseaseLikelyhood}\n{fishDiseaseLikelyhood}\n{animalDiseaseLikelyhood}\n{volcanoLikelyhood}\n{coldNightLikelyhood}\n{clearDayLikelyhood}")
