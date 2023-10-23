import PySimpleGUI as sg
from datetime import datetime, timedelta

layout = [
    [sg.Text("", key="date", font=("Helvetica", 24), justification="center")],
    [sg.Text("", key="future_clock", font=("Helvetica", 72), justification="center")],
]

win = sg.Window("ちょっとだけ未来時計", layout, size=(450, 180))

while True:
    event, val = win.read(timeout=100)
    if event in ("Exit", "Quit", None):
        break
    now = datetime.now()
    future_time = now + timedelta(minutes=5)
    future_time_str = future_time.strftime("%H:%M:%S")
    date_str = future_time.strftime("%Y/%m/%d (%a)")
    win["future_clock"].update(future_time_str)
    win["date"].update(date_str)

win.close()
