import cv2 as cv
from cv2 import aruco
import numpy as np

calib_data_path = "../calib_data/MultiMatrix.npz"

calib_data = np.load(calib_data_path)
print(calib_data.files)
with open('../calib_data/MultiMatrix.npz','rb') as f:
    camera_matrix=np.load(f)
    camera_distortion=np.load(f)
cam_mat = calib_data["camMatrix"]
dist_coef = calib_data["distCoef"]
r_vectors = calib_data["rVector"]
t_vectors = calib_data["tVector"]

MARKER_SIZE = 8  # centimeters

marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)

param_markers = aruco.DetectorParameters_create()

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(
        gray_frame, marker_dict, parameters=param_markers
    )
    if marker_corners:
        rVec, tVec, _ = aruco.estimatePoseSingleMarkers(marker_corners, MARKER_SIZE, cam_mat, dist_coef)
        total_markers = range(0, marker_IDs.size)
        for ids, corners, i in zip(marker_IDs, marker_corners, total_markers):
            cv.polylines(frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv.LINE_AA)
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            bottom_right = corners[2].ravel()
            #pose
            point = cv.drawFrameAxes(frame, cam_mat, dist_coef, rVec[i], tVec[i], 4, 4)
            cv.putText(frame,f"id: {ids[0]}",top_right,cv.FONT_HERSHEY_PLAIN,1.3,(0, 0, 255),2,cv.LINE_AA,)
            cv.putText(frame, f"x:{round(tVec[i][0][0],1)} y: {round(tVec[i][0][1],1)} ", bottom_right,cv.FONT_HERSHEY_PLAIN,1.0,(0, 0, 255),2,cv.LINE_AA,)
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv.destroyAllWindows()
