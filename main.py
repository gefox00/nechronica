import json, requests, pyperclip, os
import PySimpleGUI as sg

layout = [[sg.Text('URL'), sg.Input(key='-URL-'),sg.Button('データ取得', key='-GET_DATA-')],
          [sg.Button('変換開始', key='-CONVERT-'),
           sg.Button('クリップボードにコピー', key='-CLIP-'),
           sg.Button('履歴から取得', key='-LIST-')],
          [sg.Output(key='-OUT-',size=(61,20))]
          ]


window = sg.Window('sample', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-CONVERT-':
        pass
    if event == '-CLIP-':
        print('clip')
    if event == '-GET_DATA-':

        res = requests.get('')
        print(values['-URL-'])
window.close()