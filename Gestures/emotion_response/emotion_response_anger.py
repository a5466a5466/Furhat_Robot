from emotion_response.emotion_response import EmotionResponse


class EmotionResponseAnger(EmotionResponse):

    _GESTURES: dict[str: list[str]] = {'anger': EmotionResponse.get_gesture_names()['anger']}

    def __init__(self, gesture: dict = None) -> None:
        super().__init__(gesture=gesture)
