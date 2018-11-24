from app.dto.ReturnDirections import ReturnDirections
from app.dto.HelperDTOs import Directions
from app.gamefield import path

class PublicPlayer:

    FLAG = False
    GOAL = []
    PATH = []

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

    def SetGoal(self):
        # return ReturnDirections.NORTH
        goal_position = self.game_field.get_target_locations()[0]

        if PublicPlayer.GOAL != goal_position:
            PublicPlayer.GOAL = goal_position
            goal_path = path.astar(self.game_field.grid, (self.position[0], self.position[1]), (PublicPlayer.GOAL[1], PublicPlayer.GOAL[0]))
            print("################################################################################")
            print("################################################################################")
            print("PATH FOUND! : ")
            PublicPlayer.PATH = goal_path
            print("Path: ", goal_path)

    def ChoseAction(self):
        if len(PublicPlayer.PATH) == 0:
            return ReturnDirections.STOP

        next_pos = PublicPlayer.PATH.pop()

        if next_pos[0] == self.position[0] - 1:
            return ReturnDirections.NORTH
        if next_pos[0] == self.position[0] + 1:
            return ReturnDirections.SOUTH
        if next_pos[1] == self.position[1] - 1:
            return ReturnDirections.WEST
        if next_pos[1] == self.position[1] + 1:
            return ReturnDirections.EAST
        else:
            InterruptedError("not interrupted, but you fucked up the chose action alg")
