import random

print("Snake Water Gun")


def name(x):
    return "Snake" if x == "s" else "Water" if x == "w" else "Gun"


computer_score = 0
player_score = 0
i = 0
while i < 10:
    computer = random.choice(["s", "w", "g"])
    player = input("Snake(S) Water(W) Gun(G): ")
    player = player.lower()
    if player not in ["s", "w", "g"]:
        print("You are a noob")
        print("You are a noob")
        print("You are a noob")
        print("You are a noob")
        print("You are a noob")
        print("You are a noob")
        break
    if ((player == "s") and (computer == "s")) or ((player == "w") and (computer == "w")) or (
            (player == "g") and (computer == "g")):
        print(f"computer picked {name(computer)}")
        print("Draw")
        print()
    elif ((player == "s") and (computer == "w")) or ((player == "w") and (computer == "g")) or (
            (player == "g") and (computer == "s")):
        print(f"computer picked {name(computer)}")
        print("You Win!!")
        print()
        player_score += 1
    else:
        print(f"computer picked {name(computer)}")
        print("You Lose")
        print()
        computer_score += 1
    i += 1

print("_____________________________")
print("final score is")
print(f"{player_score} - {computer_score}")
if player_score == computer_score:
    print("Draw")
if player_score > computer_score:
    print("You Win!!!")
if player_score < computer_score:
    print("You Lose")
