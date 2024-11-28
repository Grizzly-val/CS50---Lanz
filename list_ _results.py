results = ["Mario", "Luigi"]

results.append("Princess")
#   Append adds a new element to the end of a list.
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")
results.extend(["Bowser", "Donkey Kong Jr."])   #Extends the list with a list
results.remove("Toad")  # Removes "Toad"
results.insert(0, "Toad")  # Adds / Inserts "Toad" into the nth place, which in this case, "0", or the very first place.



print(results)