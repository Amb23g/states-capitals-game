# Name: Andre Batista
# Date: 02.23.2025
# Description: Creating a states and capitals game

# Define main function
def main():
    # Declare and initialize variables
    # strings for name and menuChoice
    userName = menuChoice = ""

    # Display Intro
    print("WELCOME TO THE CAPITAL PROGRAM!!\n")

    # Prompt for name
    userName = input("First, let me get your name: ")
        
    #This is the inner loop it will loop until the user types E
    while menuChoice != "E" and menuChoice != "e":
        # Display state options
        print("\nPlease choose from the following menu:")
        print("A) PA",
              "B) SC", 
              "C) GA",
              "D) FL",
              "E) Exit",
              sep = "\n")

        # Prompt for menuChoice
        menuChoice = input("\nEnter your choice here: ")

        # Selection structure to determine which capital to display to user
        if menuChoice == "A" or menuChoice == "a" or menuChoice == "PA":
            print("The Capital of Pennslyvania is Harrisburg")
        elif menuChoice == "B" or menuChoice == "b" or menuChoice == "SC":
            print("The Capital of South Carolina is Columbia")
        elif menuChoice == "C" or menuChoice == "c" or menuChoice == "GA":
            print("The Capital of Georgia is Atlanta")
        elif menuChoice == "D" or menuChoice == "d" or menuChoice == "FL":
            print("The Capital of Florida is Tallahassee")
        elif menuChoice == "E" or menuChoice == "e":
            print("Sorry to see you go...Until next time!")
        else:
            print("Sorry, you must choose A, B, C, D, or E.")

    # Display Outro
    print(f"\nThank you {userName} for playing my State and Capitals game!")
        
main()
