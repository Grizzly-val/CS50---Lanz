#   loops - ability to do something again and again

# while

i = 10
while i != 0:
    print(i)
    i = i - 1

#line 5 : i = 10
#line 6 : state a "while" loop. "WHILE i IS NOT EQUAL TO 10, DO THIS."
#line 7 : print i, which is 10
#line 8 : i - 1. So 10 - 1, which becomes 9
#   go back to line 7. Print i, which is now 9.
#   line 8 again : i - 1, which is 9 - 1, which becomes 8.
#   and so on, until we reach 0.