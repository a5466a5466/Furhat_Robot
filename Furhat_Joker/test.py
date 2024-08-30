from time import sleep
from furhat_remote_api import FurhatRemoteAPI
from numpy.random import randint
import random
# the functions, idle_animation(), LOOK_BACK(speed), LOOK_DOWN(speed=1) are used from Lab3 demo code

FURHAT_IP = "127.0.1.1"

furhat = FurhatRemoteAPI(FURHAT_IP)
furhat.set_led(red=255, green=255, blue=255)

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
                1 / speed
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

def awaken():
    furhat.gesture(name="CloseEyes")
    furhat.gesture(body=LOOK_DOWN(speed=1), blocking=True)
    sleep(0.3)

def initialization():
    furhat.set_face(character='Titan', mask="adult")
    furhat.set_voice(name='Gregory')
    furhat.gesture(body=LOOK_DOWN(speed=1), blocking=True)
    furhat.gesture(body=LOOK_BACK(speed=1), blocking=True)

def listen():
    result = furhat.listen()
    return result


def checkYesOrNo(checkStr, input) ->bool:
    result = input.find(checkStr)


    return   False if (result == -1) else True
    


def getResponse():
    result = furhat.listen()
    print(result.message)
    # return result['message'], result['success']


if __name__ == '__main__':

    getResponse()


    # print(checkYesOrNo("Yes", " I doYesn't know  "))