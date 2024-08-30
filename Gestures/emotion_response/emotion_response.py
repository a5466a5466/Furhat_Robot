from emotion_response.furhat import Furhat
from gestures import Gestures
from time import sleep


class EmotionResponse:

    _GESTURES: dict[str: list[str]] = {
        'anger': ['anger'],
        'disgust': ['disgust'],
        'fear': ['fear'],
        'happiness': ['happiness'],
        'neutral': ['neutral'],
        'sadness': ['sadness'],
        'surprise': ['surprise']
    }
    __PAUSE_TIME: float = 1.0

    def __init__(self, gesture: dict = None) -> None:
        self._gesture: dict = gesture
        self._furhat: Furhat = Furhat()

    def get_gesture(self) -> dict:
        return self._gesture

    def set_gesture(self, gesture: dict) -> None:
        self._gesture = gesture

    def display_gesture(self, is_blocking: bool = False, is_verbal: bool = False) -> None:
        if self._gesture:
            if is_verbal:
                self._furhat.get_connection().say(text=self._gesture[Gestures.GESTURE_NAME_KEY], blocking=is_blocking)
                sleep(self.__PAUSE_TIME)
            self._furhat.get_connection().gesture(body=self._gesture, blocking=is_blocking)
            sleep(self.__PAUSE_TIME)

    @classmethod
    def get_gesture_names(cls) -> dict[str: list[str]]:
        return cls._GESTURES
