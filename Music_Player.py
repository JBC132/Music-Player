import PySimpleGUI as sg

sg.theme('reddit')

play_layout = [
    [sg.Text('Song name')]
]

volume_layout = [
    [sg.VPush()],
    [sg.Push(),sg.Slider(range = (0, 100), default_value=100, orientation='h', key='-VOLUME-'),sg.Push()],
    [sg.VPush()]
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