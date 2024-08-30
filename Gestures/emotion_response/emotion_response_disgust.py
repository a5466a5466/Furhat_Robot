from emotion_response.emotion_response import EmotionResponse


class EmotionResponseDisgust(EmotionResponse):

    _GESTURES: dict[str: list[str]] = {'disgust': EmotionResponse.get_gesture_names()['disgust']}

    def __init__(self, gesture: dict = None) -> None:
        super().__init__(gesture=gesture)
