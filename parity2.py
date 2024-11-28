def main():
    The_Number = int(input("What's x? "))
    if is_even(The_Number):
        print("Even")
    else:
        print("Odd")


def is_even(n):                 #shown under this function, is the use of boolean expression to return true or false. From least to most cleanest way.
    """
    if n % 2 == 0:
        return True             #Boolean expression - True/False
    else:
        return False
    """
#   return True if n % 2 == 0 else False

#most elegant way

    return n % 2 == 0 




main()