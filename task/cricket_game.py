import random

game = """
            GAME = IPL

            SELECT YOUR TEAM

            1) CSK
            2) GT
            3) RCB
            4) LSG
            5) MI
            6) KKR
            7) RR
            8) K11P
            9) DC
            10) SRH

        """
toss = """
            TOSS

        (HEAD / TAILS)

        
"""

BAT_BALL = """
            BAT AND BALL

        CHOOSE 1 FOR BAT AND 2 FOR BALL : BAT 
"""


print(game)
game_list = ["CSK","GT","RCB","LSG","MI","KKR","RR","K11P","DC","SRH"]

print(toss)
toss_list = ["HEAD","TAILS"]

print(BAT_BALL)
BAT_BALL_list = ["CHOOSE 1 FOR BAT AND 2 FOR BALL :  "]

status = True

c_score = 0
u_score = 0

while status:

    U_team_choice = input("Enter your team : ").upper()
    computer_team= random.choice(game_list).upper()
    computer_toss = random.choice(toss_list)
    computer_BAT_BALL = random.choice(BAT_BALL)
   

    
    print(f"COMPUTER SELECTED TEAM :{computer_team}")
    print(f" USER SELECTED TOSS : {computer_toss}")
   
    print= input("select the bat_ball : ")

    

    print(f"USER SELECTED TEAM :{U_team_choice}")

    if U_team_choice == computer_team:
        print("TIE")
    elif U_team_choice !=computer_team :
        print("WON !!!!")
         