from ranking import get_items_to_rank
from ranking import create_random_category
ranking_suxfixes = {
    1: "st",
    2: "nd",
    3: "rd",
    4: "th",
    5: "th",
    6: "th",
    7: "th",
    8: "th",
    9: "th",
    10: "th",
    11: "th",
    12: "th",
    13: "th",
    14: "th",
    15: "th",
    16: "th"
}

print("Welcome to Rank Anything")
print("To begin select one of the options below")
print("1: Start new game") # Begins a new game 
print("2: View categories") # todo 
print("3: Add categories") # todo
print("4: Remove categories") # todo

while True:
    choice = input("Please choose from one of the displayed options: ")

    try:
        choice = int(choice)
    except (ValueError, TypeError):
        print("Invalid input")
        print("Please choose from the provided options") 
    if choice == 1:
        items_to_rank = get_items_to_rank()
        print("The category to rank by is: ", create_random_category())
        print(" ")

        print("Now time to rank your items!")

        for i in range (1, len(items_to_rank)):
            print(f"The {i}{ranking_suxfixes[i]} item is {items_to_rank[i]}")
            rank = str(input("Please enter your chosen rank for this item: "))
            items_to_rank[i].choose_rank(rank)
            print("Needs to be finished")
    elif choice == 2:
        print("Working")
        break
    elif choice == 3:
        print("Working")
        break 
    elif choice == 4:
        print("Working")
        break
    else:
        print("Invalid input")
        print("Please choose from the provided options")