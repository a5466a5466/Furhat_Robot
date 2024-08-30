from emotion_response.emotion_response import EmotionResponse


class EmotionResponseSurprise(EmotionResponse):

    _GESTURES: dict[str: list[str]] = {'surprise': EmotionResponse.get_gesture_names()['surprise']}

    def __init__(self, gesture: dict = None) -> None:
        super().__init__(gesture=gesture)
