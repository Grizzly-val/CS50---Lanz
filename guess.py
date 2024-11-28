#guessing game
#lesson about variables

#       guess = 10 
#whereas guess is the variable and 10 is the value we're assigning to that variable

def get_guess():
    guess = int(input("Take a guess: "))
    return guess

def main():
    guess = get_guess()
    if guess == 25:
        print("Nice!")
    else:
        print("HAHAHA! Try again.")
    

main()