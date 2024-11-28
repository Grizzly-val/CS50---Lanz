def age(kek):   #this is how you define your own function. The colon means, all the indented lines of code below  the defined function is gonna be part of that function.
    print("oh, so you're", kek)

print("how old are you? ")
years = input()
age(years)

#def. def for "define"

#bonus
#   def age(kek="world")
#           assigning kek to "world", or what's called a DEFAULT VALUE makes it so that if you put no value when using the function age(), kek will call it's assigned default value
"""
kinda hard to explain
look at line 2
then look at line 1
then look at line 6
when line 6 is ran, line 2 will do  its thing
so it prints the string "oh, so you're", and recognizes kek. So kek looks at line 1, then line 6. In line 6, the variable "years" is inside the parenthesis.
now look at line one. what's going to be printed after "oh, so you're" is whatever's assigned to the variable "years", which is the input of the user.
in short "kek" is what I used to define
and I can use any variable I want to replace that "kek" that I defined
But if I don't put variables. Example, I put age() only instead of age(years), it's going to be an error, because the system will not know what to put for "kek"
so look at line 11. Assigning it to a default value so that even if you put age(), that default value, "world" will be put.
"""

# beware of the bug called scope. If you assign a variable inside a def, that variable will not be available outside that.