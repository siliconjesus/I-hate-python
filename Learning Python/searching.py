shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

item_to_find = "albatross"
# item_to_find = "spam"
found_at = None
# I guess None ~= null from C/C++
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print(f"Item found at {found_at}")