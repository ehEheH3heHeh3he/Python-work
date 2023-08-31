import numpy as np
from PIL import Image
import os
import cv2

def train_classifier(data_dir):
    path = [os.path.join(data_dir,f) for f in os.listdir(data_dir)]
    faces = []
    ids = []
    for image in path:
        if image == 'data/.DS_Store':
            continue
        img = Image.open(image).convert("L")
        imageNp = np.array(img,'uint8')
        id = int(os.path.split(image)[1].split(".")[1])
        faces.append(imageNp)
        ids.append(id)
        print(type(ids))
    ids = np.array(ids)
    clf = cv2.face.LBPHFaceRecognizer_create()
    print(clf)
    clf.train(faces,ids)
    clf.write("classifier.xml")

train_classifier("data")