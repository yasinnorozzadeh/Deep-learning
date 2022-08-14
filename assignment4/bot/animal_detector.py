import tensorflow
import cv2
import numpy as np
from tensorflow.keras import models

class Detector:
    def __init__(self, path_img):
        self.model = models.load_model("animals2.h5")
        self.width = self.height = 224

        img = cv2.imread(f"{path_img}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (self.width,self.height))
        img = img / 255.0
        img = img.reshape(1, self.width, self.height, 3)

        result = self.model.predict(img)
        self.pred = np.argmax(result)
        if self.pred == 0:
            self.pred_animal = "bird 🦜"
        if self.pred == 1:
            self.pred_animal = "rhino 🦏"
        if self.pred == 2:
            self.pred_animal = "snake 🐍"
        if self.pred == 3:
            self.pred_animal = "turtle 🐢"

        # return self.pred_animal



# x = Detector("botimage/4iYp8BTHUo7ksuSePVbZUn-1200-80.jpg")
# print(x)








# def pred(path_img):
#     model = models.load_model("animals2.h5")
#     width = height = 224
    
#     img = cv2.imread(f"{path_img}")
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = cv2.resize(img, (width, height))
#     img = img / 255.0
#     img = img.reshape(1, width, height, 3)

#     result = model.predict(img)
#     pred = np.argmax(result)
#     if pred == 0:
#         pred_animal = "bird 🦜"
#     if pred == 1:
#         pred_animal = "rhino 🦏"
#     if pred == 2:
#         pred_animal = "snake 🐍"
#     if pred == 3:
#         pred_animal = "turtle 🐢"

#     return pred_animal