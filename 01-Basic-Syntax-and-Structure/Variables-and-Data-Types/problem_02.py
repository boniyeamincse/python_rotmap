"""🪐 Problem 2: Even or Odd
Input an integer n.
Print "Even" if n is even, otherwise print "Odd".
example :

"""

# input a int number 
even_odd = int(input("Input Here :"))
print(even_odd)
if (even_odd % 2 == 0):
    print("The Number is Even")
else:
    print("The number is odd")

# note : what the logic behind this code?
# The code checks if the input number is even or odd by using the modulus operator (%).
# If the remainder when the number is divided by 2 is 0, it is even; otherwise, it is odd.
# The if-else statement is used to print the appropriate message based on the result of this check.
# The input is taken as an integer, and the result is printed accordingly.      
# why using if-else statement here?
# The if-else statement is used to control the flow of the program based on the condition       
# whether the number is even or odd. If the condition (even_odd % 2 == 0) is true, it executes the code block for even numbers; otherwise, it executes the code block for odd numbers.
# This allows the program to provide different outputs based on the input value.


