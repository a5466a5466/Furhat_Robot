from time import sleep
from furhat_remote_api import FurhatRemoteAPI
from numpy.random import randint
import random
# the functions, idle_animation(), LOOK_BACK(speed), LOOK_DOWN(speed=1) are used from Lab3 demo code
# IIS Assignment_3; Student: Sheng-Yu, Wu

FURHAT_IP = "127.0.1.1"

furhat = FurhatRemoteAPI(FURHAT_IP)
furhat.set_led(red=255, green=255, blue=255)

LAUGHINGSET = [
    "Ha, ha", "Hee, hee", "Ha ha, so funny", "UwU"
]

JOKESET = [
    "What does a pig put on dry skin?", "What do you call a pig that does karate?", "What do you call a fake noodle?"
]

JOKEANSWERSET = [
    "Oinkment.", "A pork chop.", "An impasta.",
]


def idle_animation():
    furhat.gesture(name="GazeAway")
    gesture = {"frames" : 
        [{
            "time" : [0.33],
            "persist" : True,
            "params": {
                "NECK_PAN"  : randint(-4,4),
                "NECK_TILT" : randint(-4,4),
                "NECK_ROLL" : randint(-4,4),
            }
        }],

    "class": "furhatos.gestures.Gesture"
    }
    furhat.gesture(body=gesture, blocking=True)

def LOOK_BACK(speed):
    return {
    "frames": [
        {
            "time": [
                0.33 / speed
            ],
            "persist": True,
            "params": {
                'LOOK_DOWN' : 0,
                'LOOK_UP' : 0,
                'NECK_TILT' : 0
            }
        }, {
            "time": [
                0.67 / speed
            ],
            "params": {
                "NECK_PAN": 0,
                'LOOK_DOWN' : 0,
                'LOOK_UP' : 0,
                'NECK_TILT' : 0
            }
        }
    ],
    "class": "furhatos.gestures.Gesture"
    }

# DO NOT CHANGE
def LOOK_DOWN(speed=1):
    return {
    "frames": [
        {
            "time": [
                0.33 / speed
            ],
            "persist": True,
            "params": {
#                'LOOK_DOWN' : 1.0
            }
        }, {
            "time": [
                1 / speed
            ],
            "persist": True,
            "params": {
                "NECK_TILT": 20
            }
        }
    ],
    "class": "furhatos.gestures.Gesture"
    }


def FACE_DONT_CARE(speed = 1):
    return {
        "frames": [
            {
            "time": [
                0.17 / speed, 1.0 / speed, 3.0 / speed
            ],
            "params": {
                "NECK_ROLL": 25.0,
                "NECK_PAN": -12.0,
                "NECK_TILT": -25.0
            }
            }
        ],
        "name": "Don't care",
        "class": "furhatos.gestures.Gesture"
    }

def FACE_LEFT_WINK(speed = 1):
    return{
        "frames": [
            {
                "time": [
                    0.5 / speed
                ],
                "persist": True,
                "params": {
                    "BLINK_LEFT": 1.0
                }
            }, {
                "time": [
                    0.67
                ],
                "params": {
                    "reset": True
                }
            }
        ],
        "name": "left wink",
        "class": "furhatos.gestures.Gesture"
    }
        
def FACE_SMILE(speed = 1):
    return {
        "frames":[
            {
                "time":[0.32,0.64],
                "persist":False,
                "params":{
                    "BROW_UP_LEFT":1,
                    "BROW_UP_RIGHT":1,
                    "SMILE_OPEN":0.4,
                    "SMILE_CLOSED":0.7
                    }
            },
            {
                "time":[0.96],
                "persist":False,
                "params":{
                    "reset":True
                    }
            }
        ],
        "name":"Smile",
        "class":"furhatos.gestures.Gesture"
    }
# Say with blocking (blocking say, bsay for short)
def saySth(line):
    furhat.say(text=line, blocking=True)
    idle_animation()
    
def sayJoke(jokeNumber):
    saySth(JOKESET.pop(jokeNumber))

    idle_animation()
    sleep(2)
    saySth(JOKEANSWERSET.pop(jokeNumber))

def awaken():
    furhat.gesture(name="CloseEyes")
    furhat.gesture(body=LOOK_DOWN(speed=1), blocking=True)
    sleep(0.3)

def initialization():
    furhat.set_face(character='Titan', mask="adult")
    furhat.set_voice(name='Gregory-Neural')
    awaken()
    sleep(0.3)
    furhat.gesture(body=LOOK_DOWN(speed=1), blocking=True)
    sleep(1)
    furhat.gesture(body=LOOK_BACK(speed=1), blocking=True)

def getResponse():
    result = furhat.listen()
    return result.message, result.success

def checkYesOrNo(checkStr, input) ->bool:
    result = input.find(checkStr)

    return False if (result == -1) else True

def askComment():
    saySth("Is this joke funny?")
    answer, isSuccess = getResponse()
    if isSuccess and checkYesOrNo('yes', answer):
        furhat.gesture(body=FACE_SMILE(speed=1), blocking=True)
        saySth("I knew you would like it. Let me tell you another joke")
    elif isSuccess and checkYesOrNo('no', answer):
        saySth("Not funny, I can tell you a better one")
    else:
        saySth("How about this joke!")


def NotFunnyJokeRobot():
    initialization()
    saySth("Hey you! Are you watching me? You can come closer. I'm a Robot.")
    saySth("Let me tell a joke to you.")
    idle_animation()
    sleep(0.8)

    sayJoke(random.randint(0, len(JOKESET)-1))

    askComment()

    sayJoke(random.randint(0, len(JOKESET)-1))

    saySth(LAUGHINGSET[random.randint(0, len(LAUGHINGSET)-1)])
    idle_animation()
    sleep(0.8)
    furhat.gesture(body=FACE_LEFT_WINK(speed=1), blocking=True)
    furhat.gesture(body=LOOK_BACK(speed=1), blocking=True)
    saySth("Anyway...I got to go, see you next time. Bye")
    furhat.gesture(body=FACE_DONT_CARE(speed=1), blocking=True)
    saySth("P.S. I'm pretenting I'm fading away...")
    furhat.gesture(body=FACE_DONT_CARE(speed=1), blocking=True)



if __name__ == '__main__':
    NotFunnyJokeRobot()
