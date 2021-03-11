 
answer_N = ["N", "n", "North", "north"]
 
answer_S = ["S", "s", "South", "south"]
 
answer_E = ["E", "e", "East", "east"]
 
answer_W = ["W", "w", "West", "west"]
 
pickup = ["yes", "Yes", "Get", "get", "take", "Take", "pickup", "Pickup"]
 
nopickup = ["no", 'No']
 
blaster = 0
 
chest = 0
 
helmet = 0
 
boots = 0
 
pants = 0
 
 
required = "\nYou entered an invalid option, please try again...\n"
 
 
 
def lounge():
 
    print("You have been teleported to lounge of the USS Starship and you\n"
 
          "have just been informed that your help is needed to take care of\n"
 
          "some unknown creature that has gotten loose inside the Cargo Bay.\n"
 
          "You will need to first find the proper gear to confront the unknown\n"
 
          "creature to ensure your survival. There are five pieces of gear you\n"
 
          "will need to find to confront the creature safely...")
 
    print("   North: Bridge\n   South: Hanger\n   West: Armory")
 
    choice = input(">>> ")
 
    if choice in answer_N:
 
        bridge()
 
    elif choice in answer_S:
 
        hanger()
 
    elif choice in answer_W:
 
        armory()
 
    else:
 
        print(required)
 
        lounge()
 
 
 
def bridge():
 
    global blaster
 
    global chest
 
    global helmet
 
    global boots
 
    global pants
 
    if chest == 0:
 
        print("Bridge")
 
        print(">>A Chest Plate is laying in the corner of the room. Do you want to pick it up???<<")
 
        choice = input(">>> ")
 
        if choice in pickup:
 
            chest = 1
 
            print("You picked up the Chest Plate and put it on!")
 
        elif choice in nopickup:
 
            chest = 0
 
            print("You did not pick up the Chest Plate!")
 
        else:
 
            print(required)
 
            bridge()
 
        print("Now where to?")
 
        print("   South: Lounge\n   West: Navigation\n   East: Captain's Quarters")
 
        choice = input(">>> ")
 
        if choice in answer_E:
 
            captain()
 
        elif choice in answer_S:
 
            lounge()
 
        elif choice in answer_W:
 
            nav()
 
        else:
 
            print(required)
 
            bridge()
 
    elif chest == 1:
 
        print("Bridge")
 
        print("Now where to?")
 
        print("   South: Lounge\n   West: Navigation\n   East: Captain's Quarters")
 
        choice = input(">>> ")
 
        if choice in answer_E:
 
            captain()
 
        elif choice in answer_S:
 
            lounge()
 
        elif choice in answer_W:
 
            nav()
 
        else:
 
            print(required)
 
            bridge()
 
 
 
def nav():
 
    global blaster
 
    global chest
 
    global helmet
 
    global boots
 
    global pants
 
    if boots == 0:
 
        print("Navigation")
 
        print(">>A Pair of Boots are near the door. Do you want put them on???<<")
 
        choice = input(">>> ")
 
        if choice in pickup:
 
            boots = 1
 
            print("You put on the pair of Boots!")
 
        elif choice in nopickup:
 
            boots = 0
 
            print("You did not put on the boots!")
 
        else:
 
            print(required)
 
            nav()
 
        print("Now where to?")
 
        print("   East: Bridge")
 
        choice = input(">>> ")
 
        if choice in answer_E:
 
            bridge()
 
        else:
 
            print(required)
 
            nav()
 
    elif boots == 1:
 
        print("Navigation")
 
        print("Now where to?")
 
        print("   East: Bridge")
 
        choice = input(">>> ")
 
        if choice in answer_E:
 
            bridge()
 
        else:
 
            print(required)
 
            nav()
 
 
def captain():
 
    print()
 
    print(">>A Helmet sits on the desk. Do you want put it on???<<")
 
    choice = input(">>> ")
 
    if choice in pickup:
 
        helmet = 1
 
        print("You put on the Helmet!")
 
    else:
 
        helmet = 0
 
    print("Now where to?")
 
    print("   West: Bridge")
 
    choice = input(">>> ")
 
    if choice in answer_W:
 
        bridge()
 
    else:
 
        print(required)
 
        captain()
 
 
 
def armory():
 
    print()
 
    print(">>A Blaster is sitting on the gun rack. Do you want to pick it up???<<")
 
    choice = input(">>> ")
 
    if choice in pickup:
 
        blaster = 1
 
        print("You now are wielding the Blaster!")
 
    else:
 
        blaster = 0
 
    print("Now where to?")
 
    print("   East: Lounge")
 
    choice = input(">>> ")
 
    if choice in answer_E:
 
        lounge()
 
    else:
 
        print(required)
 
        armory()
 
 
 
def hanger():
 
    print()
 
    print(">>A pair of Leggings are laying on a box. Do you want to put them on???<<")
 
    choice = input(">>> ")
 
    if choice in pickup:
 
        pants = 1
 
        print("You put on the Leggings!")
 
    else:
 
        pants = 0
 
    print("Now where to?")
 
    print("   North: Lounge\n   East: Cargo Bay")
 
    choice = input(">>> ")
 
    if choice in answer_E:
 
      # cargo()
 
        if (pants + helmet + chest + boots + blaster) > 4:
 
            print("\nYou laid in wait. The shimmering sword attracted "
 
                  "the orc, which thought you were no match. As he walked "
 
                  "closer and closer, your heart beat rapidly. As the orc "
 
                  "reached out to grab the sword, you pierced the blade into "
 
                  "its chest. \n\nYou survived!")
 
        else:
 
            print("\nYou should have picked up that sword. You're "
 
                  "defenseless. \n\nYou died!")
 
    elif choice in answer_N:
 
        lounge()
 
    else:
 
        print(required)
 
        hanger()
 
 
 
lounge()
 
