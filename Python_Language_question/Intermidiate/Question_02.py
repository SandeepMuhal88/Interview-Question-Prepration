# def sort(list1):
#     list1.sort()
#     return list1


# word = input("Enter a list of words separated by spaces: ").split()
# print(sort(word))


# Advance

def sort(*args):
    list1 = list(args)
    list1.sort()
    return list1


word = input("Enter a list of words separated by spaces: ").split()
print(sort(*word))


