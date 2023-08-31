name = input("What's your name? ")

"""if name == "Harry":
    print("Gryfindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")   


if name == "Harry" or name == "Hermione" or name =="Medisha" or name == "Aliyah" or name == "Ibrahim":
    print("Gryfindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?") 


match name:
    case "Harry":
        print("Gryfindor")
    case "Draco":
        print("Slytherin")
    case "Medisha":
        print("Gryfindor")
    case "Aliyah":
        print("Gryfindor")
    case "Ibrahim":
        print("Gryfindor")
    case "Hermione":
        print("Gryfindor")
    case "Ron":
        print("Gryfindor")
    case _:
        print("Who?")

"""
match name:
    case "Aliyah" | "Ibrahim" | "Harry" | "Medisha" | "Hermione" | "Ron":
        print("Gryfindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")
