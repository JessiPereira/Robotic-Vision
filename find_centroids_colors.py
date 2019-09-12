#!/usr/bin/python
from __future__ import print_function
from centroid_color import CentroidColor
import cv2 as cv
import json


variavel = open("dadosl.txt")
lines = variavel.readlines()
string = lines[0].strip()
biblio = json.loads(string)
color1 = CentroidColor(biblio["color1"])
color2 = CentroidColor(biblio["color2"])
color3 = CentroidColor(biblio["color3"])
window = 'Color Detection'
cv.namedWindow(window)

cap = cv.VideoCapture(0)
while True:
    ref, frame = cap.read()
    if frame is None:
        break
    #ref, frame2 = cap.read()
    #if frame2 is None:
    #    break
    #ref, frame3 = cap.read()
    #if frame3 is None:
    #    break
    cX1, cY1 = color1.get_centroid(frame)
    frame_threshold1 = color1.get_frame_threshold(frame)
    cX2, cY2 = color2.get_centroid(frame)
    frame_threshold2 = color2.get_frame_threshold(frame)
    cX3, cY3 = color3.get_centroid(frame)
    frame_threshold3 = color3.get_frame_threshold(frame)

    frame1 = cv.addWeighted(frame_threshold1, 1.0, frame_threshold1, 0.0, 0)
    frame2 = cv.addWeighted(frame_threshold2, 1.0, frame1, 1.0, 0)
    frame3 = cv.addWeighted(frame_threshold3, 1.0, frame2, 1.0, 0)

    def centroidhsv(cX, cY, threshold):
        cv.circle(threshold, (cX, cY), 5, (0, 0, 255), -1)
        cv.putText(threshold, "centroid", (cX - 25, cY - 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    if(cX1 is not None and cY1 is not None):
        centroidhsv(cX1, cY1, frame3)

        #cv.circle(frame_threshold1, (cX1, cY1), 5, (0, 0, 255), -1)
        #cv.putText(frame_threshold1, "centroid", (cX1 - 25, cY1 - 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        #cv.imshow(window, frame_threshold1)

        #key = cv.waitKey(30)
        #key == ord('q') or key == 27:

    if(cX2 is not None and cY2 is not None):
        centroidhsv(cX2, cY2, frame3)

        #cv.circle(frame_threshold2, (cX2, cY2), 5, (0, 0, 255), -1)
        #cv.putText(frame_threshold2, "centroid", (cX2 - 25, cY2 - 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        #cv.imshow(window, frame_threshold2)

        #key = cv.waitKey(30)
        #key == ord('q') or key == 27:

    if(cX3 is not None and cY3 is not None):
        centroidhsv(cX3, cY3, frame3)

        #cv.circle(frame_threshold3, (cX3, cY3), 5, (0, 255, 255), -1)
        #cv.putText(frame_threshold3, "centroid", (cX3 - 25, cY3 - 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        #cv.imshow(window, frame_threshold3)

        cv.imshow(window, frame3)
        key = cv.waitKey(30)
        key == ord('q') or key == 27
