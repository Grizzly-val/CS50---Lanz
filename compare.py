#let's compare integers

x = int(input("what's x?"))
y = int(input("what's y?"))

if x < y:         #this is a boolean expression. A boolean expression is basically a yes or no answer to a question
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("they're equal!")

    #the first version were all "ifs". Elif is better because once the question proves to be true, the search will stop.
    #con = this code is better, more efficient.