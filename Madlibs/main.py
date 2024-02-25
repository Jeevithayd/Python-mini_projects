def madlibs():
    
    name = input("Enter a name: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    story = f"{name} was feeling {adjective1} one day. They decided to take a walk to the {place}. On the way, they saw a {noun1} and a {noun2}. Feeling adventurous, they decided to {verb} all the way to the {place}."

    print("\nHere's your madlibs story:")
    print(story)

madlibs()
