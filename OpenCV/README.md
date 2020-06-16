# Auto Brightness on Face Detection
## Script to set screen brighntess to 90% if face is detected , if not , dim to 0%
- Works only on Windows
- Used OpenCV for face detection using haarcascades
- Used WMI python module for brightness control

To set your custom brightness change the parameters of:
```
 brightness=90
 ```
 to your desired value.


## code:

```
import cv2  # for face detection
import wmi  # to control brightness

# loading cascade
faceCascade= cv2.CascadeClassifier("C:/Users/Anuraag/Downloads/haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)

while True:
    cap, img = video_capture.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting from BGR to grayscale

    faces = faceCascade.detectMultiScale(
        img_gray,
        scaleFactor=1.1,
        minNeighbors=2,
        minSize=(30, 30)
    )
    # The detected objects are returned as a list of rectangles
    if(len(faces)>0):       #condition to check for detected face
            brightness = 90 # percentage [0-100]
            obj = wmi.WMI(namespace='wmi')
            methods = obj.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(brightness, 0)
    else:
        brightness = 0 # percentage [0-100]
        methods.WmiSetBrightness(brightness, 0)
        
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture 
# and set brightness to 50%
methods.WmiSetBrightness(50, 0)
video_capture.release()
cv2.destroyAllWindows()
```
