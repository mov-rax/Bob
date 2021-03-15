from gui_lib import *


class MainGui:
    _name: str
    _battery_percentage = 100
    _pitch = 62
    _yaw = 12
    _temp = 12

    def __init__(self, pod_name: str):
        self._name = pod_name

    def run(self):
        layout = [[sg.Text('welcome to the menu', pad=(5, 5), size=(10, 1), justification="center")],
                  [get_temperature_label(self._temp)],
                  [get_yaw_label(self._yaw)],
                  [get_pitch_label(self._pitch)],
                  [sg.Button('disconnect'), sg.Button('open/close the bud'), sg.Button('increment temp')],
                  [sg.InputText()]
                  ]

        layout2 = [[sg.Text("HELLO THERE")]]

        window = sg.Window('BUD [' + self._name.upper() + '] CONTROL PANEL', layout, resizable=True,
                           font=("Noto Sans", 12), location=(250, 250))
        while True:
            event, values = window.read()
            if event == 'increment temp':
                self._temp += 1
                window["TEMP"].Update(value=get_temperature_str(self._temp))
                print(self._temp)
            elif event == sg.WIN_CLOSED or event == 'disconnect':
                break
            print('you entered' + str(values[0]))
        window.close()


sg.theme("dark")

# variables
