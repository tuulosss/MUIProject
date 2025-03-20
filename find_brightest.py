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
       # Threshold the blurred image to create a binary mask of bright regions
    _, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)

    # Find contours of the bright regions
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour by area
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)

        # Calculate the moments of the largest contour
        moments = cv2.moments(largest_contour)

        # Calculate the average point (centroid) of the largest contour
        if moments["m00"] != 0:
            avg_x = int(moments["m10"] / moments["m00"])
            avg_y = int(moments["m01"] / moments["m00"])
            maxLoc = (avg_x, avg_y)
            
    #HIGHEST VALUE OF THE IMAGE. BY ADJUSTING, CHANGES THE THRESHOLD OF THE FLASHLIGHT VALUE
    if maxVal > 230:
        cv2.circle(frame, maxLoc, 5, (100, 255, 0), 2)
        point = maxLoc
        return point
    else:
        return None
