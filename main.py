import sys,pygame
from player import Player 
from state import State 
from Humanplayer import HumanPlayer 
from interface import restart,reset_play
BOARD_ROWS = 3
BOARD_COLS = 3


while True:
    print("\n1.One player vs AI\n2.Two players\n3.Exit")
    choice=int(input("Enter your choice"))
    
    pygame.display.update()
    if choice == 2:
        p1 = HumanPlayer(input("Enter player1 name:"))
        p2 = HumanPlayer(input("Enter player2 name:"))
        st = State(p1,p2)
        st.play3()
        global player
        reset_play()
        restart()
       
        
        
    elif choice == 1:
        p1 = Player("computer", exp_rate=0)
        p1.loadPolicy("policy_p1")
        p2 = HumanPlayer(input("Enter player name:"))
        st = State(p1, p2)
        st.play2()
        global player
        reset_play()
        restart()
        
        
    elif choice == 3:
        sys.exit()
    else:
        print("Enter correct input")
    