from app.dto.HelperDTOs import Directions
from app.gamefield import path


class HelperDTO(object):
    pass


class GameField(object):
    def __init__(self, gameField) -> None:
        self.grid = gameField
        # print(gameField)

    def givePossibleActions(self, posX, posY):

        posX = int(posX)
        posY = int(posY)
        possibleMovementsArray = []
        # print("position: {0} {1}".format(posX, posY))
        if posY > 0:
            if self.grid[posY - 1][posX] != "%":
                possibleMovementsArray.append(Directions.NORTH)
        if posY < len(self.grid):
            if self.grid[posY + 1][posX] != "%":
                possibleMovementsArray.append(Directions.SOUTH)
        if posX > 0:
            if self.grid[posY][posX + 1] != "%":
                possibleMovementsArray.append(Directions.EAST)
        if posX < len(self.grid[0]):
            if self.grid[posY][posX - 1] != "%":
                possibleMovementsArray.append(Directions.WEST)
        #print(possibleMovementsArray)
        return possibleMovementsArray
