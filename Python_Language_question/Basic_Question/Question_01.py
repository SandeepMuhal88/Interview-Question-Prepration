# def append_list(cal, my_list=[]):
#     my_list.append(cal)
#     return my_list


# print(append_list(1))
# print(append_list(2))
# print(append_list(3, []))
# print(append_list(4))


def append_list(cal, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(cal)
    return my_list


print(append_list(1))
print(append_list(2))
print(append_list(3, []))
print(append_list(4))
