class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    def add_room_item(self, item):
        add_item = RoomItem(self, item)
        self.items.append(add_item)        

# add items to rooms
class RoomItem:
    def __init__(self, room, item):
        self.room = room  
        self.item = item          