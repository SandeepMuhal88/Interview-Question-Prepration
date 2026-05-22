# def number(n,m=None):
#     if m is None:
#         m=(n,n)
#     return m


# print(number(5))
# print(number(5,6))

# print(number(90,0))

def append_list(cal, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(cal)
    return my_list


def delete_list(cal, my_list=None):
    if my_list is None:
        my_list = []
    my_list.remove(cal)
    return my_list

print(append_list(1))
print(append_list(2))
print(append_list(3))


