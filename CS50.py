print("what's your name?")
    #print is the function and inside the parenthesis is the argument

name = input()

    #to remove unwanted white spaces in the string...
name = name.strip()
    #to capitalize and title is to capitalize first letter of all words
name = name.capitalize().title()
    #to split
"""first, last = name.split(" ")    """
        #you can also CHAIN functions together
#name = name.strip().title()

    #or even better
"""name = input().strip().title()""" #this is the function assigned to the variable and the overridden parameters all in one line of code

    #name is the variable


"""print("hello, ", end="")
"""
    #end is a parameter for the function print which I can override
#print(name)
    #now, you've override end=\n which creates a new line.
    
    #this is other way of fixing the problem. New feature to python btw.
print(f"hello, {name}")
    # the code above used an f-string
    # the curly bracket prevents the function to literally print "first". In other words, the curly bracket helps recognize a variable and not mistake it for a string
    # and the f is just there for the code to recognize it as an "f string"