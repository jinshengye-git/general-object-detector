"""
Displays symbols

"""
import cv2 as cv


def load():
    """
    Loads the signs as opencv images

    Returns:
    signs   - List of signs [stopsign]
    """
    signs = []
    signs.append(cv.imread('resources/stop.png', -1))
    
    return signs


def showStopSign(frame, stop_sign, labels, conf):
    """
    Args:
    frame   - Opencv frame object
    labels  - List with predicted labels
    conf    - List with confidences of each prediction
    
    Returns:
    frame   - Frame with stopsign displayed if sign is detected
    """
    stop_sign_label = 7 # Use class car for test

    if (stop_sign_label in labels):
        # Show stop sign symbol

        # Calculate top centre position to place stop sign
        x_offset = int(frame.shape[1] / 2) - int(stop_sign.shape[1] / 2)
        y_offset = 20
        y1, y2 = y_offset, y_offset + stop_sign.shape[0]
        x1, x2 = x_offset, x_offset + stop_sign.shape[1]

        # Extract alpha channel for transparency
        alpha_s = stop_sign[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s

        # Add stop sign to frame
        for c in range(0, 3):
            frame[y1:y2, x1:x2, c] = (alpha_s * stop_sign[:, :, c] +
                                alpha_l * frame[y1:y2, x1:x2, c])

    return frame