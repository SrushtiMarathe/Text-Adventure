def start_game():
    print("Welcome to the Forest of Fate!")
    print("You wake up at a crossroad in a mysterious forest.")
    print("Do you go LEFT toward the mountains or RIGHT toward the river?")

    choice1 = input("Type 'left' or 'right': ").lower()

    if choice1 == "left":
        print("\nYou walk towards the mountains and find a cave.")
        print("Do you ENTER the cave or KEEP walking?")
        choice2 = input("Type 'enter' or 'keep walking': ").lower()

        if choice2 == "enter":
            print("\nYou find a sleeping dragon!")
            print("Do you STEAL the treasure or SNEAK out?")
            choice3 = input("Type 'steal' or 'sneak': ").lower()

            if choice3 == "steal":
                print("\nThe dragon wakes up and roasts you. Game Over!")
            elif choice3 == "sneak":
                print("\nYou sneak out safely. Smart choice! You win!")
            else:
                print("Confused, you trip and the dragon wakes up. Game Over.")

        elif choice2 == "keep walking":
            print("\nYou walk into a bandit ambush. Game Over!")
        else:
            print("You wander off the path and get lost. Game Over.")

    elif choice1 == "right":
        print("\nYou follow the river and find a boat.")
        print("Do you RIDE the boat or FOLLOW the river on foot?")
        choice2 = input("Type 'ride' or 'follow': ").lower()

        if choice2 == "ride":
            print("\nThe boat leads to a hidden village. You're safe! You win!")
        elif choice2 == "follow":
            print("\nYou slip on wet rocks and fall. Game Over!")
        else:
            print("You hesitate and a bear finds you. Game Over.")
    else:
        print("You sit there doing nothing. A tree falls on you. Game Over.")

start_game()

