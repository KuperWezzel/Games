import PySimpleGUI as sg
from metropolis.MetropolisGame import MetropolisGame
from metropolis.MetropolisPlayer import MetropolisPlayer
from metropolis.MetropolisCard import MetropolisCard
from cards import normal_deck, architect, onderzoekscentrum, monument
from helper import text_generator


def player_row(player: MetropolisPlayer):
    cards = [architect] + sorted(player.hand)
    return [sg.Col(
        [[sg.Push(), sg.T(player.name), sg.Push()],
         [sg.T("Score: 0 points", k=(player, "total_score")), sg.T("City: 0 points", k=(player, "city_score"))],
         [sg.T("Choose next card to play")],
         [sg.Push(), sg.DropDown(cards, k=(player, "card_to_play"), readonly=True, default_value=cards[0]), sg.Button("Play card", k=(player, 'play')), sg.Push()]
         ], k=(player, "city"), vertical_alignment='top'),
            sg.VSep("black")]


def game_window_layout(game: MetropolisGame):
    sg.theme("DarkGreen")
    layout: list[list] = [[sg.Button("Deal cards to all players", k='deal')]]
    player_rows = []
    for player in game.players:
        player_rows.extend(player_row(player))
    player_rows.pop()
    layout.append(player_rows)
    return layout


def update_card_combo(window, player: MetropolisPlayer):
    if architect in player.city:
        playable_cards = sorted(player.hand)
    else:
        playable_cards = sorted([architect] + player.hand)
    window[player, 'card_to_play'].update(values=playable_cards, value=playable_cards[0])


def discard_layout(amount_to_discard: int, cards_to_choose_from: list[MetropolisCard]):
    layout: list[list] = [[sg.T(f"Choose {amount_to_discard} cards to discard:")],
                          [sg.Listbox(cards_to_choose_from, key='cards', size=(20, len(cards_to_choose_from)),
                                      select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE)],
                          [sg.Submit(k='submit')]]
    return layout


def discard_popup(amount_to_discard: int, cards_to_choose_from: list[MetropolisCard] = None, layout=None):
    if layout is None:
        layout = discard_layout(amount_to_discard, cards_to_choose_from)
    window = sg.Window("", layout, modal=True, no_titlebar=True)
    while True:
        event, values = window.read()

        if event == 'submit':
            cards = values['cards']
            if len(cards) != amount_to_discard:
                sg.popup_timed(f"You need to select exactly {amount_to_discard} cards, but you selected {len(cards)} cards!", no_titlebar=True, auto_close_duration=3)
                continue
            else:
                break
    window.close()
    return cards


def event_loop(game: MetropolisGame):
    layout = game_window_layout(game)
    window = sg.Window("Metropolis", layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            print("closing...")
            break

        if event == "deal":
            game.deal_cards_income()
            for player in game.players:
                update_card_combo(window, player)

        if type(event) == tuple and event[1] == "play":
            player: MetropolisPlayer = event[0]
            card1: MetropolisCard = values[player, "card_to_play"]
            cards = [card1]
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
                window[player, 'city_score'].update(f"City: {player.points()} points")
                window[player, 'total_score'].update(f"Score: {player.score} points")
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
