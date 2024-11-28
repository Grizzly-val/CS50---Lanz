"""
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)    
"""

#simple code for an addition calculator above.
#int is the integer. Without it, we are going to be adding two values (x and y) as a string instead of an integer, or a NUMBER.
#here's another way to do the code

x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

#just like in mathematics. When looking at a line of code with multiple enclosing parenthesis.
#Start with what's on the very inside then work your way out to the outermost parenthesis.

# under is the more compacted version but harder to understand. Less readable.
#print(int(input("What's x? ")) + int(input("What's y? ")))