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