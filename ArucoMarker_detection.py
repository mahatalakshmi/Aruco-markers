import cv2
from cv2 import aruco
import numpy as np


marker_dict= aruco.Dictionary_get(aruco.DICT_4X4_100)
parameter_marker=aruco.DetectorParameters_create()

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    marker_corners,marker_IDs,reject=aruco.detectMarkers(gray_frame,marker_dict,parameters=parameter_marker)
    if marker_corners:
        aruco.drawDetectedMarkers(frame,marker_corners)
        for ids,corners in zip(marker_IDs,marker_corners):
            cv2.polylines(frame,[corners.astype(np.int32)],True,(0,225,0),4,cv2.LINE_AA)
            
            corners=corners.reshape(4,2)
            corners=corners.astype(int)
            top_right = corners[0].ravel()
            cv2.putText(frame,f"id: {ids[0]}",top_right,cv2.FONT_HERSHEY_PLAIN,1.3,(0,0,225),2,cv2.LINE_AA)
    cv2.imshow("video",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
