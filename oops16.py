class Campany:
    name = "Open AI"
    def __init__(self):
        print("Campany name :  ",Campany.name)
        


print("Before Campany Name")
c = Campany()


print("___________________\n")
Campany.name = "Chat GPT"

print("After Campany Name")
x = Campany()

