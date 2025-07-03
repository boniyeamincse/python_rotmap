"""
 Problem 1: Sum of Two Numbers
Input two integers in a single line separated by space.
Print their sum.

input : 5 7  
output : 12

"""
# single line input intriger types variable 
var_1, var_2 = map(int , input().split())
#var_1 =
#var_2 = 
total = var_1 + var_2
print(total)


# note : why using map function here?
# The map function applies the int function to each element of the input list,
# converting them from strings to integers in a single line.# This is a common pattern in Python for reading multiple inputs in a single line.
# why using split() function here?
# The split() function is used to split the input string into a list of substrings based on whitespace.
# In this case, it splits the input string into two parts, which are then converted to integers using the map function.
# This allows for a more concise and efficient way to read multiple inputs in a single line.