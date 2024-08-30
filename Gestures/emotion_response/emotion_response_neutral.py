from emotion_response.emotion_response import EmotionResponse


class EmotionResponseNeutral(EmotionResponse):

    _GESTURES: dict[str: list[str]] = {'neutral': EmotionResponse.get_gesture_names()['neutral']}

    def __init__(self, gesture: dict = None) -> None:
        super().__init__(gesture=gesture)
