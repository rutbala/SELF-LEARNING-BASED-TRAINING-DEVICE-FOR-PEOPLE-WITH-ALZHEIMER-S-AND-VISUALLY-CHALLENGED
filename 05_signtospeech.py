import cv2
import numpy as np
from Models.audio import say
import time
def nothing(x):
    pass

image_x, image_y = 64,64

from keras.models import load_model
classifier = load_model('Models/Trained_model.h5')


def predictor():
       import numpy as np
       from tensorflow.keras.preprocessing import image
       test_image = image.load_img('Models/1.png', target_size=(64, 64))
       test_image = image.img_to_array(test_image)
       test_image = np.expand_dims(test_image, axis = 0)
       result = classifier.predict(test_image)
       
       if result[0][0] == 1:
              return 'None'
       elif result[0][1] == 1:
              return 'Hello'
       elif result[0][2] == 1:
              return 'help'
       elif result[0][3] == 1:
              return 'how are you'
       elif result[0][4]== 1:
              return 'Get me up'
       elif result[0][5]== 1:
              return 'sorry'
       elif result[0][6]== 1:
              return 'i am sleepy'


cam = cv2.VideoCapture(0)

img_counter = 0

img_text = ''
found = set()

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)

    l_h=0
    l_s =70
    l_v=0
    u_h = 179
    u_s = 255
    u_v = 255

    img = cv2.rectangle(frame, (425,100),(625,300), (0,255,0), thickness=2, lineType=8, shift=0)

    lower_hsv = np.array([l_h, l_s, l_v])
    upper_hsv = np.array([u_h, u_s, u_v])
    imcrop = img[102:298, 427:623]

    hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    


    img_name = "Models/1.png"
    save_img = cv2.resize(mask, (image_x, image_y))
    cv2.imwrite(img_name, save_img)
    img_text = predictor()
    print(img_text)
    cv2.putText(frame, img_text, (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
    cv2.imshow("Sign to Speech", frame)
    cv2.imshow("mask", mask)
    if(str(img_text) != 'None'):
        if str(img_text) not in found :
            #say(str(img_text))
            found.add(str(img_text))
            #time.sleep(2)
    else:
        found.clear()

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
