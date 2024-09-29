from name_picker import set_players_window
from game_window import game_window_layout
from metropolis.MetropolisGame import MetropolisGame
from metropolis.MetropolisPlayer import MetropolisPlayer
from cards import normal_deck


if __name__ == "__main__":
    players = set_players_window()
    if not players:
        exit()
    game = MetropolisGame(normal_deck)
    for player in players:
        game.add_player(MetropolisPlayer(player, []))
    game.start_game()
    game_window_layout(game)
