def main():
    #sc_details = {"name": "Voyager 1", "distance": 170}

    sc_details = {"name": "James Webb Telescope"}
    sc_details["distance"] = 0.01
    sc_details.update({"type": "Telescope"})
    print(print_details(sc_details))

def print_details(spacecraft):
    return f"""
    ============REPORT============
    
    Spacecraft  : {spacecraft["name"]} AU
    Distance    : {spacecraft.get("distance")}
    Type        : {spacecraft.get("type")}

    ============REPORT============
    """

main()