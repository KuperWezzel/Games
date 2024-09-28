import PySimpleGUI as sg
from metropolis.MetropolisGame import MetropolisGame
from metropolis.MetropolisPlayer import MetropolisPlayer
from metropolis.MetropolisCard import MetropolisCard
from cards import all_cards


def player_row(player, cards):
    return [sg.Col(
        [[sg.T(player.name)],
         [sg.T("Score: 0 points", k=(player, "total_score")), sg.T("City: 0 points", k=(player, "city_score"))],
         [sg.T("Choose next card to play")],
         [sg.DropDown(cards, k=(player, "card_to_play"), readonly=True, default_value=cards[0])]
         ], k=(player, "city")),
            sg.VSep("black")]


def game_window_layout(game: MetropolisGame):
    sg.theme("DarkGreen")
    layout: list[list] = [[sg.Button("Play round", k='play')], []]
    for player in game.players:
        layout[1].extend(player_row(player, game.unique_cards))
    layout[1].pop()

    window = sg.Window("Metropolis", layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            print("closing...")
            return

        if event == "play":
            for player in game.players:
                card: MetropolisCard = values[player, "card_to_play"]
                player.play_cards([card])
                window.extend_layout(window[player, "city"], card.layout())
                window[player, 'city_score'].update(f"City: {player.points()} points")
                window[player, 'total_score'].update(f"Score: {player.score} points")


if __name__ == "__main__":
    players = [MetropolisPlayer('Wessel', [])]
    game = MetropolisGame(list(all_cards.keys()))
    for player in players:
        game.add_player(player)
    game_window_layout(game)
