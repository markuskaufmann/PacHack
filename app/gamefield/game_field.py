from app.dto.HelperDTOs import Directions


class HelperDTO(object):
    pass


class GameField(object):
    def __init__(self, gameField) -> None:
        self.gameField = gameField
        print(gameField)

    def givePossibleActions(self, posX, posY):
        possibleMovementsArray = []
        if self.gameField[posX][posY + 1] != "%":
            possibleMovementsArray.append(Directions.NORTH)
        if self.gameField[posX][posY - 1] != "%":
            possibleMovementsArray.append(Directions.SOUTH)
        if self.gameField[posX + 1][posY] != "%":
            possibleMovementsArray.append(Directions.EAST)
        if self.gameField[posX - 1][posY] != "%":
            possibleMovementsArray.append(Directions.WEST)

        print(possibleMovementsArray)
        return possibleMovementsArray
