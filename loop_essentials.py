"""
    while
    while True
    for

List
_ = ["", "", "", "", ""]

for _ in range():

The way that for loop works is that it creates
for you a variable that I've called i, but I could call it anything I want.
It then assigns i initially to the first thing (0) in the list.
It then automatically assigns i to the next thing (1) in the list.
And then it assigns i to the third thing (2) in the list.
And each time, it does all of the indented code underneath.

for i in [0, 1, 2]:
    print("meow")

We realize, though, that this is not going
to scale well if I want to do something like a million times.
So we introduced range instead.
That has the effect of doing the same thing.
It returns to me a range of values-- a list of three things, really,
so the behavior is exactly the same.

"""