from furhat_remote_api import FurhatRemoteAPI


def main():
    # Setup furhat
    furhat = FurhatRemoteAPI('localhost')
    furhat.set_voice(name='Matthew')

    # Greetings
    furhat.say(text='Hi, I am your mindfulness coach. How are you?')
    result = furhat.listen()

    # Mindfulness meditation

    # Farewell


if __name__ == '__main__':
    main()
