print("Enter a selection from the below menu.  Press '0' to exit.")
menu_items = ["Bake a loaf of bread", "Bake a pound cake", "Prepare Roast Chicken", "Make Curry", \
    "Put a rack of ribs in the smoker", "Buy dinner out", "Have ice cream", "Sandwiches - again"]

select = None
while True:
    for i in range(len(menu_items)):
        print(f"{i+1}:\t{menu_items[i]}")
    select = int(input("\nMake a selection: "))
    if select == 0:
        print("Shutting down!\n")
        break
    if select > len(menu_items):
        print("I don't have that many options today!\n")
        continue
    select -= 1
    print(f"\nYou selected: {menu_items[select]}\n")