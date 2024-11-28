distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58, 
    "Pioneer 11": 44, 
}

#   def main():
#    for names in distances.keys():
#       print(f"{names} is {distances[names]} AU away from Earth")

def main():
    for distance in distances.values():
        print(f"{distance} AU is equivalent to {convert(distance)} m")

def convert(au):
    return au * 149597870700

main()

#   distances.keys      focuses on the keys of a dictionary. In this case, the spacecrafts.
#   distances.values    focuses on the values of a dictionary. In this case, the distances.