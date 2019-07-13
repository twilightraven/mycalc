# by WW
# March 2018.

#get the first number "num1" that is not a 0. If the number is invalid, the program will display an error. 
num1 = float(input("Please enter a first number that is not 0: "))
while num1 == 0:
    print("Invalid number. Please try again.")
    num1 = float(input("Please enter a number that is not 0: "))

#display operators
print("Please enter a valid operator: \n1-add\n2-subtract\n3-multiply\n4-divide")
    
#if operator is invalid, the program will display an error
option = 0
choices = [1, 2, 3, 4]
while option not in choices:
    option = int(input("Enter valid operation: 1-Add, 2-Subtract, 3-Multiply, or 4-Divide: "))
    print("Invalid operator. Please try again.")
    option = float(input("Please enter operation (1, 2, 3, or 4): "))

#get the second number "num2" that is not a 0. If the number is invalid, the program will display an error. 
num2 = int(input("Please enter a second number that is not 0: "))
while num2 == 0:
    print("Invalid number. Please try again")
    num2 = float(input("Please enter a number that is not 0: "))
 
#perform addition operation
if option == 1:
    result = num1 + num2
#perform subtraction operation
elif option == 2:
    result = num1 - num2
#perform multiplication operation
elif option == 3:
    result = num1 * num2
#perform division operation
elif option == 4:
    result = num1 / num2

#if other than option, exit program
else:
    print:("Invalid operator")

#display the result
print(result)

#exit the program 
