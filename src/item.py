from player import Player

class Item:
    def __init__(self, name):
        self.name = name
    def get_item(self, player):
        current_player.items.append(self)
    def drop_item(self, player):
        current_player.items.remove(self)