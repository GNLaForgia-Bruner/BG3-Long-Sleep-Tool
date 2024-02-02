def ask_completion():
    print("Baldur's Gate 3 - Post-Sleep Tracker")
    print("Open Source & Free - Please support Larian Studios")
    print("Created by: Apollo - Discord: Gruffalo#0000\n")

    options = ['A. Longstrider', 'B. Warding Bond', 'C. Bardic Inspiration', 'D. Potions/Elixirs']
    responses = {}

    for option in options:
        response = input(f"Have you performed {option}? (yes/no): ").lower()
        while response != 'yes':
            if response == 'no':
                print("You must perform this task before proceeding.")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
            response = input(f"Have you performed {option}? (yes/no): ").lower()
        responses[option] = response

    reset = input("Would you like to reset for the next long rest? (yes/no): ").lower()
    while reset != 'yes':
        if reset == 'no':
            print("You must reset for the next long rest.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        reset = input("Would you like to reset for the next long rest? (yes/no): ").lower()

    print("\nResetting responses...")
    ask_completion()

if __name__ == "__main__":
    ask_completion()

