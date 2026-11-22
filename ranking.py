import random

categories_to_rank_by: list[str] = ["Who would make the best therapist?", "Who would make the best football coach?",
                         "Who would make the best frontman in a band?", "Who would make the best sandwich?",
                         "Who would be the best actor?"]
class Item:
    """
    Item class creates items to be placed in ranks

    When an Item is ranked it is both put into the contains list for a Rank obj 
    and has that rank stored in self.rank 

    the __repr__ method allows it to be printed cleanly 

    choose_rank is a setter method 
    """
    def __init__(self,name) -> None:
        self.name = name 
        self.rank = ""

    def __repr__(self) -> None:
        return f"{self.name}"
    
    def choose_rank(self, rank) -> None:
        self.rank = rank

class Rank:
    """
    Rank class is used to create ranks to hold the items that get placed in a certain class
    """
    def __init__(self, contains, rank) -> None:
        self.rank = rank
        self.contains = []
    
    def __repr__(self) -> None:
        return f"{self.rank} rank"

#Gets the items to be ranked by the user 

def get_items_to_rank() -> list["Item"]:
    items_to_rank: list["Item"] = [None] # items_to_rank has a None type at index 0 so number prefixes can be properly applied 
    num_items = int(input("Please enter how many items you want to rank from 4 - 16: "))
    if num_items < 4:
        print("Cannot rank less than 4 items")
    elif num_items > 16:
        print("Cannot rank more than 16 items")
    elif int(num_items) is False:
        print("Please input a number between 4 - 16")
    else:
        for i in range(0, num_items):
            item = input("Enter the next item to rank: ")
            items_to_rank.append(Item(item))
    return items_to_rank

# Uses random  library to choose a random entry from the categories_to_rank_by list
def create_random_category() -> str:
    return categories_to_rank_by[random.randint(0, len(categories_to_rank_by))]
