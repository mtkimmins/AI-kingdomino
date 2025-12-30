
####################################################
class State:
    def __init__(self) -> None:
        pass

##################################################

class AdversarialNetwork:
    def __init__(self) -> None:
        self.goal_state = 1
        self.minimax_depth = 10
    
    def getUtility(self,state)->float:
        utility = 0.0
        return utility
    
    def getTerminal(self,state)->bool:
        terminal = False
        return terminal
    
    def minimax(self):
        pass

    def abPruning(self):
        pass