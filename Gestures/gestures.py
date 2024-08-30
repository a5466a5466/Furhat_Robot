from os import listdir, path
from json import load


class Gestures:

    __GESTURES_PATH: str = "gestures/"
    __FILE_TYPE: str = ".json"

    GESTURE_NAME_KEY: str = "name"
    __GESTURE_FRAMES_KEY: str = "frames"
    __GESTURE_TIME_KEY: str = "time"

    def __init__(self) -> None:
        self.__gestures_data: dict[str: dict] = dict()
        self.load_gestures_data()

    def load_gestures_data(self) -> None:
        for file_name in listdir(self.__GESTURES_PATH):
            if file_name.endswith(self.__FILE_TYPE):
                file_path: str = path.join(self.__GESTURES_PATH, file_name)

                with open(file_path, 'r') as file:
                    gesture_data: dict = load(file)
                    self.__gestures_data[gesture_data[self.GESTURE_NAME_KEY]] = gesture_data

    def get_gestures_data(self) -> dict[str: dict]:
        return self.__gestures_data

    def get_gesture_time(self, gesture: dict) -> float:
        gesture_final_frame: dict = self.__gestures_data[gesture[self.GESTURE_NAME_KEY]][self.__GESTURE_FRAMES_KEY][-1]
        return gesture_final_frame[self.__GESTURE_TIME_KEY][0]
