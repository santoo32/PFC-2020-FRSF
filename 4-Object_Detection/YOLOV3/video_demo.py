# OpenCV: Image processing
import cv2
import time
import popupWindow as detectionWindow
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread

# numpy: numerical computation
import numpy as np
import core.utils as utils
# Tensorflow: deep learning
import tensorflow as tf
# Allow for GPU memory growth to prevent "Out of memory" errors
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
  except RuntimeError as e:
    print(e)

# YOLOV3 itself
from core.yolov3 import YOLOv3, decode
    

def startDetection(window, minConfidence, videoPath):
    video_path = videoPath

    # Number of classes, one class for each element
    num_classes     = 80
    input_size      = 704
    min_confidence = minConfidence / 100
    
    # Layer to be used as an entry point into a Network (a graph of layers).
    # Tuple with height, width and depth used to reshape arrays.
    # This is used for reshaping in Keras.
    input_layer  = tf.keras.layers.Input([input_size, input_size, 3])

    # (TO DO: see how it does it)
    feature_maps = YOLOv3(input_layer)

    bbox_tensors = []

    for i, fm in enumerate(feature_maps):
        bbox_tensor = decode(fm, i)
        bbox_tensors.append(bbox_tensor)

    # Model groups layers into an object with training and inference features.
    # input: input_layer
    # output: bbox_tensors
    model = tf.keras.Model(input_layer, bbox_tensors)

    # load weights from file
    utils.load_weights(model, "./data/weights/handgun.weights")


    # Prints a string summary of the network.
    # model.summary()

    # Load video from file with openCV
    vid = cv2.VideoCapture(video_path)

    runFlag = True
    while runFlag:
        # Get a frame from the video
        # Returns a bool (True/False).
        # If frame is read correctly, it will be True. 
        # So you can check end of the video by checking this return value.
        return_value, frame = vid.read()
        if not return_value:
            raise ValueError("No image!")

        # thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
        # print(thistuple[:2]) => ('apple', 'banana')
        # shape holds heigth, width and number of channels
        # Gets width and height of the frame
        frame_size = frame.shape[:2]

        # np.copy(frame) => Return an array copy of the given object.
        # Resizes frame to network input size => def image_preporcess(image, target_size, gt_boxes=None):
        image_data = utils.image_preporcess(np.copy(frame), [input_size, input_size])

        image_data = image_data[np.newaxis, ...].astype(np.float32)

        # Performs the prediction on the frame (TO DO: see how it does it)
        pred_bbox = model.predict_on_batch(image_data)

        # Changes tensor shape, similar to transposing a matrix
        # href: https://www.tensorflow.org/api_docs/python/tf/reshape
        pred_bbox = [tf.reshape(x, (-1, tf.shape(x)[-1])) for x in pred_bbox]
        # Concatenates tensors along one dimension axis = 0 => axis = y
        pred_bbox = tf.concat(pred_bbox, axis=0)

        # (TO DO: see how it does it)
        bboxes = utils.postprocess_boxes(pred_bbox, frame_size, input_size, min_confidence)
         # (TO DO: see how it does it)
        bboxes = utils.nms(bboxes, 0.45, method='nms')

        # Draws boundingbox in image
        # (TO DO: see how it does it)
        image = utils.draw_bbox(frame, bboxes)
    
        window.imageDisplay.setPixmap(QtGui.QPixmap(utils.convert_cv_qt(image.image)))
        
        # HERE check if detected class is handgun
        if(image.classDetected == 'giraffe'):
            #cv2.destroyAllWindows()
            #window.label_4.setText("Handgun detected")
            #return "Alert"
            #break
            callPopUpWindow(window, image.image)

        # Breaks while loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            cv2.destroyAllWindows()
            break


def callPopUpWindow(self, detection):
        dialog = detectionWindow.DetectionWindow(self)
        dialog.setImage(detection)
        dialog.show()
