import cv2

firstx = 0
firsty = 0
def find_brightest(frame):
    #Findin the brightest spot in "frame"

    #turn to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # perform a naive attempt to find the (x, y) coordinates of
    # the area of the image with the largest intensity value
    blur = cv2.blur(gray, (20,20))
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blur)
    cv2.circle(frame, maxLoc, 5, (255, 0, 0), 2)
    point = maxLoc
    
    return point

