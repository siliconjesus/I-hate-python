available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chose_exit = input("Please choose a direction: ")

print("Congratulations on escaping")