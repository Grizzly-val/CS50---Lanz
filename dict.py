"""
dict - DICTIONARY
A data structure that allows you
to associate one value with another.
Literally a dictionary like in the human world.
-
Associate something with something.
"""


#   students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin",}
#       technically, you can do this, but this is hard to read
#   So do this instead when creating a dictionary
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    }

"""
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
"""

for student in students:
    print(student, students[student], sep=", ")

#   student is the variable we assigned to iterate all values in the list/dictionary:students
#   students[student] is basically just us including the value that we assigned to a value, in other words the dictionary that we created. Ex. Ron: Gryffindor
#   sep is just a parameter. A separator. In this case, we used it to separate with a comma.
#   try,  print(student, students, sep=", "). Notice that it print the whole bracket. students[student] basically means that print each value in the dictionary as you iterate.