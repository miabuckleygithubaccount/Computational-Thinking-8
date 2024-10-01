#intro 
print("You're out trick or treating with friends.")
print("You knock on the door of a creepy, dim-lit house.")
print("A man dressed like a clown answers and beckons you inside.")
print("You come inside and the door shuts behind you.")
print("Will you escape the house?")

# choice 1
c1 = input("Do you choose to go to the [kitchen] with the clown or the [living room]?")
if "living room" in c1:
    print("You quietly walk into the living room")

else:
    print("You decide to go into the kitchen and the clown feeds you poisonous candies")

# choice 2
c2 = input("Do you choose to go sit on the [couch] or go [upstairs]? ")
if "upstairs" in c2:
    print("You decide to go upstairs and you see a long hallway.")

else: 
    print("You sit on the couch and the clown finds you.")

# choice 3
c3 = input("Do you decide to go down the [hallway] or into the [bathroom]?")
if "hallway" in c3:
    print("You go down the hallway and find an old table and a key.")

else:
    print("You go into the bathroom and the clowns dog finds you and eats you.")

# choice 4
print("You grab the key and there's a room on your right and your left.")
c4 = input("Do you go [right] or [left]?")
if "right" in c4:
    print("You walk right and into the dark room.")

else:
    print("You go left into the other room and the door shuts and locks behind you. You're stuck inside and you starve.")

# choice 5
print("In the room, you can take a [bat], a [crowbar] or a [sword].")
c5 = input("What do you take for protection?")
if "bat" in c5:
    print("You pick up the bat.")
elif "crowbar" in c5:
    print("You take the crowbar.")
else:
    print("You take the sword just to find out it was just a prop and not real.")

# choice 6
print("You go downstairs, your weapon raised and ready. You find the clown.")
c6 = input("Do you [hit] the clown on the head or [whack] him in the legs?")
if "hit" in c6:
    print("You hit him in the head and knock him out. You take the key you found and escape.")
else:
    print("You hit him in the legs and he falls, but then stands up and attacks you.")