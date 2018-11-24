from app.dto.HelperDTOs import Directions


class HelperDTO(object):
    pass


class GameField(object):

    AGENT_FOOD_MAP = {
        0: [],
        1: []
    }

    def __init__(self, game_field, agent_id) -> None:
        self.grid = game_field
        self.agent_id = agent_id
        field_size_x = len(game_field[0])
        GameField.AGENT_FOOD_MAP[0] = [int(field_size_x / 2), field_size_x - 1]
        GameField.AGENT_FOOD_MAP[1] = [1, int(field_size_x / 2) - 1]
        print(GameField.AGENT_FOOD_MAP)
        self.food_range = GameField.AGENT_FOOD_MAP[self.agent_id]
        print(game_field)

    def givePossibleActions(self, pos_x, pos_y):
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        possible_movements = []
        print("position: {0} {1}".format(pos_x, pos_y))
        if pos_y > 0:
            if self.grid[pos_y - 1][pos_x] != "%":
                possible_movements.append(Directions.NORTH)
        if pos_y < len(self.grid):
            if self.grid[pos_y + 1][pos_x] != "%":
                possible_movements.append(Directions.SOUTH)
        if pos_x > 0:
            if self.grid[pos_y][pos_x + 1] != "%":
                possible_movements.append(Directions.EAST)
        if pos_x < len(self.grid[0]):
            if self.grid[pos_y][pos_x - 1] != "%":
                possible_movements.append(Directions.WEST)
        print(possible_movements)
        return possible_movements

    def get_target_locations(self):
        food_locations = self._get_food_locations()
        if len(food_locations) == 0:
            return self._get_agent_home_field()
        return food_locations

    def get_agent_home(self):
        return self._get_agent_home_field()

    def _get_agent_home_field(self):
        food_map = GameField.AGENT_FOOD_MAP[self.agent_id]
        loc_y = 1
        loc_x = food_map[0] - 1 if self.agent_id == 0 else food_map[1] + 1
        return [loc_x, loc_y]

    def _get_food_locations(self):
        food_positions = []
        for idx_y in range(len(self.grid)):
            for idx_x in range(self.food_range[0], self.food_range[1] + 1):
                pos = self.grid[idx_y][idx_x]
                if pos == "\u00b0":
                    food_positions.append([idx_x, idx_y])
        return food_positions
