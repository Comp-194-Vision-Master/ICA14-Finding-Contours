""" ==============================================================================================
File: activ14.py
Author: Susan Fox
Date: Fall 2025

Contains functions to practice with finding contours
==================================================================================================
"""

import cv2


# -----------------------------------------------------------------------------------------------------------
# Example of using inRange on video frames to match color



def findPink(whichSource=0):
    """Takes in either a number for a webcam or a string that is the path/filename for a video file,
    and it connects to the video source. It processes each frame of the video with processImage, and
    displays the result, until the user hits q to quit."""
    vidCap = cv2.VideoCapture(whichSource)

    while True:
        res, frame = vidCap.read()
        if not res:
            print("Video feed done")
            break

        newIm = thresholdPink(frame)
        cv2.imshow("Video Process", newIm)
        x = cv2.waitKey(10)
        if x > 0:
            if chr(x) == 'q':
                break

    vidCap.release()


# TODO: Modify the thresholdPink function below to select from the contours the one that is most likely to
# TODO: locate the ball


def thresholdPink(image):
    """Given an input image, it performs some transformation on it, and returns the resulting image.
    In its starting form, it does nothing but copy the original image and return it."""
    # Modify the low and high ranges for HSV values according to the color of the object you want to track
    pinkLow = (165, 100, 20)
    pinkHigh = (175, 255, 255)
    img2 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(img2, pinkLow, pinkHigh)
    cv2.imshow("Thresh", thresh)
    contrs, hier = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contrs, -1, (255, 255, 255), 2)
    return image



# -----------------------------------------------------------------------------------------------------------
# Finding coins or balls with thresholds and findContours

# TODO: Copy your threshold function(s) here (either operating on single images, or the video-stream one)
# TODO: Modify this to experiment with findContours to find contours in the thresholded image, and to
# TODO: select from the list of contours the ones that best identify ball or coin shapes


# -----------------------------------------------------------------------------------------------------------
# Detecting simple hand gestures

# TODO: (OPTIONAL!) Copy the video processing program above, and modify it so that it you identify your hand
# TODO: held up in front of a plain background (regular brightness thresholding might work here). Try to identify
# TODO: from the shape of the contour whether someone is making a fist, or holding up a flat hand, or holding up fingers




# ===========================================================================================================
# Main script

if __name__ == "__main__":
    # TODO: Put sample calls to your functions below this, along with reading in images, etc.
    # -----------------------------------------------------------------------------------------------------------
    # Example with inRange, video, and pink

    findPink(0)
