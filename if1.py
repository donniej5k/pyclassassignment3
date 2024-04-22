
#1. Nested Decisions: The Adventure Game
#Task 1 code correction
place = str(input("Choose a place: forest or cave? "))

if place == "forest":
    action = str(input("climb a tree or cross a river? "))
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
    torch = str(input("light a torch or proceed in the dark ")) # task 2
    if torch == "light a torch":
        print("Torch is lit")
    elif torch == "proceed in the dark":
        print("No torch proceeding in the dark")
# task 3

else:
    pass