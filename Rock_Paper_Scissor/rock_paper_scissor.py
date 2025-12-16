import random 

user_move = int(input("Enter your move (0: Rock, 1: Paper, 2: Scissor): "))
moves = ["Rock","Paper","Scissor"]

print(f"You choosed '{moves[user_move]}'")

def comp_move():
    return random.randint(0, 2)


if user_move == comp_move():
    print("You both matched")
    print("It's a Tie!")

elif (user_move == 0 and comp_move() == 2) or (user_move == 1 and comp_move() == 0):
    if comp_move() == 2 :
      print("Computer choosed 'Scissor'")
      print("Congratulations🔥🔥, You won!!!")
    else :
      print("Computer choosed 'Rock'")
      print("Congratulations🔥🔥, You won!!!")

elif (user_move == 0 and comp_move() == 1) or (user_move == 1 and comp_move() == 2) or (user_move == 2 and comp_move() == 0):
    if comp_move() == 1 :
      print("Computer choosed 'Paper'")
      print("Oops you lost 😒, better luck next time.")
    elif comp_move() == 2 :
      print("Computer choosed 'Scissor'")
      print("Oops you lost 😒, better luck next time.")
    else:
      print("Computer choosed 'Rock'")
      print("Oops you lost 😒, better luck next time.")

elif (user_move == 2 and comp_move() == 1):
    print("Computer choosed 'Paper'")
    print("Congratulations🔥🔥, You won!!!")
