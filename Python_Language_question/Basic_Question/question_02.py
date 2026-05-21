import sys

# List Comprehension (uses [])
list_comp = [x**2 for x in range(10000)]
print(sys.getsizeof(list_comp)) # ~87616 bytes

# Generator Expression (uses ())
gen_expr = (x**2 for x in range(10000))
print(sys.getsizeof(gen_expr))  # ~104 bytes