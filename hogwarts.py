students = ["Hermione", "Harry", "Ron"]

#   print(students[0])          #   So student[0] is "Hermione", [1], is "Harry", and so on.
#   print(students[1]) 
#   print(students[2]) 

"""
for student in students:
    print(student)
"""

# len : or length - will tell you the length of a list and other things down the line, too.

for i in range(len(students)):      #   the range function expects an integer. That's why under normal circumstances, it wouldn't accept a variable or string. This is where len comes in.
    print(i + 1, students[i])
