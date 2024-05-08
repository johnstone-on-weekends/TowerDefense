from Towers.tower import Tower


class TowerMenu:
    def __init__(self):
        """
        This class represents the menu that pops up that has the towers that can be placed
        """
        self.towers = ["popper", "jeff", "billy", "factory", "mitch", "robot", "warrior", "elephant"]

        self.add_tower_class()

    def add_tower_class(self):
        """
        Converts self.towers into a list of lists with Tower objects rather than just strings. Useful because Towers have
        certain properties, such as an image associated with the type.
        """

        for i in range(len(self.towers)):
            self.towers[i] = Tower(self.towers[i])
