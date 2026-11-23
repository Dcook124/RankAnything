from ranking import get_items_to_rank
from ranking import create_random_category
from ranking import categories_to_rank_by
from ranking import Rank 
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
#Creating classes 

S_Rank = Rank("S")
A_Rank = Rank("A")
B_Rank = Rank("B")
C_Rank = Rank("C")
D_Rank = Rank("D")
Ranks = {
    "S" : S_Rank,
    "A" : A_Rank,
    "B" : B_Rank,
    "C" : C_Rank,
    "D" : D_Rank
}
print("Welcome to Rank Anything")
print("To begin select one of the options below")
print("1: Start new game") # Begins a new game 
print("2: View categories") # Displays all the categories stored in categories_to_rank_by 
print("3: Add categories") # Asks user for the category they want to add, appends it to categories_to_rank_by, then prints added category
print("4: Remove categories") # Asks user for the category they want to delete by index, uses del to remove it from categories_to_rank_by
print("5: Exit program") # Exits the program. What did you think this would do?

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

        for i in range(1, len(items_to_rank)):
            print(f"The {i}{ranking_suxfixes[i]} item is {items_to_rank[i]}")
            while True:
                rank = str(input("Please enter your chosen rank for this item: "))
                items_to_rank[i].choose_rank(rank)
                try:
                    Ranks[rank].add_item(items_to_rank[i])
                    break
                except KeyError:
                    print("Please choose from S-A-B-C-D Descending")
        print("Final rankings")
        S_Rank.display_contained_items()
        A_Rank.display_contained_items()
        B_Rank.display_contained_items()
        C_Rank.display_contained_items()
        D_Rank.display_contained_items()

    elif choice == 2:
        for i in range(0, len(categories_to_rank_by)):
            print(f"{i+1}: {categories_to_rank_by[i]}") 

    elif choice == 3:
        new_category = input("Please enter the new category you want to add: ") # Need to safeguard input handling
        categories_to_rank_by.append(new_category)
        print(f"Added '{categories_to_rank_by[-1]}'")

    elif choice == 4:
        print("Please input the number of the category you want removed")
        print("Use option 2 'View categories' to see all categories and their numbers")
        category_to_delete = int(input("Remove category: ")) # Need to safe guard input handling. Make function to check?
        del categories_to_rank_by[category_to_delete-1]
    elif choice == 5:
        print("Ending program. Goodbye")
        break
    else:
        print("Invalid input")
        print("Please choose from the provided options")