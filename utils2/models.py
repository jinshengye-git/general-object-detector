import contextlib
import sys
import io

from ssd_pytorch.ssd import ssdModel as ssd
from detr.detr import detr_load as detr
from detr.detr import detr_predict
from detr.detr_panoptic import detr_panoptic_load as detr_panoptic
from detr.detr_panoptic import detr_panoptic_predict
from faster_rcnn.fasterrcnn import fasterRcnnModel as frcnn
from faster_rcnn.fasterrcnn import frcnn_predict
from yolo.yolo import yoloModel as yolo
from yolo.yolo import yolo_predict
from visualizer.pascal import drawBoxes as pascalBoxes
from visualizer.coco import draw_boxes as cocoBoxes

from detectron2.config import get_cfg

# For suppressing print output
class DummyFile(object):
    def write(self, x): pass

@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = DummyFile()
    yield
    sys.stdout = save_stdout


class DetectionModel:
    def __init__(self, model_type):
        if model_type:
            self.model_type = model_type
            self.predictor = None
            

    def load_model(self, model_type = None):
        if model_type:
            self.model_type = model_type

        if ((self.model_type == "-ssdm") or (self.model_type == "-ssdmlite")):
            _, self.predictor = ssd(self.model_type)
        elif (self.model_type == "-fasterrcnn"):
            self.predictor = frcnn()
        elif (self.model_type == "-detr"):
            self.predictor = detr()
        elif (self.model_type == "-yolov5s"):
            self.predictor = yolo()
        elif (self.model_type == "-detr-panoptic"):
            self.predictor, self.postprocessor = detr_panoptic()
        else:
            print("Unable to load model. Valid models include -ssdm, -ssdmlite, -fasterrcnn, -detr, and -yolov5s")


    def model_predict(self, image):
        
        if (self.model_type == "-ssdm" or self.model_type == "-ssdmlite"):
            boxes, labels, conf = self.predictor.predict(image, 10, 0.4)
            frame = pascalBoxes(image, conf, boxes, labels)
        elif (self.model_type == "-detr"):
            boxes, labels, conf = detr_predict(self.predictor, image)
            frame = cocoBoxes(image, boxes, labels, conf)
        elif (self.model_type == "-fasterrcnn"):
            boxes, labels, conf = frcnn_predict(self.predictor, image)
            frame = cocoBoxes(image, boxes, labels, conf)
        elif (self.model_type == "-yolov5s"):
            boxes, labels, conf = yolo_predict(self.predictor, image)
            frame = cocoBoxes(image, boxes, labels, conf)
        elif (self.model_type == "-detr-panoptic"):
            frame = detr_panoptic_predict(self.predictor, self.postprocessor, image)
            return frame, None, None, None
        else:
            raise Exception("Error: Model not loaded")
        
        return frame, boxes, labels, conf