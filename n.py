while True:
    n = int(input("What's n? "))
    if n < 0:
        continue        #continue is continue the loop
    else:
        break           #break is stop the loop

#   but better if you just do:
#       if n > 0:
#           break