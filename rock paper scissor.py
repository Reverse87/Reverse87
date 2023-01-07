import random
print("Welcome to Rock, Paper, Scissors game!")
choicePlayer = input("Type Rock, Paper, or Scissors to begin.")
choice = ["Rock", "Paper", "Scissors"]
choiceOpponent = random.choice(choice)
if choicePlayer == "Rock" and choiceOpponent == "Paper":
    print("The paper of the opponent covered your rock.")
    print("GAME OVER, you lost !")
elif choicePlayer == "Rock" and choiceOpponent == "Rock":
    print("Your rock and that of the opponent exploding the head by running.")
    print("EDQUALITY.")
elif choicePlayer == "Rock" and choiceOpponent == "Scissors":
    print("Your rock squished the scissors of the opponent.")
    print("CONGRATULATIONS, you won !")
elif choicePlayer == "Paper" and choiceOpponent == "Rock":
    print("Your paper covered the rock of the opponent.")
    print("CONGRATULATIONS, you won !")
elif choicePlayer == "Paper" and choiceOpponent == "Paper":
    print("Your paper and that of the opponent meets and make the love.")
    print("EQUALITY.")
elif choicePlayer == "Paper" and choiceOpponent == "Scissors":
    print("The scissors of the opponent cut your paper.")
    print("GAME OVER, you lost !")
elif choicePlayer == "Scissors" and choiceOpponent == "Rock":
    print("The rock of the opponent squished your scissors.")
    print("GAME OVER, you lost !")
elif choicePlayer == "Scissors" and choiceOpponent == "Paper":
    print("Your scissors cutted the paper of the opponent.")
    print("CONGRATULATIONS, you won !")
elif choicePlayer == "Scissors" and choiceOpponent == "Scissors":
    print("Your scissors and that of the opponent meets and decided to kill the two.")
    print("EQUALITY.")
else:
    print("Sorry, you don't tiped Rock, Paper o Scissors !")
print("Launch the game again to play again.")
