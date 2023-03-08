import PySimpleGUI as sg

import base64
from io import BytesIO
from PIL import Image

def base64_image_import(path):
    image = Image.open(path)

sg.theme('reddit')

play_layout = [
    [sg.Text('Song name')],
    #[sg.Button(image_data=),sg.Button(image_data=)]
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