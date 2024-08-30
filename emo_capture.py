import cv2
from feat.data import Fex
from feat import Detector
from feat.utils import FEAT_EMOTION_COLUMNS
import pandas as pd
import time
import os
import winsound


## Sorry I can find our neural network code on github, so this function is temporarily empty
def Neural_Network_Emo_Prediction(ActionUnits):
    prediction=""
    return prediction


## Since now we call the pyfeat and cv2 library in this function, it need to take more time to activate. 
## If we activate this two library in the furhat code begining, it might spend less time to fetch emotion.
def emo_capture():
    predicted_emo=''
    detector = Detector(device="cuda")  
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_BUFFERSIZE,10)

    count = 0
    
    strat_ =time.time()
    ret, frame = cap.read()

    if not ret:
        print("OpenCV found an error reading the next frame.")
    else:
        
        # Sound notification: catch your face AUs after the sound. 
        winsound.Beep(1500, 300) #Could delete this if no need

        cv2.imwrite(str(count)+'.jpg', frame)

        prediction_info = detector.detect_image(str(count)+'.jpg')
        AUs_info = prediction_info.aus
        Emo_info = prediction_info.emotions
        strongest_emotion = Emo_info.idxmax(axis=1)
        strongest_emotion.to_frame(name='Emotion')

        # output = pd.concat([strongest_emotion, AUs_info], axis=1)

        ### Sorry I can find our neural network code on github, so this function is temporarily empty
        #===> predicted_emo = Neural_Network_Emo_Prediction(AUs_info)
        predicted_emo = strongest_emotion

        ## Test output
        # print(AUs_info)
        # print(output)
        # print(strongest_emotion)
        # print(time.time()-strat_)

        cap.release()
        os.remove(str(count)+'.jpg')
        return predicted_emo
    
    cap.release()

    return -1
    


# # test code
# print(emo_capture())
