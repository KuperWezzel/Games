import PySimpleGUI as sg


def player_line(n: int):
    return [sg.Text(f"Player {n}", k=('txt', n)), sg.InputText(k=('in', n))]


def set_players_window():
    sg.theme('DarkGreen')
    num_players = 1
    max_players = 1
    layout = [
        [sg.Button("Add player", k='add_player'), sg.Button("Remove player", k='rem_player')],
        [sg.Col([player_line(num_players)], k='cool_fields')],
        [sg.Submit(k='submit')]
    ]

    window = sg.Window("Metropolis - Select players", layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            print("closing...")
            return []

        elif event == "submit":
            names = []
            for i in range(1, num_players + 1):
                names.append(values['in', i])
            return names

        elif event == "add_player":
            num_players += 1
            if max_players == num_players - 1:
                max_players += 1
                window.extend_layout(window["cool_fields"], [player_line(num_players)])
            else:
                window["txt", num_players].update(visible=True)
                window["in", num_players].update(visible=True)

        elif event == "rem_player" and num_players > 1:
            window["txt", num_players].update(visible=False)
            window["in", num_players].update(visible=False)
            num_players -= 1


if __name__ == "__main__":
    out = set_players_window()
    print(out)
