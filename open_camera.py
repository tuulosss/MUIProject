import cv2
def open_camera():
    # Open the default camera
    cam = cv2.VideoCapture(0)

    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(frame_width, frame_height)

    while True:
        ret, frame = cam.read()

        # Display the captured frame
        cv2.imshow('Camera', cv2.flip(frame,1))
        # Press 'q' to exit the loop

        if cv2.waitKey(1) == ord('q'):
            break
        
    # Release the capture and writer objects
    cam.release()
    cv2.destroyAllWindows()

