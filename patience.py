from cards import fullDeck, Deck
import PySimpleGUI as sg
from time import time


def main():
    global moving, moving_from, moving_card, cards_picked_up
    # variables
    eztestmodus = False  # if True, will not shuffle cards before dealing and number of cards turned is 1 instead of 3
    cards_picked_up = 0
    moving = False
    moving_card = None
    moving_from = ""
    hidden = "Gesloten kaart"
    sg.theme('GreenTan')
    reset = False

    # creating the board and stacks
    stack = fullDeck()
    num_cards = len(stack.cards)
    if not eztestmodus:
        stack.shuffle()
    board = [Deck() for _ in range(7)]
    for i in range(7):
        for j in range(7-i):
            if j == 6-i:
                stack.cards[0].hidden = False
            board[6 - i].moveToSelf([stack.cards[0]])
    Aces = {'-HAas-': Deck(), '-KAas-': Deck(), '-SAas-': Deck(), '-RAas-': Deck()}

    # card columns
    def card_column(layo):
        return sg.Column(layo, vertical_alignment='top')

    card_col = []
    for i in range(7):
        col_j = []
        for j in range(i+1):
            if j == i:
                col_j.append([sg.Text(str(board[i].cards[j]), key=f'-{i},0{j}cc-', enable_events=True, s=(15, 1), text_color=board[i].cards[j].suit.colour, metadata={"h": False, "f": True})])
            else:
                col_j.append([sg.Text(hidden, key=f'-{i},0{j}cc-', enable_events=True, s=(15, 1), text_color='grey', metadata={"h": True, "f": True})])
        for k in range(12+7-i):
            col_j.append([sg.Text("", key=f'-{i},0{i+k+1}cc-', enable_events=True, s=(15, 1), metadata={"h": False, "f": False})])
        card_col.append(col_j)
    # print(board)

    # ace columns
    ace_col1 = [[sg.Text("Ruimte voor Harten Aas", key='-HAas-', text_color='red', relief=sg.RELIEF_SOLID, border_width=1, size=(20, 1), enable_events=True)],
                [sg.Text("Ruimte voor Ruiten Aas", key='-RAas-', text_color='red', relief=sg.RELIEF_SOLID, border_width=1, size=(20, 1), enable_events=True)]]
    ace_col2 = [[sg.Text("Ruimte voor Schoppen Aas", key='-SAas-', relief=sg.RELIEF_SOLID, border_width=1, size=(20, 1), enable_events=True)],
                [sg.Text("Ruimte voor Klaveren Aas", key='-KAas-', relief=sg.RELIEF_SOLID, border_width=1, size=(20, 1), enable_events=True)]]

    # Full layout
    layout = [
        [sg.HSeparator()],
        [
            sg.VSeparator(),
            card_column(card_col[0]), sg.VSeperator(),
            card_column(card_col[1]), sg.VSeperator(),
            card_column(card_col[2]), sg.VSeperator(),
            card_column(card_col[3]), sg.VSeperator(),
            card_column(card_col[4]), sg.VSeperator(),
            card_column(card_col[5]), sg.VSeperator(),
            card_column(card_col[6]), sg.VSeparator()
        ],
        [sg.HSeparator()],
        [
            sg.Column(ace_col1), sg.Column(ace_col2),
            sg.Text(f"aantal: {len(stack.cards)}", key='-closed_stack-', relief=sg.RELIEF_SOLID, border_width=1),
            sg.Text(str(stack.cards[0]), key="-open_stack-", size=(15, 1), text_color=stack.cards[0].suit.colour, relief=sg.RELIEF_SOLID, border_width=1, enable_events=True),
            sg.Button("Draaien", key='-Draaien-'), sg.Button("Reset", key="-reset-"), sg.Button("Exit", key='-exit-')
        ]
    ]

    window = sg.Window("Patience", layout)

    # function for checking whether you are moving a card
    def stop_moving():
        global moving, moving_from, moving_card, cards_picked_up
        if moving:
            for k in range(cards_picked_up):
                if k == 0:
                    window[moving_from].update(background_color=sg.theme_background_color())
                else:
                    window[f"-{moving_from[1]},0{int(moving_from[-5:-3]) + k}cc-"].update(background_color=sg.theme_background_color())
            moving = False
            moving_card = None
            moving_from = ""
            cards_picked_up = 0

    def start_moving():
        global moving, moving_from, moving_card
        if not moving:
            moving = True
            moving_from = event
            for k in range(cards_picked_up):
                if k == 0:
                    window[event].update(background_color="lightgreen")
                else:
                    window[f"-{event[1]},0{int(event[-5:-3]) + k}cc-"].update(background_color="lightgreen")

    start_time = time()
    # main event loop
    while True:
        event, values = window.read()
        print(event, values)

        if event is not None:
            meta = window[event].metadata
        else:
            meta = None

        if event == sg.WIN_CLOSED:
            print("closing...")
            break

        elif event == '-exit-':
            confirm = sg.Window("Exit?", layout=[[sg.Text("Weet je zeker dat je wilt stoppen?")], [sg.Button("Ja"), sg.Button("Nee")]])
            event2, values2 = confirm.read()
            if event2 == 'Ja':
                confirm.close()
                break
            confirm.close()

        elif event == '-reset-':
            confirm = sg.Window("Reset?", layout=[[sg.Text("Weet je zeker dat je opnieuw wilt beginnen?")], [sg.Button("Ja"), sg.Button("Nee")]])
            event3, values3 = confirm.read()
            if event3 == 'Ja':
                reset = True
                confirm.close()
                break
            confirm.close()

        elif event == "-Draaien-" and len(stack.cards) > 0:
            print("Draaien", len(stack.cards))

            stop_moving()

            if eztestmodus:
                stack.moveBottomToTop(1)
            else:
                stack.moveBottomToTop(3)
            window["-open_stack-"].update(str(stack.cards[0]), text_color=stack.cards[0].suit.colour)

        elif event == "-open_stack-" and len(stack.cards) > 0:
            print("open_stack")

            stop_moving()

            cards_picked_up = 1
            start_moving()
            moving_card = stack.cards[0]

        elif event[-4:] == "Aas-":
            print(f"{event[1]}Aas")
            if moving:
                print(event[1], moving_card.suit.name[0], len(Aces[event].cards), moving_card.value)
                is_movable = (moving_card.is_top() and moving_from == "-open_stack-") or (moving_card.is_bottom() and moving_from[-3:] == "cc-")
                if event[1] == moving_card.suit.name[0] and len(Aces[event].cards) == moving_card.value - 1 and is_movable:
                    # to part
                    window[event].update(str(moving_card), text_color=moving_card.suit.colour)
                    # board part
                    Aces[event].moveToSelf([moving_card])
                    # from part
                    if moving_from == "-open_stack-":
                        window["-closed_stack-"].update(f"aantal: {len(stack.cards)}")
                        if len(stack.cards) > 0:
                            window["-open_stack-"].update(str(stack.cards[0]), text_color=stack.cards[0].suit.colour)
                        else:
                            window["-open_stack-"].update("Geen kaarten meer", text_color='grey')
                    else:  # moving from board to ace stacks
                        window[moving_from].update("")
                        window[moving_from].metadata = {"h": False, "f": False}
            stop_moving()

        elif event[-3:] == "cc-":
            print("cc", event[1], event[-5:-3])
            if moving and not meta['h'] and meta['f']:  # try placing card(s)
                print("normal placing cards")
                placing_on = board[int(event[1])].cards[int(event[-5:-3])]
                if placing_on.suit.colour != moving_card.suit.colour and placing_on.value == moving_card.value + 1 and placing_on.is_bottom() and event[1] != moving_from[1]:
                    # to part
                    for k in range(cards_picked_up):
                        if k == 0:
                            window[f'-{event[1]},0{int(event[-5:-3]) + 1 + k}cc-'].update(str(moving_card), text_color=moving_card.suit.colour)
                        else:
                            window[f'-{event[1]},0{int(event[-5:-3]) + 1 + k}cc-'].update(str(board[int(moving_from[1])].cards[int(moving_from[-5:-3]) + k]), text_color=board[int(moving_from[1])].cards[int(moving_from[-5:-3]) + k].suit.colour)
                        window[f'-{event[1]},0{int(event[-5:-3]) + 1 + k}cc-'].metadata = {"h": False, "f": True}

                    # board part
                    if cards_picked_up == 1:
                        board[int(event[1])].moveToSelf([moving_card])
                    else:
                        board[int(event[1])].moveToSelf(board[int(moving_from[1])].cards[int(moving_from[-5:-3]):])

                    # from part
                    if moving_from == "-open_stack-":  # same as lines 152-160
                        window["-closed_stack-"].update(f"aantal: {len(stack.cards)}")
                        if len(stack.cards) > 0:
                            window["-open_stack-"].update(stack.cards[0], text_color=stack.cards[0].suit.colour)
                        else:
                            window["-open_stack-"].update("Geen kaarten meer", text_color='grey')
                    else:  # moving from board to board
                        for k in range(cards_picked_up):
                            window[f'-{moving_from[1]},0{int(moving_from[-5:-3]) + k}cc-'].update("")
                            window[f'-{moving_from[1]},0{int(moving_from[-5:-3]) + k}cc-'].metadata = {"h": False, "f": False}
                stop_moving()

            elif moving and not meta['h'] and not meta['f'] and len(board[int(event[1])].cards) == 0:  # place at top of empty column
                print("placing cards at empty top")
                # to part
                for k in range(cards_picked_up):
                    if k == 0:
                        window[f'-{event[1]},00cc-'].update(str(moving_card), text_color=moving_card.suit.colour)
                    else:
                        window[f'-{event[1]},0{k}cc-'].update(str(board[int(moving_from[1])].cards[int(moving_from[-5:-3]) + k]), text_color=board[int(moving_from[1])].cards[int(moving_from[-5:-3]) + k].suit.colour)
                    window[f'-{event[1]},0{k}cc-'].metadata = {"h": False, "f": True}

                # board part
                if cards_picked_up == 1:
                    board[int(event[1])].moveToSelf([moving_card])
                else:
                    board[int(event[1])].moveToSelf(board[int(moving_from[1])].cards[int(moving_from[-5:-3]):])

                # from part
                if moving_from == "-open_stack-":  # same as lines 130-137
                    window["-closed_stack-"].update(f"aantal: {len(stack.cards)}")
                    if len(stack.cards) > 0:
                        window["-open_stack-"].update(stack.cards[0], text_color=stack.cards[0].suit.colour)
                    else:
                        window["-open_stack-"].update("Geen kaarten meer", text_color='grey')
                else:  # moving from board to board
                    for k in range(cards_picked_up):
                        window[f'-{moving_from[1]},0{int(moving_from[-5:-3]) + k}cc-'].update("")
                        window[f'-{moving_from[1]},0{int(moving_from[-5:-3]) + k}cc-'].metadata = {"h": False, "f": False}
                stop_moving()

            elif not moving and not meta['h'] and meta['f']:  # pick up card(s)
                print("picking up cards")
                cards_picked_up = len(board[int(event[1])].cards[int(event[-5:-3]):])
                start_moving()
                moving_card = board[int(event[1])].cards[int(event[-5:-3])]
                print(cards_picked_up, moving_card, board[int(event[1])].cards[int(event[-5:-3]):])

            elif meta['h'] and board[int(event[1])].cards[int(event[-5:-3])].is_bottom():  # hidden card
                print("turning hidden cards")
                stop_moving()
                window[event].metadata['h'] = False
                window[event].update(str(board[int(event[1])].cards[int(event[-5:-3])]), text_color=board[int(event[1])].cards[int(event[-5:-3])].suit.colour)

            else:
                print("nothing")
                stop_moving()

        if sum([len(suitdeck.cards) for suitdeck in Aces.values()]) == num_cards:
            tottime = round(time() - start_time)
            mins, secs = divmod(tottime, 60)
            sg.popup(f"Gefeliciteerd! Je hebt gewonnen! \nJe deed er {mins} minuten en {secs} seconden over.")
            # reset()

    window.close()
    return reset