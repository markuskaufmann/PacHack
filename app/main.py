import os

import bottle

from app.dto.PublicGameState import PublicGameState
from app.dto.PublicPlayer import PublicPlayer
from app.dto.ReturnDirections import ReturnDirections
from app.gamefield.game_field import GameField


class TargetLocations:
    LOCATIONS = None


class MoveCounter:
    COUNT = 0


class ReturnHome:
    THRESHOLD = 3


class TempPoints:
    COUNTER = 0


@bottle.post('/start')
def start():
    return "TheRealDiehl"


@bottle.post('/chooseAction')
def move():

    data = PublicGameState(ext_dict=bottle.request.json)
    data_dict = data.__dict__
    agent_id = data_dict['agent_id']
    public_players = data_dict['publicPlayers']
    game_field = GameField(data_dict['gameField'], agent_id)
    target_locations = game_field.get_target_locations()
    agent = PublicPlayer(game_field=game_field, jsonString=public_players[agent_id])
    opponent = PublicPlayer(game_field=game_field, jsonString=public_players[0 if agent_id == 1 else 1])
    dist_oponnent = agent.dist_to_opponent(opponent.position[0], opponent.position[1])
    action = ReturnDirections.STOP
    if TargetLocations.LOCATIONS is not None:
        loc_size = len(TargetLocations.LOCATIONS)
        curr_size = len(target_locations)
        if curr_size < loc_size:
            TempPoints.COUNTER += 1
        elif curr_size > loc_size:
            TempPoints.COUNTER = 0
    TargetLocations.LOCATIONS = target_locations
    if game_field.is_agent_home(agent.position):
        TempPoints.COUNTER = 0
    if dist_oponnent < 3 and agent.isPacman == False and opponent.isPacman:
        action = agent.chase_oponnent(opponent.position[0], opponent.position[1])
    elif dist_oponnent < 2 and opponent.isPacman == False:
        action = agent.panic_action(opponent.position[0], opponent.position[1])
    elif agent.isPacman and dist_oponnent < 5:
        action = agent.panic_action(opponent.position[0], opponent.position[1])
    elif MoveCounter.COUNT >= 450:
        print("MOVE: RETURN TO ESCAPE POINT")
        action = agent.return_to_escape_point()
    elif TempPoints.COUNTER >= ReturnHome.THRESHOLD:
        print("POINTS: RETURN TO ESCAPE POINT")
        action = agent.return_to_escape_point()
    #elif dist_oponnent < 10 and opponent.isPacman == False and agent.isPacman :
    #    action = agent.eat_safe(opponent.position[0], opponent.position[1])
    else:
        action = agent.eat_action()
    print("POINTS: {0}".format(TempPoints.COUNTER))
    print("action: {0}".format(action))
    MoveCounter.COUNT += 1
    return action


application = bottle.default_app()


if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
