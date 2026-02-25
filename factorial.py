n=int(input("Enter Factorial No: "))
fact = 1
i = 1
for i in range(1,n):
    fact=fact*i
print("Factorial Of",n,"is",fact)
