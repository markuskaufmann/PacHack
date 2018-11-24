from app.dto.ReturnDirections import ReturnDirections
from app.dto.HelperDTOs import Directions
from app.gamefield import path


class PublicPlayer:
    FLAG = False
    GOAL = []
    PATH = []

    def __init__(self, game_field, isPacman=True, direction=Directions.NORTH, position=[0, 0], jsonString=None,
                 activeCapsule=False):
        self.isPacman = isPacman
        self.direction = direction
        self.position = position
        self.activeCapsule = activeCapsule

        if (jsonString != None):
            self.__dict__ = jsonString
            self.game_field = game_field
            self.position = [int(self.position[0]), int(self.position[1])]

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

    def eat_safe(self, opp_x, opp_y):
        pass

    def panic_action(self, opp_x, opp_y):
        escape_points = self.game_field.get_escape_points()

        for i in range(len(escape_points)):
            print("çççççççççççççççççççççççççççç")
            print(escape_points)
            path_agent = path.astar(self.game_field.grid, (self.position[1], self.position[0]),
                               (escape_points[i][0], escape_points[i][1]))
            path_enemy = path.astar(self.game_field.grid, (opp_y, opp_x),
                                (escape_points[i][0], escape_points[i][1]))
            if len(path_agent) < len(path_enemy):
                print("çççççççççççççççççççççççççççç")
                print("Escaping to ", escape_points[i])
                print("çççççççççççççççççççççççççççç")
                return self.get_action_from_next_pos(path_agent[len(path_agent) - 1])

    def eat_action(self):
        # return ReturnDirections.NORTH
        goal_position = self.game_field.get_target_locations()[0]

        #if PublicPlayer.GOAL != goal_position:
        return self.get_goal_action(goal_position)

    def get_goal_action(self, goal_position):
        PublicPlayer.GOAL = goal_position
        goal_path = path.astar(self.game_field.grid, (self.position[1], self.position[0]),
                               (PublicPlayer.GOAL[1], PublicPlayer.GOAL[0]))
        print("###### ##########################################################################")
        print("################################################################################")
        print("PATH FOUND! : ")
        PublicPlayer.PATH = goal_path
        print("Path: ", goal_path)
        return self.get_action_from_next_pos(goal_path[len(goal_path) - 1])

    def dist_to_opponent(self, opp_x, opp_y):
        goal_path = path.astar(self.game_field.grid, (self.position[1], self.position[0]),
                               (opp_y, opp_x))
        return len(goal_path)

    # def ChoseAction(self):
    #     if len(PublicPlayer.PATH) == 0:
    #         return ReturnDirections.STOP
    #
    #     next_pos = self.position
    #     if self.position[0] != next_pos[0] and self.position[1] != next_pos[1]:
    #         next_pos = PublicPlayer.PATH.pop()
    #
    #     return self.get_action_from_next_pos(next_pos)

    def get_action_from_next_pos(self, next_pos):
        print("next_pos: {0}".format(next_pos))
        print("self_pos: {0}".format(self.position))
        if next_pos[0] == self.position[1] + 1:
            return ReturnDirections.NORTH
        if next_pos[0] == self.position[1] - 1:
            return ReturnDirections.SOUTH
        if next_pos[1] == self.position[0] - 1:
            return ReturnDirections.WEST
        if next_pos[1] == self.position[0] + 1:
            return ReturnDirections.EAST
        else:
            return ReturnDirections.STOP
