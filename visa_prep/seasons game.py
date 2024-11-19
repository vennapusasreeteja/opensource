def seasons(mon):
    if mon < 1 or mon > 12:
        print("Invalid")
    elif mon in [3, 4, 5]:
        print("Spring")
    elif mon in [6, 7, 8]:
        print("Summer")
    elif mon in [9,10,11]:
        print("Autumn")
    else:
        print("Winter")
mon = int(input())
seasons(mon)
