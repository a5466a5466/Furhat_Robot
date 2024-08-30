from furhat_remote_api import FurhatRemoteAPI


def singleton(cls) -> callable:
    instances: dict = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class Furhat:

    __FURHAT_IP: str = "127.0.1.1"  # LOCAL IP ADDRESS

    # DEFAULT LED COLOURS
    __RED: int = 0
    __GREEN: int = 220
    __BLUE: int = 179

    def __init__(self) -> None:
        self.__furhat_connection: FurhatRemoteAPI = FurhatRemoteAPI(host=self.__FURHAT_IP)
        self.__furhat_connection.set_led(red=self.__RED, green=self.__GREEN, blue=self.__BLUE)

    def get_connection(self) -> FurhatRemoteAPI:
        return self.__furhat_connection

    def set_led(self, red: int = __RED, green: int = __GREEN, blue: int = __BLUE) -> None:
        self.__furhat_connection.set_led(red=red, green=green, blue=blue)
