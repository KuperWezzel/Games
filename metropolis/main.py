from name_picker import set_players_window
from game_window import game_window_layout
from metropolis.MetropolisGame import MetropolisGame
from metropolis.MetropolisPlayer import MetropolisPlayer
from cards import all_cards


if __name__ == "__main__":
    players = set_players_window()
    if not players:
        exit()
    game = MetropolisGame(all_cards)
    for player in players:
        game.add_player(MetropolisPlayer(player, []))
    game_window_layout(game)
