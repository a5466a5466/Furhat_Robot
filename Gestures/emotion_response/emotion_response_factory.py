from emotion_response.emotion_response_happiness import EmotionResponseHappiness
from emotion_response.emotion_response_surprise import EmotionResponseSurprise
from emotion_response.emotion_response_disgust import EmotionResponseDisgust
from emotion_response.emotion_response_neutral import EmotionResponseNeutral
from emotion_response.emotion_response_sadness import EmotionResponseSadness
from emotion_response.emotion_response_anger import EmotionResponseAnger
from emotion_response.emotion_response_fear import EmotionResponseFear
from emotion_response.emotion_response import EmotionResponse


class EmotionResponseFactory:

    def __init__(self, gestures: dict[str: dict]) -> None:
        self.__gestures: dict[str:dict] = gestures

    def get_emotion_responses(self) -> dict[str: EmotionResponse]:
        emotion_responses: dict[str: EmotionResponse] = dict()

        for gesture_name in self.__gestures.keys():
            if gesture_name in list(EmotionResponseAnger.get_gesture_names().values())[0]:
                emotion_responses[gesture_name] = EmotionResponseAnger(self.__gestures[gesture_name])
            elif gesture_name in list(EmotionResponseDisgust.get_gesture_names().values())[0]:
                emotion_responses[gesture_name] = EmotionResponseDisgust(self.__gestures[gesture_name])
            elif gesture_name in list(EmotionResponseFear.get_gesture_names().values())[0]:
                emotion_responses[gesture_name] = EmotionResponseFear(self.__gestures[gesture_name])
            elif gesture_name in list(EmotionResponseHappiness.get_gesture_names().values())[0]:
                emotion_responses[gesture_name] = EmotionResponseHappiness(self.__gestures[gesture_name])
            elif gesture_name in list(EmotionResponseNeutral.get_gesture_names().values())[0]:
                emotion_responses[gesture_name] = EmotionResponseNeutral(self.__gestures[gesture_name])
            elif gesture_name in list(EmotionResponseSadness.get_gesture_names().values())[0]:
                emotion_responses[gesture_name] = EmotionResponseSadness(self.__gestures[gesture_name])
            elif gesture_name in list(EmotionResponseSurprise.get_gesture_names().values())[0]:
                emotion_responses[gesture_name] = EmotionResponseSurprise(self.__gestures[gesture_name])

        return emotion_responses
