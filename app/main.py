import random
from threading import Thread

import bottle
import os

from app.dto.PublicGameState import PublicGameState
from app.dto.PublicPlayer import PublicPlayer
from app.dto.ReturnDirections import ReturnDirections
from app.gamefield.game_field import GameField


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
    agent = PublicPlayer(game_field=game_field, jsonString=public_players[agent_id])
    opponent = PublicPlayer(game_field=game_field, jsonString=public_players[0 if agent_id == 1 else 1])
    dist_oponnent = agent.dist_to_opponent(opponent.position[0], opponent.position[1])
    action = ReturnDirections.STOP

    if dist_oponnent < 5:
        action = agent.panic_action(opponent.position[0], opponent.position[1])
    elif dist_oponnent < 20:
        action = agent.eat_safe(opponent.position[0], opponent.position[1])
    else:
        target_locations = game_field.get_target_locations()
        print("target locations: {0}".format(target_locations))
        print("home field: {0}".format(game_field.get_agent_home()))
        action = agent.eat_action()
    print("action: {0}".format(action))
    return action


application = bottle.default_app()


if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '127.0.0.1'), port=os.getenv('PORT', '8080'))
