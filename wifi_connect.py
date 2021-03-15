import wifi as w


class WifiConnect:
    __wifi_list = None
    __current_connected_name = None

    def __init__(self):
        print("Created wifi")

    # When fully implemented, this should be able to scan for wifi networks
    def scan(self):
        self.__wifi_list = ["First", "Second", "Third"]

    def get_list(self):
        return self.__wifi_list

    # When fully implemented, this should be able to connect to wifi networks
    def connect(self, pod_name: str):

        # do things that connect to the pod.

        self.__current_connected_name = pod_name
        return True

    def get_connected_name(self):
        return self.__current_connected_name



