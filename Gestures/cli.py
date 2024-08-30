from emotion_response.emotion_response import EmotionResponse
from argparse import ArgumentParser


def cli() -> tuple[bool, str | None]:
    gestures: list[str] = [gesture for gestures in list(EmotionResponse.get_gesture_names().values())
                           for gesture in gestures]

    parser: ArgumentParser = ArgumentParser()
    parser.add_argument('--gesture', help='Gesture to display', default=None)
    args: any = parser.parse_args()

    if str(args.gesture).lower() in gestures or args.gesture is None:
        return True, str(args.gesture).lower() if args.gesture is not None else None
    print(f"Gesture '{str(args.gesture)}' is not a recognized emotional response!")
    return False, None
