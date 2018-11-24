import random
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
    game_field = GameField(data_dict['gameField'])
    print(data)
    public_players = data_dict['publicPlayers']
    agent_id = data_dict['agent_id']
    agent = PublicPlayer(game_field=game_field, jsonString=public_players[agent_id])
    opponent = PublicPlayer(game_field=game_field, jsonString=public_players[0 if agent_id == 1 else 1])
    print("Possible actions agent: {0}".format(agent.getPossibleActions()))
    print("Possible actions opponent: {0}".format(opponent.getPossibleActions()))
    return random.choice(agent.getPossibleActions())


application = bottle.default_app()


if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '127.0.0.1'), port=os.getenv('PORT', '8080'))
