# Problem 3: Swap Two Numbers
# Input two integers a and b separated by space.
# Swap their values and print them in a single line.
# input: 10 20
# output: 20 10
#  input two integers separated by space

a, b = map (int,input("Enter two numbers searated space:").split())
# swap 
a, b = b, a

print (a, b)

# write code explanation here 
# The code takes two integers as input, separated by a space.
# It then swaps their values using tuple unpacking and prints the swapped values in a single line   
# The input is taken as a single line, split into two parts, and converted to integers using the map function.
# The swapping is done using tuple unpacking, which allows for a concise and efficient way to
# swap the values of two variables without needing a temporary variable.
# The final output is printed in a single line, showing the swapped values of a and b   
#