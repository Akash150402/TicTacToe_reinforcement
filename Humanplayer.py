from interface import eventt


class HumanPlayer:
    def __init__(self, name):
        self.name = name 
       
    def chooseAction(self, positions):
        
        while True:
         
            action = eventt()
            
            if action in positions:
                return action
    
    # append a hash state
    def addState(self, state):
        pass
    
    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        pass
            
    def reset(self):
        pass

