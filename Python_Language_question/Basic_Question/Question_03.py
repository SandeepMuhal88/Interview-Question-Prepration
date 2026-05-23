# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))

# print(','.join(l))


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

print("Calculate the factorial of a number")
x=int(input("Enter a number: "))
print(fact(x))


print("Calculate the squares of numbers from 1 to n")

n=int(input("Enter a number: "))
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)