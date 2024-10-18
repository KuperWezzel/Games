import PySimpleGUI as sg
from metropolis.MetropolisGame import MetropolisGame
from metropolis.MetropolisPlayer import MetropolisPlayer
from metropolis.MetropolisCard import MetropolisCard, DEFAULT_THEME
from cards import normal_deck, architect
from game_window import end_screen

POPUP_THEME = "DarkBlue"
sg.theme(DEFAULT_THEME)


def player_row_score(player: MetropolisPlayer, cards):
    cards = [architect] + cards
    return [sg.Col(
        [[sg.Push(), sg.T(player.name), sg.Push()],
         [sg.T("Score: 0 points", k=(player, "total_score")), sg.T("City: 0 points", k=(player, "city_score"))],
         [sg.T("Choose next cards to play")],
         [sg.Combo(cards, k=(player, "cards_to_play"), readonly=True, default_value=cards[0])],
         [sg.Button("Play card", k=(player, 'play'))]
         ], k=(player, "city"), vertical_alignment='top'),
            sg.VSep("black")]


def score_window_layout(game: MetropolisGame):
    layout: list[list] = [[sg.Button("End round and score cities", k='deal_and_score')]]
    player_rows = []
    for player in game.players:
        player_rows.extend(player_row_score(player, game.unique_cards))
    player_rows.pop()  # remove final VSep
    layout.append(player_rows)
    return layout


def event_loop(game: MetropolisGame):
    layout = score_window_layout(game)
    window = sg.Window("Metropolis", layout, resizable=True)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            another_game = end_screen(game)
            break

        if event == "deal_and_score":
            for player in game.players:
                window[player, 'total_score'].update(f"Score: {player.update_score()} points")

            if game.has_winner():
                another_game = end_screen(game)
                break

        if type(event) == tuple and event[1] == "play":
            player: MetropolisPlayer = event[0]
            card: MetropolisCard = values[player, "cards_to_play"]
            # play cards
            try:
                player.play_card(card)
            except ValueError:
                pass  # we get a value error since we try to remove cards that the player dont have
            # update screen
            window.extend_layout(window[player, "city"], card.layout())
            window[player, 'city_score'].update(f"City: {player.city_points()} points")

    window.close()
    return another_game


if __name__ == "__main__":
    players2 = [MetropolisPlayer('Wessel', []), MetropolisPlayer('fiets', [])]
    game2 = MetropolisGame(normal_deck)
    for player2 in players2:
        game2.add_player(player2)
    # players2[0].score = 55
    game2.start_game()
    # players2[0].hand.extend([school])
    event_loop(game2)
