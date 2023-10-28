import patience2 as patience
import PySimpleGUI as sg


sg.theme('GreenTan')


def makeMainMenu():
    return sg.Window("Patience Hoofdmenu",
                     layout=[[sg.Text("Welkom bij Patience")],
                             [sg.Button("Start!"), sg.Button("Exit")],
                             [sg.Text("Geprogrammeerd door Wessel Heerink")]]
                     )


mainMenu = makeMainMenu()
event, values = mainMenu.read()

if event == 'Start!':
    reset = True
    k = True
    while reset:
        if k:
            k = False
            mainMenu.close()
        reset = patience.main()
else:
    mainMenu.close()
