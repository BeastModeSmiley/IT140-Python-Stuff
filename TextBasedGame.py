answer_N = ["N", "n", "North", "north"]
answer_S = ["S", "s", "South", "south"]
answer_E = ["E", "e", "East", "east"]
answer_W = ["W", "w", "West", "west"]
pickup = ["y", "Y", "yes", "Yes", "Get", "get", "take", "Take", "pickup", "Pickup"]
leave = ["n", "N", "no", 'No']
blaster = 0
chest = 0
helmet = 0
boots = 0
pants = 0

required = "\nYou entered an invalid option, please try again...\n"
print("You have been teleported to lounge of the USS Starship and you\n"
      "have just been informed that your help is needed to take care of\n"
      "some unknown creature that has gotten loose inside the Cargo Bay.\n"
      "You will need to first find the proper gear to confront the unknown\n"
      "creature to ensure your survival. There are five pieces of gear you\n"
      "will need to find to confront the creature safely...")
print('-' * 70)


def lounge():
    print("Lounge")
    print("You are in the lounge where fellow crew members are sitting around\n"
          "enjoying peaceful conversations with each other. A server is bringing\n"
          "drinks to everyone when you hear a loud scream coming from the south.\n"
          "No one knows what that was and now all of you are starting to worry.")
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
        print("You have made your way to the Bridge. You see lots of people at work\n"
              "preforming their duties to keep the ship moving. There are computer\n"
              "screens every where with tons of data that you have no clue what it\n"
              "means. You do see some security monitors but the one the cargo bay is down...")
        print(">>A Chest Plate is laying in the corner of the room. Do you want to pick it up???<<")
        choice = input(">>> ")
        if choice in pickup:
            chest = 1
            print("You picked up the Chest Plate and put it on!")
        elif choice in leave:
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
        print("You have made your way to the Bridge. You see lots of people at work\n"
              "preforming their duties to keep the ship moving. There are computer\n"
              "screens every where with tons of data that you have no clue what it\n"
              "means. You do see some security monitors but the one the cargo bay is down...")
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
        print("You stand before a massive screen that is pretty much a map of the stars.\n"
              "There are several blinking dots on this map but nothing is labeled so\n"
              "you cannot tell which dot is the ship your on. You now see one dot that is\n"
              "blinking red and it appears to be way of course. Could this be your ship??")
        print(">>A Pair of Boots are near the door. Do you want put them on???<<")
        choice = input(">>> ")
        if choice in pickup:
            boots = 1
            print("You put on the pair of Boots!")
        elif choice in leave:
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
        print("You stand before a massive screen that is pretty much a map of the stars.\n"
              "There are several blinking dots on this map but nothing is labeled so\n"
              "you cannot tell which dot is the ship your on. You now see one dot that is\n"
              "blinking red and it appears to be way of course. Could this be your ship??")
        print("Now where to?")
        print("   East: Bridge")
        choice = input(">>> ")
        if choice in answer_E:
            bridge()
        else:
            print(required)
            nav()


def captain():
    global blaster
    global chest
    global helmet
    global boots
    global pants
    if helmet == 0:
        print("Captain's Quarters")
        print("A huge chair sits in the middle of the room with a giant monitor sitting\n"
              "in front of it. The Captain is not here but it seems that he was just here\n"
              "because you see a cup of coffee sitting on the chair arm and it is steaming.\n"
              "Where could he have ran off to in such a hurry??")
        print(">>A Helmet sits on the desk. Do you want put it on???<<")
        choice = input(">>> ")
        if choice in pickup:
            helmet = 1
            print("You put on the Helmet!")
        elif choice in leave:
            helmet = 0
            print("You did not put on the Helmet!")
        else:
            print(required)
            captain()
        print("Now where to?")
        print("   West: Bridge")
        choice = input(">>> ")
        if choice in answer_W:
            bridge()
        else:
            print(required)
            captain()
    elif helmet == 1:
        print("Captain's Quarters")
        print("A huge chair sits in the middle of the room with a giant monitor sitting\n"
              "in front of it. The Captain is not here but it seems that he was just here\n"
              "because you see a cup of coffee sitting on the chair arm and it is steaming.\n"
              "Where could he have ran off to in such a hurry??")
        print("Now where to?")
        print("   West: Bridge")
        choice = input(">>> ")
        if choice in answer_W:
            bridge()
        else:
            print(required)
            captain()


def armory():
    global blaster
    global chest
    global helmet
    global boots
    global pants
    if blaster == 0:
        print("Armory")
        print("This is by far the coolest room you have visited so far. There are all kinds\n"
              "of cages that are filled with different types of armor and weapons. There is\n"
              "even some missiles stacked up in the corner ready to be used. There is an\n"
              "Officer waving at you in the corner and asking if you need help.")
        print(">>A Blaster is sitting on the gun rack. Do you want to pick it up???<<")
        choice = input(">>> ")
        if choice in pickup:
            blaster = 1
            print("You now are wielding the Blaster!")
        elif choice in leave:
            blaster = 0
            print("You did not pick up the Blaster!")
        else:
            print(required)
            armory()
        print("Now where to?")
        print("   East: Lounge")
        choice = input(">>> ")
        if choice in answer_E:
            lounge()
        else:
            print(required)
            armory()
    elif blaster == 1:
        print("Armory")
        print("This is by far the coolest room you have visited so far. There are all kinds\n"
              "of cages that are filled with different types of armor and weapons. There is\n"
              "even some missiles stacked up in the corner ready to be used. There is an\n"
              "Officer waving at you in the corner and asking if you need help.")
        print("Now where to?")
        print("   East: Lounge")
        choice = input(">>> ")
        if choice in answer_E:
            lounge()
        else:
            print(required)
            armory()


def hanger():
    global blaster
    global chest
    global helmet
    global boots
    global pants
    if pants == 0:
        print("Hanger")
        print("You are in a very large room with multiple ships ready to launched. There are\n"
              "people over to the west holding a door shut for some reason. A loud scary\n"
              "noise comes from behind the door that they are holding. You now know where\n"
              "the loud scream came from earlier. Everyone is looking to you to help with\n"
              "what ever is behind the door. Are you prepared to face what ever it is?!?!")
        print(">>A pair of Leggings are laying on a box. Do you want to put them on???<<")
        choice = input(">>> ")
        if choice in pickup:
            pants = 1
            print("You put on the Leggings!")
        elif choice in leave:
            pants = 0
            print("You did not put on the Leggings!")
        else:
            print(required)
            hanger()
        print("Now where to?")
        print("   North: Lounge\n   East: Cargo Bay")
        choice = input(">>> ")
        if choice in answer_E:
            cargo()
        elif choice in answer_N:
            lounge()
        else:
            print(required)
            hanger()
    elif pants == 1:
        print("Hanger")
        print("You are in a very large room with multiple ships ready to launched. There are\n"
              "people over to the west holding a door shut for some reason. A loud scary\n"
              "noise comes from behind the door that they are holding. You now know where\n"
              "the loud scream came from earlier. Everyone is looking to you to help with\n"
              "what ever is behind the door. Are you prepared to face what ever it is?!?!")
        print("Now where to?")
        print("   North: Lounge\n   East: Cargo Bay")
        choice = input(">>> ")
        if choice in answer_E:
            cargo()
        elif choice in answer_N:
            lounge()
        else:
            print(required)
            hanger()


def cargo():
    global blaster
    global chest
    global helmet
    global boots
    global pants
    total = blaster + chest + helmet + boots + pants
    if total == 5:
        print("You walk into the room through the door and do not see anything at\n"
              "first but you hear something behind a stack of boxes. As you get\n"
              "closer to the boxes a huge creature with four arms jumps out and\n"
              "starts attacking you!!!!!!!!!!!!")
        print("Lucky you prepared yourself for this moment and you are able to\n"
              "conquer the creature easily!!! Great Job!!! You WIN!!!")
        exit()
    else:
        print("You walk into the room through the door and do not see anything at\n"
              "first but you hear something behind a stack of boxes. As you get\n"
              "closer to the boxes a huge creature with four arms jumps out and\n"
              "starts attacking you!!!!!!!!!!!!")
        print("Unfortunately you were not prepared to face this creature and\n"
              "the creature easily devours you!!!!! You LOSE!!!!")
        exit()


lounge()
