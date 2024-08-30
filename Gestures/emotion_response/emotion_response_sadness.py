from emotion_response.emotion_response import EmotionResponse


class EmotionResponseSadness(EmotionResponse):

    _GESTURES: dict[str: list[str]] = {'sadness': EmotionResponse.get_gesture_names()['sadness']}

    def __init__(self, gesture: dict = None) -> None:
        super().__init__(gesture=gesture)
