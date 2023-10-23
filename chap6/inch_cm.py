import PySimpleGUI as sg

layout = [
    [sg.Text('インチをセンチメートルに変換します。')],
    [sg.Text('インチ'), sg.InputText(key='inch')],
    [sg.Button('変換')],
    [sg.Text('---', key='info', size=(40, 1))]
]

win = sg.Window('インチ→センチ変換', layout)

while True:
    event, val = win.read()
    if event in ('Exit', 'Quit', None):
        break
    if event == '変換':
        inch = float(val['inch'])
        cm = inch * 2.54
        s = '{0}inch = {1}cm'.format(inch, cm)
        win['info'].update(s)

win.close()