class Field:

    def __init__(self, type_of_field):
        self.type_of_field = type_of_field
        self.color = self.match_field_color()
        self.tower = None

    def match_field_color(self):
        """
        Finds the matching color for the type of field.
        :return: the color found to associate with the type
        """
        match self.type_of_field:
            case "p":  # path
                return [139, 69, 19]  # Brownish
            case "g":  # grass
                return [144, 238, 144]  # Greenish
            case "w":  # water
                return [65, 105, 225]  # Blue
            case "s":  # start
                return [255, 99, 71]  # Reddish
            case "e":  # end
                return [240, 230, 140]  # Beige
