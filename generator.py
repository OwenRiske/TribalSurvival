class generator:
    turn=1
    def __init__(self, name, yeild, turnYeild):
        self.yeild=yeild
        self.turnYeild=turnYeild

    def turnGoneBy(self):
        if(self.turn==self.turnYeild):
            turn=1
            return self.yeild
        else:
            self.turn+=1
