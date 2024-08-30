import time
import random
from furhat_remote_api import FurhatRemoteAPI
from emo_capture import emo_capture
import json



def reply_greeting(emotion):
    reply = {
        'neutral': ['Your facial expression speaks of calm; let\'s embrace this stillness and delve into our practice.',
                    'Your calm demeanor is a perfect starting point for our mindfulness journey;'
                    'let\'s savor this tranquility.',
                    'No matter how you feel now, each emotion is welcomed here; let\'s begin with an open mind.'],
        'anger': ['I see some tension—acknowledging and navigating through it mindfully can be a helpful practice.',
                  'I sense your anger, let\'s allow it to unfold and dissipate as we center ourselves through mindfulness.',
                  'I can see your anger; let\'s embrace it without judgment and find peace through our mindfulness journey.'],
        'disgust': ['I notice a facial expression reflecting some discomfort,'
                    'let\'s acknowledge it and guide our focus to the present.',
                    'Whether it\'s discomfort or something else, let\'s use our practice to navigate through these feelings.',
                    'If there\'s a sense of disgust, let\'s approach it with mindfulness, creating space for understanding.'],
        'fear': ['I see a hint of concern, embracing it and practicing mindfulness can help bring a sense of calm.',
                 'Your face reflects a touch of fear; let\'s explore this emotion mindfully and find comfort in the breath.',
                 'If there\'s fear present, let\'s shift our focus and find strength in the present.'],
        'happiness': ['Your joyful expression is wonderful, let\'s embrace this positive energy through mindfulness.',
                      'Your happy face is a beautiful starting point, let\'s use this positive energy to deepen our practice.',
                      'I see happiness on your face, let\'s allow the joy to enhance our connection to the present moment.'],
        'sadness': ['I see a touch of sadness; let\'s embrace it without judgment and allow the breath to bring comfort.',
                    'Your face shows a bit of sadness, let\'s mindfully explore and release any emotional weight.',
                    'Your expression suggests a bit of sadness;'
                    'let\'s approach it with gentleness and breathe through these emotions.'],
        'surprise': ['I see surprise on your face, let\'s use this curiosity to deepen our mindfulness experience.',
                     'I notice surprise; let\'s use it to enhance our connection to the present.',
                     'Your face reflects surprise; let\'s weave it into our mindfulness practice.'],
    }
    return random.choice(reply[emotion])


def reply_during_meditation(emotion):
    reply = {
        # 'neutral': ['neutral'],
        'anger': ['As you notice anger, gently redirect your focus to the calming rhythm of your breath.',
                  'Acknowledge your sensation without judgment, and allow the intensity to gradually subside.',
                  'Let the energy flow, and channel it into the present moment.'],
        'disgust': ['If you feel discomfort, let it pass like a wave, and return to the neutrality of your breath.',
                    'Visualize exhaling stress with each breath, allowing yourself to find a calmer state of mind.',
                    'Remember, it\'s natural for discomfort to surface, and you are cultivating resilience and presence with each breath.'],
        'fear': ['Sense the feeling of fear, inhale strength, and exhale any anxiety, trusting in your resilience.',
                 'In the presence of fear, ground yourself with safety by feeling the support beneath you.',
                 'Recognize that you are safe in this moment, and breathe into a sense of security.'],
        'happiness': ['Embrace the warmth of happiness, let it fill you, and breathe in the joy of the moment.',
                      'If a joyful memory surfaces, let it enrich your experience and gently bring your focus back.',
                      'Allow the positive energy to coexist with your mindfulness practice.'],
        'sadness': ['Notice the presence of sadness, inhale acceptance, and exhale, letting go of emotional weight.',
                    'Allow each breath to bring a bit of ease and acceptance, understanding that it\'s okay to feel this way.',
                    'Breathe in self-compassion, and exhale, releasing the burden.'],
        'surprise': ['Notice the unexpected with a gentle awareness, breathe in the novelty, and let the breath ground you in the present.',
                     'If your mind begins to wander, gently acknowledge the thoughts and guide your attention back to the breath.',
                     'If distractions arise, let the rhythm of your breath anchor you back into the present moment.'],
    }
    return random.choice(reply[emotion])


def main():
    fSmile = open('./Gesture/Smile.json', 'r')
    SmileGesture = json.load(fSmile)
    fBigSmile = open('./Gesture/Big smile.json', 'r')
    BigSmileGesture = json.load(fBigSmile)
    fGoodbye = open('./Gesture/Goodbye.json', 'r')
    GoodbyeGesture = json.load(fGoodbye)

    # Setup furhat
    furhat = FurhatRemoteAPI('localhost')
    furhat.set_voice(name='Matthew')

    # Greetings
    furhat.gesture(name="BigSmile")
    furhat.say(text='Hi, I am your mindfulness coach. How are you?')
    furhat.gesture(name="BrowRaise")
    # Capture emotion
    emotion = emo_capture()
    print(emotion[0])
    if emotion[0] == emotion[0]:    # Emotion captured
        furhat.say(text=reply_greeting(emotion[0]))

    # Prepare for meditation
    furhat.gesture(name="Nod")
    furhat.say(text='We can now start a two minute meditation. Sit on your chair in a relaxed posture.'
                    'Close your eyes if you feel comfortable doing so, or maintain a soft gaze.')

    timer = 120     # 2 minutes
    start = time.time()
    change = 0      # count emotion changes

    # Start meditation
    furhat.say(text='Begin by taking a few deep breaths, inhaling through your nose, and exhaling through your mouth.'
                    'Focus on the sensation of your breath. Notice the natural rhythm of the rise and fall.'
                    'Settle yourself into the present moment, and let go of any tension.')
    time.sleep(15)
    while True:
        now = time.time()
        if now - start >= timer:
            break
        time.sleep(5)

        # Capture emotion changes
        emotion = emo_capture()
        if emotion[0] != emotion[0]:    # No face captured
            furhat.say(text='Are you still here?')
            continue
        print(emotion[0])
        if emotion[0] == 'neutral':     # No emotion changes
            continue
        # Emotion change captured
        change += 1
        reply = reply_during_meditation(emotion[0])
        furhat.say(text=reply)
        time.sleep(5)

    # Finish meditation and evaluate performance
    furhat.gesture(name="Nod")
    furhat.say(text='As we conclude the meditation, slowly bring your awareness back.'
                    'Open your eyes if they are closed, and Keep the mindfulness in mind.')
    if change <= 3:
        furhat.gesture(body=BigSmileGesture)
        furhat.say(text='Well done for dedicating time to your practice!'
                        'Each moment of mindfulness contributes to your well-being and growth.')
    else:
        furhat.gesture(body=SmileGesture)
        furhat.say(text='It\'s completely normal to have moments that feel challenging.'
                        'Be compassionate with yourself. The important thing is that you showed up and gave it a try.')

    # Farewell
    furhat.gesture(name="Nod")
    furhat.say(text='Thank you for practicing with me. I wish you a pleasant and productive day. Goodbye.')
    furhat.gesture(body=GoodbyeGesture)

    fSmile.close()
    fBigSmile.close()
    fGoodbye.close()


if __name__ == '__main__':
    main()
