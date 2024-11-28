def greet(reply):
    if "hello" in reply:
       return "hello there!"
    else:
        return "wtf?"

rawr = input("What's up!")
greeting = greet(rawr)
print("Yoo, " + greeting)