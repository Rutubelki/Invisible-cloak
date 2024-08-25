import cv2
import numpy as np
import time

video = cv2.VideoCapture(0)
time.sleep(3)

background = 0
for i in range(30):
    ret, background = video.read()
background = np.flip(background, axis=1)

while True:
    ret, img = video.read()
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv, (35, 35), 0)
    
    
    lower_orange = np.array([0,120,70])
    upper_orange = np.array([10, 255, 255])
    mask01 = cv2.inRange(hsv, lower_orange, upper_orange)
    
   
    lower_purple = np.array([170, 120, 70])  
    upper_purple = np.array([180, 255, 255])  
    mask02 = cv2.inRange(hsv, lower_purple, upper_purple)
    
   
    mask = mask01 + mask02
    
   
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    
   
    img[np.where(mask == 255)] = background[np.where(mask == 255)]
    
    cv2.imshow("Display", img)
    cv2.imshow("background", background)
    cv2.imshow("mask01", mask01)
    cv2.imshow("mask02", mask02)
    cv2.imshow("combined_mask", mask)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


# import cv2
# import numpy as np

# # HSV color for bright orange
# bright_orange_hsv = np.uint8([[[15, 255, 255]]])  # Adjust values if needed

# # Convert HSV to BGR
# bright_orange_bgr = cv2.cvtColor(bright_orange_hsv, cv2.COLOR_HSV2BGR)

# # Create a blank image and fill it with the bright orange color
# image = np.zeros((100, 300, 3), dtype=np.uint8)
# image[:] = bright_orange_bgr[0][0]

# # Display the color
# cv2.imshow("Bright Orange Color", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




