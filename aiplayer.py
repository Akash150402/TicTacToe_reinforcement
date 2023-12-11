
from player import Player 
from state import State 


p1 = Player("p1")
p2 = Player("p2")

st = State(p1, p2)
print("training...")
st.play(10000)

p1.savePolicy()
p2.savePolicy()
p1.loadPolicy("policy_p1")
