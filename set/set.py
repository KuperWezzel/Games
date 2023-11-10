from set_functions import make_shuffled_deck as make_deck
import PySimpleGUI as sg


if __name__ == "__main__":
    # default values
    empty_card = "images/empty.png"
    num_card_rows = 3
    num_card_cols = 6
    start_cols = 4
    num_cards = num_card_rows * start_cols
    active_cards = []
    giving_point = False

    # values to be set
    num_players = 3

    # put first cards on the board and remove them from the deck
    deck = make_deck()

    card_rows = []
    for i in range(num_card_rows):
        row_j = []
        card_rows.append(row_j)
        for j in range(num_card_cols):
            if j < start_cols:
                card = deck.pop()
                card.location = ("b", i, j)
                row_j.append(sg.Image(card.image, key=card.location, enable_events=True, subsample=7, metadata=card))
            else:
                row_j.append(sg.Image(empty_card, key=("b", i, j), enable_events=True, subsample=7))

    button_row = [sg.B("Add three cards", key=("k", "add")), sg.B("Check for sets", key=("k", "check"))]

    score_row = []
    for i in range(num_players):
        score_row.append(sg.T(f"Player {i+1} \nScore: 0", key=("s", i+1), enable_events=True, s=(20, 2), metadata={"score": 0}))

    layout = [
        card_rows,
        [sg.HSeparator()],
        button_row,
        [sg.HSeparator()],
        score_row,
    ]

    sg.theme('Green')
    window = sg.Window("SET!", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            print("closing...")
            break

        if event is not None:
            meta = window[event].metadata
        else:
            meta = None

        print(event, meta)

        # clicking a (non-empty) card on the board
        if event[0] == 'b' and not giving_point and meta is not None:
            card = meta

            # flip active stated and add/remove from list
            card.active = not card.active
            if card.active:
                active_cards.append(card)
                # window[event].update(background_color="orange")
            else:
                active_cards.remove(card)
                # window[event].update(background_color="green")

            if len(active_cards) == 3:
                if not card.is_set(*active_cards[:2]):
                    # set is incorrect
                    for old_card in active_cards:
                        # window[old_card].update(background_color="green")
                        old_card.active = False
                    active_cards = []
                else:
                    # set is correct, so let players click on player who scored
                    giving_point = True

        if event[0] == 's' and giving_point:
            # give point
            meta["score"] += 1
            window[event].update(f"Player {event[1]} \nScore: {meta['score']}")

            for old_card in active_cards:
                old_card.active = False

            # put new cards
            if deck and num_cards == 12:
                for old_card in active_cards:
                    i, j = old_card.location[1:]
                    new_card = deck.pop()
                    new_card.location = old_card.location
                    window[old_card.location].update(new_card.image, subsample=7)
                    window[old_card.location].metadata = new_card
                    # window[old_card.location].update(background_color="green")
            else:  # there were more than 12 cards, so don't put down extra
                active_cards.sort(key=lambda c: 10 * c.location[1] - c.location[2])
                old_max_col = num_cards // 3 - 1
                for k in range(3):
                    card_to_move = window[("b", k, old_max_col)].metadata
                    window[card_to_move.location].update(empty_card, subsample=7)
                    window[card_to_move.location].metadata = None

                    if card_to_move not in active_cards:  # card on right-most column is not in set
                        for old_card in active_cards:
                            if old_card.location[2] != old_max_col:
                                card_to_move.location = old_card.location
                                window[old_card.location].update(card_to_move.image, subsample=7)
                                window[old_card.location].metadata = card_to_move
                                active_cards.remove(old_card)
                                # window[old_card.location].update(background_color="green")
                                break
                num_cards -= 3

            active_cards = []
            giving_point = False

        if event == ("k", "add") and not giving_point and deck:
            j = num_cards//3
            for i in range(num_card_rows):
                new_card = deck.pop()
                new_card.location = ("b", i, j)
                window[new_card.location].update(new_card.image, subsample=7)
                window[new_card.location].metadata = new_card
            num_cards += 3

        if event == ("k", "check"):
            set_exists = False
            for k in range(num_cards):
                if set_exists:
                    break
                ki = k % num_card_rows
                kj = k // num_card_rows
                c1 = window[("b", ki, kj)].metadata
                for l in range(k+1, num_cards):
                    if set_exists:
                        break
                    li = l % num_card_rows
                    lj = l // num_card_rows
                    c2 = window[("b", li, lj)].metadata
                    for m in range(l+1, num_cards):
                        if set_exists:
                            break
                        mi = m % num_card_rows
                        mj = m // num_card_rows
                        c3 = window[("b", mi, mj)].metadata
                        set_exists = c1.is_set(c2, c3)
            if set_exists:
                sg.popup("At least one set can be found")
                # print(c1, c2, c3)
            else:
                sg.popup("No sets can be found")

        print(active_cards)
