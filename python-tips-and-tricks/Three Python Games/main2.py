import random

player = 0
cpu = 0

print("three points win the game!")

while player < 3 and cpu < 3:
    cpu_choice = random.choice(["rock", "paper", "scissors"])
    player_choice = input("rock, paper or scissors: ")

    print(f"cpu: {cpu_choice} vs player: {player_choice}")

    if player_choice.lower() == cpu_choice:
        print("tie! no points!")
    elif player_choice.lower() == "rock":
        if cpu_choice == "scissors":
            player += 1
            print(f"player wins! one point!")
        elif cpu_choice == "paper":
            cpu += 1
            print(f"cpu wins! one point!")
    elif player_choice.lower() == "scissors":
        if cpu_choice == "paper":
            player += 1
            print(f"player wins! one point!")
        elif cpu_choice == "rock":
            cpu += 1
            print(f"cpu wins! one point!")
    elif player_choice.lower() == "paper":
        if cpu_choice == "rock":
            player += 1
            print(f"player wins! one point!")
        elif cpu_choice == "scissors":
            cpu += 1
            print(f"cpu wins! one point!")
    else:
        print("invalid input! new round!")

print("player wins!" if player > cpu else "cpu wins!")