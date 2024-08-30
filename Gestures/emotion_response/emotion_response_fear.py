from emotion_response.emotion_response import EmotionResponse


class EmotionResponseFear(EmotionResponse):

    _GESTURES: dict[str: list[str]] = {'fear': EmotionResponse.get_gesture_names()['fear']}

    def __init__(self, gesture: dict = None) -> None:
        super().__init__(gesture=gesture)
