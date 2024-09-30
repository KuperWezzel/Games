from cards import normal_deck
from game_window import event_loop
from metropolis.MetropolisGame import MetropolisGame
from metropolis.MetropolisPlayer import MetropolisPlayer
from pre_game_screens import get_player_names_window, start_discard_window


def main():
    names = None
    another_game = True
    while another_game:
        # get names
        player_names = get_player_names_window(names)
        if not player_names:
            exit()

        game = MetropolisGame(normal_deck)
        for name in player_names:
            game.add_player(MetropolisPlayer(name, []))
        game.start_game()
        # discard 2 cards
        start_discard_window(game)
        # actually start normal game
        another_game = event_loop(game)
        names = [player.name for player in game.players]


if __name__ == "__main__":
    main()
