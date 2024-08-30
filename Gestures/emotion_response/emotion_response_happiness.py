from emotion_response.emotion_response import EmotionResponse


class EmotionResponseHappiness(EmotionResponse):

    _GESTURES: dict[str: list[str]] = {'happiness': EmotionResponse.get_gesture_names()['happiness']}

    def __init__(self, gesture: dict = None) -> None:
        super().__init__(gesture=gesture)
