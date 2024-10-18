from cards import normal_deck
from metropolis.MetropolisGame import MetropolisGame
from metropolis.MetropolisPlayer import MetropolisPlayer
from pre_game_screens import get_player_names_window, start_discard_window
from game_window import event_loop as game_event_loop
from score_window import event_loop as score_event_loop


def main():
    names = None
    another_game = True
    while another_game:
        # get names
        is_normal_game, player_names = get_player_names_window(names)
        if not player_names:
            exit()

        game = MetropolisGame(normal_deck)
        for name in player_names:
            game.add_player(MetropolisPlayer(name, []))
        game.start_game()
        if is_normal_game:
            # discard 2 cards
            start_discard_window(game)
            # actually start normal game
            another_game = game_event_loop(game)
        else:
            another_game = score_event_loop(game)
        names = [player.name for player in game.players]


if __name__ == "__main__":
    main()
