from time import sleep
from furhat_remote_api import FurhatRemoteAPI
from numpy.random import randint





FURHAT_IP = "127.0.1.1"

furhat = FurhatRemoteAPI(FURHAT_IP)
furhat.set_led(red=255, green=255, blue=255)




def Face_Confused_about_Angry():
    return {
        "name":"Face_Confused_about_Angry",
        "frames":[
            {
            "time":[0.32,0.64],
            "persist":False,
            "params":{
                "EXPR_FEAR":1,
                "BROW_UP_RIGHT": 0.5,
                "BROW_UP_LEFT": 0.5,
                "BLINK_LEFT": 0.0,
                "BLINK_RIGHT": 0.0,
                }
            },
            {
            "time":[0.96],
            "persist":False,
            "params":{
                "reset":True
                }
            }],
        "class":"furhatos.gestures.Gesture"
    }


def FACE_ANGER():
        return {
        "name":"Face_Confused_about_Angry",
        "frames":[
            {
            "time":[0.32,0.64],
            "persist":False,
            "params":{
                "EXPR_ANGER":1,
                "BROW_UP_RIGHT": 0.5,
                "BROW_UP_LEFT": 0.5,
                "BLINK_LEFT": 0.0,
                "BLINK_RIGHT": 0.0,
                }
            },
            {
            "time":[0.96],
            "persist":False,
            "params":{
                "reset":True
                }
            }],
        "class":"furhatos.gestures.Gesture"
    }




def apparenceTest():
    furhat.gesture(body=FACE_ANGER())





if __name__ == '__main__':
    furhat.say(text="Start")
    apparenceTest()
    furhat.say(text="End")

    






# def FACE_ANGER(speed = 1):
#     return {
#         "name":"BigSmile",
#         "frames":[
#             {
#             "time":[0.64,1.28],
#             "persist":False,
#             "params":{
#                     "EXPR_ANGER":1,
#                 }
#             },
#             {
#             "time":[2],
#             "persist":False,
#             "params":{
#                 "reset":True
#                 }
#             }],
#         "class":"furhatos.gestures.Gesture"
#     }



# def FACE_Nertral(speed = 1):
#     return {
#         "frames":[
#             {
#                 "time":1,
#                 "persist":True,
#                 "params":{
#                     "reset": 1
#                     }
#             }
#         ],
#         "class":"furhatos.gestures.Gesture"
#     }



# furhat.gesture(body={
#     "frames": [
#         {
#             "time": [
#                 0.33
#             ],
#             "params": {
#                 "BLINK_LEFT": 1.0
#             }
#         },
#         {
#             "time": [
#                 0.67
#             ],
#             "params": {
#                 "reset": True
#             }
#         }
#     ],
#     "class": "furhatos.gestures.Gesture"
#     })


# def FACE_SMILE():
#     return {
#         "name":"BigSmile",
#         "frames":[
#             {
#             "time":[0.32,0.64],
#             "persist":False,
#             "params":{
#                     "EXPR_ANGER":1,
#                 }
#             },
#             {
#             "time":[0.96],
#             "persist":False,
#             "params":{
#                 "reset":True
#                 }
#             }],
#         "class":"furhatos.gestures.Gesture"
#     }

# def FACE_TEST():
#     return {
#         "name":"BigSmile",
#         "frames":[
#             {
#             "time":[0.32,0.64],
#             "persist":False,
#             "params":{
#                 "BROW_UP_RIGHT": 0.5,
#                 "BROW_UP_LEFT": 0.5,
#                 "BLINK_LEFT": 0.0,
#                 "BLINK_RIGHT": 0.0,
#                 "SURPRISE": 0.0,
#                 "SMILE_OPEN": 1.0,
#                 "NECK_TILT": 0.0,
#                 "NECK_ROLL": -4.0,
#                 "NECK_PAN": 0.0
#                 }
#             },
#             {
#             "time":[0.96],
#             "persist":False,
#             "params":{
#                 "reset":True
#                 }
#             }],
#         "class":"furhatos.gestures.Gesture"
#     }
