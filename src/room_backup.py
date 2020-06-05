# Implement a class to hold room information. This should have name and description attributes.


rooms = [Room("outside", "desc1"), 
         Room("foyer", "desc2"), 
         Room("overlook", "desc3"), 
         Room("narrow", "desc4"), 
         Room("treasure", "desc5")]





# create items
items = [Item("mushrooms"), Item("gold"), Item("bread"), Item("sword"), Item("key"), Item("treasure")]

# current_player = Player("ignacio", 'outside')

# pickup item
# items[0].get_item(current_player)
# items[1].get_item(current_player)
# items[2].get_item(current_player)
# print(len(current_player.items))

# drop item
# items[0].drop_item(current_player)
# print(len(current_player.items))


# add items to rooms
class RoomItem:
    def __init__(self, room, item):
        self.room = room  
        self.item = item  

# add items to rooms        
rooms[0].add_room_item(items[0]) # mushrooms to outside
rooms[0].add_room_item(items[1]) # gold to outside
rooms[1].add_room_item(items[2]) # bread to foyer
rooms[1].add_room_item(items[3]) # bread to foyer
rooms[2].add_room_item(items[3]) # key to overlook

# print(rooms[1].items[1].item.name)   

# write class cardinal point : n, s, e, w
class Direction:
    def __init__(self, abbr, opposite):
        self.abbr = abbr
        self.opposite = opposite

# write room-allowed-directions: direction, target (the room you reach with that movement)
# class Move:
#     def __init__(self, from_room, direction, to_room):
#         self.from_room = from_room
#         self.direction = direction
#         self.to_room = to_room

moves = [{"from_room": "outside", "direction": "n", "to_room": "foyer"}, 
    {"from_room": "foyer", "direction": "s", "to_room": "outside"},
    {"from_room": "foyer", "direction": "n", "to_room": "overlook"}, 
    {"from_room": "overlook", "direction": "s", "to_room": "foyer"},
    {"from_room": "foyer", "direction": "e", "to_room": "narrow"},
    {"from_room": "narrow", "direction": "w", "to_room": "foyer"},
    {"from_room": "narrow", "direction": "n", "to_room": "treasure"},
    {"from_room": "treasure", "direction": "s", "to_room": "narrow"}]


# write class player with attributes: name, current


# write method for movement in specified directions


current_player = Player(input("Enter player name: "), "outside")
print(f"{current_player.name} is walking {current_player.current}")


# player input prompt: what direction do you want to move to?
# find new move in allowed moves to determine the destination room
# current_player: you are now in room X
# current_player input prompt: what direction do you want to move to?

# while True:

item_bag = []

mushroom = input(f"Look! there is a mushroom! Should I pick it up?")
if mushroom == "y":
    items[0].get_item(current_player)
    for i in current_player.items:
        item_bag.append(i.name)
    print(item_bag)
    print(f"{current_player.name} was hungry, so he ate it")
    print(f"Delicious! I should pick up some more to share with my friends")
    frog = input(f"Oh look, there's a frog holding a pot of gold, should I approach?")
    if frog == "y":
        print(f"Hi frog, my name is {current_player.name}, nice gold! can I have some?")
        print(f"Hi {current_player.name}, sure, since you asked nicely, why not? Here, have a piece")
        items[1].get_item(current_player)
        for i in current_player.items:
            item_bag.append(i.name)
        print(item_bag)
        print(f"Yay!, now I have some mushrooms and gold")
else:
    print("boring")
# player new move
new_move = input("Which direction do you want to go? ")
print(f"{current_player.name} is moving {new_move}")
for move in moves:
    if move['from_room'] == current_player.current and move['direction'] == new_move:
        current_player.current = move['to_room']
        break
    # else:
    #     print("Movement not allowed")
print(f"You are now in {current_player.current}")

# foyer elf
if current_player.current == "foyer":
    print("Hi Elf, look what I have, GOLD!")
    elf = input(f"Cool, do you want to trade for some dragon bread and a sword?")
    if elf == "y":
        items[1].drop_item(current_player)
        items[2].get_item(current_player)
        items[3].get_item(current_player)
        for i in current_player.items:
            item_bag.append(i.name)
            print(i.name)
        print(f"Nice, now I have dragon breand and a sword")        
    else:
        print("boring")
# player new move
new_move = input("Which direction do you want to go? ")
print(f"{current_player.name} is moving {new_move}")
for move in moves:
    if move['from_room'] == current_player.current and move['direction'] == new_move:
        current_player.current = move['to_room']
        break
    # else:
    #     print("Movement not allowed")
print(f"You are now in {current_player.current}")            

# overlook dragon
if current_player.current == "overlook":
    print(f"{current_player.name}: Hi Dragon, Elf told me you where hungry!")
    print("Dragon: I am, but i don't have any dragon bread, just have this key")
    dragon = input(f"Dragon: Do you have any bread that want to trade?")
    if dragon == "y":
        items[2].drop_item(current_player)
        items[4].get_item(current_player)
        for i in current_player.items:
            item_bag.append(i.name)
            print(i.name)
        print(f"I like my new key, I wonder what it opens...")  
    else:
        print("boring")

# player new move
new_move = input("Which direction do you want to go? ")
print(f"{current_player.name} is moving {new_move}")
for move in moves:
    if move['from_room'] == current_player.current and move['direction'] == new_move:
        current_player.current = move['to_room']
        break
    # else:
    #     print("Movement not allowed")
print(f"You are now in {current_player.current}")           

# foyer elf again
# player new move
new_move = input("Which direction do you want to go? ")
print(f"{current_player.name} is moving {new_move}")
for move in moves:
    if move['from_room'] == current_player.current and move['direction'] == new_move:
        current_player.current = move['to_room']
        break
    # else:
    #     print("Movement not allowed")
print(f"You are now in {current_player.current}")                  

# narrow troll
if current_player.current == "narrow":
    print(f"{current_player.name}: Hi Troll, are you friendly?")
    print("Troll: No!, I'm gonna kill you!")
    troll = input(f"Do you want to atack with your sword?")
    if troll == "y":
        items[3].drop_item(current_player)
        for i in current_player.items:
            item_bag.append(i.name)
            print(i.name)
        print(f"Your sword broke, but you killed the Troll")  
    else:
        print("boring")
      
# player new move
new_move = input("Which direction do you want to go? ")
print(f"{current_player.name} is moving {new_move}")
for move in moves:
    if move['from_room'] == current_player.current and move['direction'] == new_move:
        current_player.current = move['to_room']
        break
    # else:
    #     print("Movement not allowed")
print(f"You are now in {current_player.current}")       

# treasure
if current_player.current == "treasure":
    print(f"{current_player.name}: I wonder what this heavy door opens, it's locked")
    print("You just remembered you have a key")
    key = input(f"Do you want to try it?")
    if key == "y":
        items[4].drop_item(current_player)
        items[5].get_item(current_player)
        for i in current_player.items:
            item_bag.append(i.name)
            print(i.name)
        print(f"{current_player.name}: I just found a treasure! woohoo! I'll have the rest of my mushrooms and enjoy it")  
    else:
        print("boring")    
# player new move
print(f"The END")




