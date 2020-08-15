# OpenCV: Image processing
import cv2
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
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
    utils.load_weights(model, "./data/weights/yolov3.weights")


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
        if return_value:
            # cv2.cvtColor() method is used to convert an image from one color space to another.
            # RGB stands for Red Green Blue. Most often, an RGB color is stored in a structure or unsigned integer with Blue occupying the least significant "area" (a byte in 32-bit and 24-bit formats), 
            #   Green the second least, 
            #   and Red the third least.
            # BGR is the same, except the order of areas is reversed. Red occupies the least significant area, Green the second (still), and Blue the third.
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        else:
            # Video ended
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

        # prev_time and curr_time are used for ms display
        # prev_time = time.time()
        # Performs the prediction on the frame (TO DO: see how it does it)
        pred_bbox = model.predict_on_batch(image_data)
        # curr_time = time.time()
        # exec_time = curr_time - prev_time


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

        result = np.asarray(image.image)

        # info = "time: %.2f ms" %(1000*exec_time)
        info = ""

        cv2.putText(
            result, 
            text=info, 
            org=(50, 70), 
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1, 
            color=(255, 0, 0), 
            thickness=1)

        cv2.namedWindow("result", cv2.WINDOW_AUTOSIZE)
        result = cv2.cvtColor(image.image, cv2.COLOR_RGB2BGR)
        
        print("Detected: ", image.classDetected)
        
        cv2.imshow("result", result) 
        # window.label_2.setPixmap(QtGui.QPixmap(Image.fromarray(result, 'RGB')))
        if(image.classDetected == 'handgun'):
            cv2.destroyAllWindows()
            window.label_4.setText("Handgun detected")
            return "Alert"
            break
        # Breaks while loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            cv2.destroyAllWindows()
            break





