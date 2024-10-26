import random
import os
import time

def clear_screen():
    # Clear the screen based on the operating system
    os.system("cls" if os.name == "nt" else "clear")

counter_comp = 0
counter_player = 0

while True:
    clear_screen()
    print("______Choose______")
    print("1. Snake\n2. Water\n3. Gun\n4. Quit")

    try:
        choice = int(input("\nEnter your choice (1/2/3 or 4 to quit): "))
        
        if choice == 4:
            print("\nExiting the game...")
            print(f"Final Scores -> Bot: {counter_comp}, You: {counter_player}")
            break
        elif choice not in [1, 2, 3]:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            input("Press Enter to continue...")
            continue
        
        comp_choice = random.choice([1, 2, 3])
        print(f"Bot's Choice: {comp_choice}")

        if choice == comp_choice:
            print("\nIt's a Draw!\n")

        elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
            counter_player += 1
            print("\nYou Won!\n")

        else:
            counter_comp += 1
            print("\nYou Lost!\n")
        
        print(f"Score -> Bot: {counter_comp}, You: {counter_player}")
        input("Press Enter to continue...")

    except ValueError:
        print("Invalid input. Please enter a number.")
        input("Press Enter to continue...")

