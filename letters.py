def main():
    guests = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for i in range(len(guests)):    # len is the length of the list. It covers everything in the list. The range function expects an integer, so we need this.
        print(write_letter(guests[i], "Princess Peach"))

"""
for name in names:
    print(name, "Princess Peach"))
"""

def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are invited to
        my Birthday WRRAHHHH.
        Pls come!

        It is I, {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

#    These are not curly braces for a dictionary.
#    These are curly braces for interpolating some value. For f-string

main()

"""
print(write_letter("Mario", "Princess Peach"))
print(write_letter("Luigi", "Princess Peach"))
print(write_letter("Daisy", "Princess Peach"))
print(write_letter("Yoshi", "Princess Peach"))
    we pretty much created a code better than this in the main().
"""