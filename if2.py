# 2. Quick Decisions: The Event Planner
# Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue Selection

ap = "projector" if attendees > 100 else "audio system"
print(ap)

# task 3
# Task 3: Catering Choices

# Ask the user if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes, 
# otherwise recommend "Gourmet Meals Caterers".

food = str(input("Would you like vegetarian food? (yes/no)"))
f = "Veggie Delight Caterers" if food == "yes" else "Gourmet Meals Caterers"
print(f)