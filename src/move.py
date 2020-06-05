class Move:
    def __init__(self, from_room, direction, to_room):
        self.from_room = from_room
        self.direction = direction
        self.to_room = to_room

moves = [Move("from_room": "outside", "direction": "n", "to_room": "foyer"), 
    Move("from_room": "foyer", "direction": "s", "to_room": "outside"),
    Move("from_room": "foyer", "direction": "n", "to_room": "overlook"), 
    Move("from_room": "overlook", "direction": "s", "to_room": "foyer"),
    Move("from_room": "foyer", "direction": "e", "to_room": "narrow"),
    Move("from_room": "narrow", "direction": "w", "to_room": "foyer"),
    Move("from_room": "narrow", "direction": "n", "to_room": "treasure"),
    Move("from_room": "treasure", "direction": "s", "to_room": "narrow")]