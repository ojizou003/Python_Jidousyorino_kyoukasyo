import PySimpleGUI as sg
from datetime import datetime

layout = [
    [sg.Text("デジタル時計")],
    [sg.Text("00:00:00", key="clock", font=("Helvetica", 72))],
]

win = sg.Window("時計", layout)

while True:
    event, val = win.read(timeout=100)
    if event in ("Exit", "Quit", None):
        break
    s = datetime.now().strftime("%H:%M:%S")
    win["clock"].update(s)

win.close()
