from emotion_response.emotion_response_factory import EmotionResponseFactory
from emotion_response.emotion_response import EmotionResponse
from gestures import Gestures
from cli import cli


def main() -> None:
    gestures: Gestures = Gestures()
    emotion_response_factory: EmotionResponseFactory = EmotionResponseFactory(gestures=gestures.get_gestures_data())
    emotion_responses: dict[str: EmotionResponse] = emotion_response_factory.get_emotion_responses()

    is_display_emotion, emotion_to_display = cli()  # get user input from cli for displaying gesture(s)
    if is_display_emotion:
        if emotion_to_display is not None:
            # display cli-requested gesture
            emotion_responses[emotion_to_display].display_gesture(is_verbal=True)
        else:
            # display all gestures in sequence for demo
            for emotion_response in emotion_responses.keys():
                emotion_responses[emotion_response].display_gesture(is_blocking=True, is_verbal=True)


if __name__ == "__main__":
    main()
