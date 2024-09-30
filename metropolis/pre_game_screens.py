import PySimpleGUI as sg
from metropolis.MetropolisGame import MetropolisGame
from metropolis.MetropolisCard import DEFAULT_THEME


def player_line(n: int, name: str = ""):
    return [sg.Text(f"Player {n}", k=('txt', n)), sg.InputText(name, k=('in', n))]


def get_player_names_window(names: list[str] = None):
    if names is None:
        names = [""]
    sg.theme(DEFAULT_THEME)
    max_players = len(names)
    num_players = 0
    col = []
    for num_players, name in enumerate(names):
        col.append(player_line(num_players + 1, name))
    num_players += 1
    layout = [
        [sg.Button("Add player", k='add_player'), sg.Button("Remove player", k='rem_player')],
        [sg.Col(col, k='cool_fields')],
        [sg.Submit("Start game", k='submit')]
    ]

    window = sg.Window("Metropolis - Select players", layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            print("closing...")
            names = []
            break

        elif event == "submit":
            names = []
            for i in range(1, num_players + 1):
                names.append(values['in', i])
            break

        elif event == "add_player":
            num_players += 1
            if max_players == num_players - 1:
                max_players += 1
                window.extend_layout(window["cool_fields"], [player_line(num_players)])
            else:
                window["txt", num_players].update(visible=True)
                window["in", num_players].update(visible=True)
            window["in", num_players].set_focus()

        elif event == "rem_player" and num_players > 1:
            window["txt", num_players].update(visible=False)
            window["in", num_players].update("", visible=False)
            num_players -= 1
            window["in", num_players].set_focus()

    window.close()
    return names


def start_discard_window(game: MetropolisGame):
    layout: list[list] = [[sg.T(f"Choose 2 cards to discard:")]]
    player_rows = []
    for player in game.players:
        p_lay = [[sg.Push(), sg.T(player.name), sg.Push()],
                 [sg.Listbox(player.hand, key=(player, 'cards'), size=(20, 7),
                             select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, no_scrollbar=True)],
                 ]
        player_rows.extend([sg.Col(p_lay), sg.VSep("black")])
    player_rows.pop()  # remove final VSep
    layout.append(player_rows)
    layout.append([sg.Submit(k='submit')])

    window = sg.Window("", layout, modal=True, no_titlebar=True)
    while True:
        event, values = window.read()

        if event == 'submit':
            num_failed_players = 0
            failure_text = "Each player needs to select exactly 2 cards\n"
            for player in game.players:
                to_discard = values[player, 'cards']
                if len(to_discard) != 2:
                    num_failed_players += 1
                    failure_text += f"{player.name} selected {len(to_discard)} cards instead of 2\n"
            failure_text = failure_text[:-1]

            if num_failed_players > 0:
                sg.popup_timed(failure_text, no_titlebar=True, auto_close_duration=4+num_failed_players)
                continue
            else:
                break
    for player in game.players:
        player.discard_cards(values[player, 'cards'])
    window.close()


if __name__ == "__main__":
    out = get_player_names_window()
    print(out)
