a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
print("Select the arithmetic operation: ")
c=input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
if c == "1" :
        d = a + b
elif c == "2" :
        d = a - b
elif c == "3" :
        d = a * b
elif c == "4" :
        d = a / b
else :
        print("Invalid selection!")
print("The result is ", d)
input()
