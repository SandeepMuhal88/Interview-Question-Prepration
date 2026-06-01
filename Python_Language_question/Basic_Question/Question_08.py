# num = input("Enter a number: ")

# if num.isdigit():
#     num = int(num)
#     if num % 2 == 0:
#         print(f"{num} is an even number.")
#     else:
#         print(f"{num} is an odd number.")
# else:
#     print("Invalid input! Please enter a valid number.")

while True:
    print("Calculate the Table of a Number:- ")


    number = int(input("Enter a number: "))
    print(f"Table of {number}:")
    for i in range(1,11):
        print(f"{number} x {i} = {number * i}")
    cont = input("Do you want to calculate another table? (yes/no): ").lower()
    if cont != "yes":
        print("Thank you for using the program!")
        break
