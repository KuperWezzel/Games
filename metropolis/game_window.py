import PySimpleGUI as sg
from metropolis.MetropolisGame import MetropolisGame
from metropolis.MetropolisPlayer import MetropolisPlayer
from metropolis.MetropolisCard import MetropolisCard
from cards import normal_deck, architect
from helper import text_generator


def player_row(player: MetropolisPlayer):
    cards = [architect] + sorted(player.hand)
    return [sg.Col(
        [[sg.Push(), sg.T(player.name), sg.Push()],
         [sg.T("Score: 0 points", k=(player, "total_score")), sg.T("City: 0 points", k=(player, "city_score"))],
         [sg.T("Choose next cards to play")],
         [sg.Listbox(cards, k=(player, "cards_to_play"), s=(20, 12), no_scrollbar=True,
                     select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE)],
         [sg.Button("Play card", k=(player, 'play'))]
         ], k=(player, "city"), vertical_alignment='top'),
            sg.VSep("black")]


def game_window_layout(game: MetropolisGame):
    sg.theme("DarkGreen")
    layout: list[list] = [[sg.Button("End round and deal cards", k='deal_and_score')]]
    player_rows = []
    for player in game.players:
        player_rows.extend(player_row(player))
    player_rows.pop()  # remove final VSep
    layout.append(player_rows)
    return layout


def update_card_combo(window, player: MetropolisPlayer):
    if architect in player.city:
        playable_cards = sorted(player.hand)
    else:
        playable_cards = sorted([architect] + player.hand)
    window[player, 'cards_to_play'].update(values=playable_cards)


def discard_popup(amount_to_discard: int, cards_to_choose: list[MetropolisCard]):
    sg.theme("DarkBlue")
    layout: list[list] = [[sg.Frame("", [[sg.T(f"Choose {amount_to_discard} cards to discard:")],
                                         [sg.Listbox(cards_to_choose, key='cards', size=(20, len(cards_to_choose)),
                                                     select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, no_scrollbar=True)],
                                         [sg.Submit(k='submit')]], element_justification='center')]]
    window = sg.Window("", layout, modal=True, no_titlebar=True)
    while True:
        event, values = window.read()

        if event == 'submit':
            cards = values['cards']
            if len(cards) != amount_to_discard:
                sg.popup_timed(f"You must select exactly {amount_to_discard} cards, but you selected {len(cards)} cards!",
                               modal=True, no_titlebar=True, auto_close_duration=3, background_color="red")
                continue
            else:
                break
    window.close()
    sg.theme("DarkGreen")
    return cards


def event_loop(game: MetropolisGame):
    layout = game_window_layout(game)
    window = sg.Window("Metropolis", layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            print("closing...")
            break

        if event == "deal_and_score":
            game.deal_cards_income()
            for player in game.players:
                # check if player has too many cards
                if ...:
                    ...
                window[player, 'total_score'].update(f"Score: {player.update_score()} points")
                update_card_combo(window, player)

        if type(event) == tuple and event[1] == "play":
            player: MetropolisPlayer = event[0]
            cards: list[MetropolisCard] = values[player, "cards_to_play"]
            if player.may_play_cards(cards):
                # play cards
                player.play_cards(cards)
                # choose which to discard
                total_price = player.calculate_total_card_price(cards)
                if total_price > 0:
                    to_discard = discard_popup(total_price, player.hand)
                    player.discard_cards(to_discard)
                # update screen
                for card in cards:
                    window.extend_layout(window[player, "city"], card.layout())
                window[player, 'city_score'].update(f"City: {player.city_points()} points")
                # remove cards from inputbox
                update_card_combo(window, player)
            else:
                names = text_generator(cards, "You cannot play ", " currently")
                sg.popup_no_titlebar(names)

    window.close()


if __name__ == "__main__":
    players2 = [MetropolisPlayer('Wessel', [])]
    game2 = MetropolisGame(normal_deck)
    for player2 in players2:
        game2.add_player(player2)
    game2.start_game()
    # players2[0].hand.extend([onderzoekscentrum, monument])
    event_loop(game2)
