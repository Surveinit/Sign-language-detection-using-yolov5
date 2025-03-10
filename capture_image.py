import os
import cv2
import time
import uuid

IMAGE_PATH = 'Collected_Images'

labels = ['Ask', 'Bathroom', 'Dad', 'Drink', 'Eat', 'Goodbye', 'Hello', 'Help', 'I Love You', 'Me', 'Mom', 'Need',
          'No', 'Please', 'Sorry', 'Thank you', 'Water', 'Yes']


number_of_images = 20

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    try:
        os.makedirs(img_path)
    except FileExistsError:
        pass
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)


    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        image_name = os.path.join(IMAGE_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(image_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()