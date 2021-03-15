from connect_gui import ConnectGui
from gui import MainGui

c_gui = ConnectGui()

a = [1, 2, 3, [1, 2, 3], "wee"]

while True:
    if c_gui.run():
        m_gui = MainGui(c_gui.get_connected_name())
        m_gui.run()
        print("Something happened I think!")
    else:
        print("Window closed!")
        break


