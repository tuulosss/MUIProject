import cv2

firstx = 0
firsty = 0
def find_brightest(frame):

    #Finding the brightest spot in "frame"
    #turn to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    object_detect = cv2.createBackgroundSubtractorMOG2()
    mask = object_detect.apply(frame)

    # perform a naive attempt to find the (x, y) coordinates of
    # the area of the image with the largest intensity value
    blur = cv2.blur(gray, (20,20))
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blur)
    
    #HIGHEST VALUE OF THE IMAGE. BY ADJUSTING, CHANGES THE THRESHOLD OF THE FLASHLIGHT VALUE
    if maxVal > 225:
        cv2.circle(frame, maxLoc, 5, (100, 255, 0), 2)
        point = maxLoc
        return point
    
