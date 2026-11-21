import random
# Expand later. Maybe find online repo? 
#Give players choice to add their own categories?

categories_to_rank_by: list[str] = ["Who would make the best therapist?", "Who would make the best football coach?",
                         "Who would make the best frontman in a band?", "Who would make the best sandwich?",
                         "Who would be the best actor?"]

#Gets the items to be ranked by the user.
#Possibly create class later? unsure if neccessary 

def get_items_to_rank() -> list:
    items_to_rank: list = [None]
    num_items = int(input("Please enter how many items you want to rank from 4 - 16: "))
    if num_items < 4:
        raise Exception("Cannot rank less than 4 items")
    elif num_items > 16:
        raise Exception("Cannot rank more than 16 items")
    elif int(num_items) is False:
        raise Exception("Please input a number between 4 - 16")
    else:
        for i in range(0, num_items):
            item = input("Enter the next item to rank: ")
            items_to_rank.append(item)
    return items_to_rank

# Uses random  library to choose a random entry from the categories_to_rank_by list
def create_random_category() -> str:
    return categories_to_rank_by[random.randint(0, len(categories_to_rank_by))]