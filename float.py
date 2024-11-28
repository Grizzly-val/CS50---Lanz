#float is different from integers
#float is where the numbers have decimals
#  float = float
#  integers = int


x = float(input("What's x? "))
y = float(input("What's y? "))

#   print(round(x + y))

z = round(x / y, 2)
#   function round rounds up a number
#   round(number, ndigits=None) doc

# use an f string
print(f"{z:,}")
#   the code above prints {z} so that the integers will be displayed with commas

"""
    you can also do...
print(f"{z:.2f}")
    this has the same function as line 12.
    think of it as 2f for 2 floats, or rounding the number to 2 decimal points.
    consider this as the F-STRING approach for what we're trying to do with line 12
"""