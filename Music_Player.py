import PySimpleGUI as sg

sg.theme('reddit')

play_layout = [
    [sg.Text('Song name')]
]

volume_layout = [
    [sg.Slider(range = (0, 100))]
]

layout = [
    [sg.TabGroup([[sg.Tab('Play', play_layout),sg.Tab('Volume', volume_layout)]])]
    ]

window = sg.Window('Music Player', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()