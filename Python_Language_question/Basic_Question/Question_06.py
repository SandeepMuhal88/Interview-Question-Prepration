print("Enter the number of rows and columns (separated by a comma):")

a= int(input("Enter the number of rows: "))
b=int(input("Enter the number of columns: "))

multilist = [[0 for col in range(b)] for row in range(a)]
for row in range(a):
    for col in range(b):
        multilist[row][col]= row*col
print(multilist)

