from app.dto.HelperDTOs import Directions


class PublicPlayer:
    def __init__(self, game_field, isPacman=True, direction=Directions.NORTH, position=[0, 0], jsonString=None, activeCapsule=False):
        self.isPacman = isPacman
        self.direction = direction
        self.position = position
        self.activeCapsule = activeCapsule
        if (jsonString != None):
            self.__dict__ = jsonString
            self.game_field = game_field

    def __str__(self):
        returnVal = 'G'
        if self.direction == Directions.NORTH:
            returnVal = 'N'
        if self.direction == Directions.SOUTH:
            returnVal = 'S'
        if self.direction == Directions.WEST:
            returnVal = 'W'
        if self.direction == Directions.EAST:
            returnVal = 'E'
        if self.isPacman:
            return returnVal.lower()
        return returnVal.upper()

    def getPossibleActions(self):
        return self.game_field.givePossibleActions(self.position[0], self.position[1])