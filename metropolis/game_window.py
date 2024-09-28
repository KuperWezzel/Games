import PySimpleGUI as sg
from metropolis.MetropolisGame import MetropolisGame
from metropolis.MetropolisPlayer import MetropolisPlayer
from metropolis.MetropolisCard import MetropolisCard
from cards import all_cards, architect


def player_row(player):
    cards = [architect] + player.hand
    return [sg.Col(
        [[sg.Push(), sg.T(player.name), sg.Push()],
         [sg.T("Score: 0 points", k=(player, "total_score")), sg.T("City: 0 points", k=(player, "city_score"))],
         [sg.T("Choose next card to play")],
         [sg.Push(), sg.DropDown(cards, k=(player, "card_to_play"), readonly=True, default_value=cards[0]), sg.Button("Play card", k=(player, 'play')), sg.Push()]
         ], k=(player, "city"), vertical_alignment='top'),
            sg.VSep("black")]


def game_window_layout(game: MetropolisGame):
    sg.theme("DarkGreen")
    layout: list[list] = [[]]
    for player in game.players:
        layout[0].extend(player_row(player))
    layout[0].pop()

    window = sg.Window("Metropolis", layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            print("closing...")
            return

        if type(event) == tuple and event[1] == "play":
            player = event[0]
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
    game.start_game()
    game_window_layout(game)
