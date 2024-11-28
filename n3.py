def main():
    number = get_number()
    meow(number)


def get_number():
    n = int(input("How many meows? "))
    while n > 0:
        break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()