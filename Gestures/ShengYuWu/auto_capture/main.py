from time import sleep
from furhat_remote_api import FurhatRemoteAPI
from numpy.random import randint
import json


FURHAT_IP = "127.0.1.1"

furhat = FurhatRemoteAPI(FURHAT_IP)
furhat.set_led(red=255, green=255, blue=255)




def apparenceTest(gestureBodySetting):
    furhat.gesture(body=gestureBodySetting)





if __name__ == '__main__':
    f = open('Stare.json', 'r')
    gestureSetting = json.load(f)

    print(gestureSetting)

    furhat.say(text="Start")
    apparenceTest(gestureSetting)
    

    f.close()
    


