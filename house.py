#   ' match '   Match is a mechanism that, if you've programmed before, is similar in spirit to something called switch in other languages.

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":      # Notice, the use of the single vertical bar |. Much like the or keyword, this allows us to check for multiple values in the same case statement.
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                     # Notice the use of the _ symbol in the last case. This will match with any input, resulting in similar behavior as an else statement.
        print("Who?")