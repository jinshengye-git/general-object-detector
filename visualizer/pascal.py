import cv2 as cv

def drawBoxes(image, probs, boxes, labels):
    """
    Draws bounding boxes for selected classes of the Pascal dataset.
    Classes are:
    * Bicycle   | Label 2
    * Bus       | Label 6
    * Car       | Label 7
    * Motorbike | Label 14
    * Person    | Label 15

    Box colours are:
    Motorized vehicles  | Blue
    Bicycles, person    | Red
    
    Args:
    image       - Opencv image object in RGB
    probs       - Confidences for the detections
    boxes       - Coordinates of the bounding boxes
    labels      - Torch tensor with label indices

    Returns:
    image       - Opencv image in BGR with bounding boxes
    """
    labelsMotor = [6, 7, 14]
    labelsPerson = [2, 15]

    colourMotor = (255, 0, 0)
    colourPerson = (0, 0, 255)
    colourOther = (255, 165, 0)

    for i in range(boxes.size(0)):
                # Filter for classes
                if (labels[i] in labelsMotor):
                    box = boxes[i, :]
                    cv.rectangle(image, (box[0], box[1]), (box[2], box[3]), colourPerson, 2)
                elif (labels[i] in labelsPerson):
                    box = boxes[i, :]
                    cv.rectangle(image, (box[0], box[1]), (box[2], box[3]), colourMotor, 2)
                else:
                    box = boxes[i, :]
                    cv.rectangle(image, (box[0], box[1]), (box[2], box[3]), colourOther, 2)
    
    # Convert colour channels back to BGR
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    return image