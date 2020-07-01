string = "abcdefghij"

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for char in string:
#     print(char)

# for char in iter(string):
#     print(char)

my_iterator = iter(string)
size = len(string)
i = 0

while i < size:
    print(next(my_iterator))
    i += 1