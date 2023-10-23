import PySimpleGUI as sg

layout = [
    [sg.Text('こんにちは！')],
    [sg.Text('簡単にGUIが作れます！')],
    [sg.OK()]
]

win = sg.Window('サンプル', layout)

while True:
    event, val = win.read()
    if event in ('Exit', 'Quit', None):
        break
    if event == 'OK':
        break

win.close()
