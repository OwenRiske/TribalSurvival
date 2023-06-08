#Owen Riske

import pygame
import File

#preset window size
width=1080
height=width*0.75

#screen display
screen=pygame.display.set_mode((width,height))


#get all the settings that have been saved on the file settings.txt
options=File.read_file("settings")



#settings that can be changed
#increased likelyhood of trade with a boat
likelyHoodOfTradeWithBoat=int(options[0])

#resource value in trade
peopleValue=int(options[1])
coconutValue=int(options[2])
treeValue=int(options[3])
superTreeValue=int(options[4])
boatValue=int(options[5])
blanketValue=int(options[6])
medicineValue=int(options[7])
swordValue=int(options[8])
spearValue=int(options[9])
netValue=int(options[10])

#generator information
treeTurnsForYeild=int(options[11])
treeYeild=int(options[12])
superTreeTurnsForYeild=int(options[13])
superTreeYeild=int(options[14])
spearTurnsForYeild=int(options[15])
spearYeild=int(options[16])
netTurnsForYeild=int(options[17])
netYeild=int(options[20])

#disaster information
peopleKilledInBearAttack=int(options[19])
bearAttackLikelyHood=int(options[20])
treeDiseaseLikelyhood=int(options[21])
fishDiseaseLikelyhood=int(options[22])
animalDiseaseLikelyhood=int(options[23])
volcanoLikelyhood=int(options[24])
coldNightLikelyhood=int(options[25])
clearDayLikelyhood=int(options[26])


#reset the screen size
def changeScreenSize():
    pygame.display.set_mode((width,height))

#save the settings that the user can change
def save():
    File.write_file(f"{likelyHoodOfTradeWithBoat}\n{peopleValue}\n{coconutValue}\n{treeValue}\n{superTreeValue}\n{boatValue}\n{blanketValue}\n{medicineValue}\n{swordValue}\n{spearValue}\n{netValue}\n{treeTurnsForYeild}\n{treeYeild}\n{superTreeTurnsForYeild}\n{superTreeYeild}\n{spearTurnsForYeild}\n{spearYeild}\n{netTurnsForYeild}\n{netYeild}\n{peopleKilledInBearAttack}\n{bearAttackLikelyHood}\n{treeDiseaseLikelyhood}\n{fishDiseaseLikelyhood}\n{animalDiseaseLikelyhood}\n{volcanoLikelyhood}\n{coldNightLikelyhood}\n{clearDayLikelyhood}","settings")
