# Ref:https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/
# import the necessary packages
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
from numpy import NaN
import matplotlib.pyplot as plt
print('Length Width\n')
def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
def CrackLen(ImagePath):
    image = cv2.imread(ImagePath)
    width = float(2)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv2.Canny(gray, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    # find contours in the edge map
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # sort the contours from left-to-right and initialize the
    # 'pixels per metric' calibration variable
    (cnts, _) = contours.sort_contours(cnts)
    pixelsPerMetric = None

    # loop over the contours individually
    for c in cnts:
        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 100:
            continue

        # compute the rotated bounding box of the contour
        orig = image.copy()
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")

        # order the points in the contour such that they appear
        # in top-left, top-right, bottom-right, and bottom-left
        # order, then draw the outline of the rotated bounding
        # box
        box = perspective.order_points(box)
        cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

        # loop over the original points and draw them
        for (x, y) in box:
            cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

        # unpack the ordered bounding box, then compute the midpoint
        # between the top-left and top-right coordinates, followed by
        # the midpoint between bottom-left and bottom-right coordinates
        (tl, tr, br, bl) = box
        (tltrX, tltrY) = midpoint(tl, tr)
        (blbrX, blbrY) = midpoint(bl, br)

        # compute the midpoint between the top-left and top-right points,
        # followed by the midpoint between the top-righ and bottom-right
        (tlblX, tlblY) = midpoint(tl, bl)
        (trbrX, trbrY) = midpoint(tr, br)

        # draw the midpoints on the image
        cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

        # draw lines between the midpoints
        cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
                 (255, 0, 255), 2)
        cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
                 (255, 0, 255), 2)

        # compute the Euclidean distance between the midpoints
        dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
        dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

        # if the pixels per metric has not been initialized, then
        # compute it as the ratio of pixels to supplied metric
        # (in this case, inches)
        if pixelsPerMetric is None:
            pixelsPerMetric = dB / width

        # compute the size of the object
        dimA = round(dA / pixelsPerMetric,3)
        dimB = round(dB / pixelsPerMetric,3)
        cv2.putText(orig, "W = {:.1f}nm".format(dimA), (int(tltrX - 200), int(tltrY + 400)), cv2.FONT_HERSHEY_SIMPLEX, 2, (1, 160, 1), 6)
        cv2.putText(orig, "L = {:.1f}nm".format(dimB), (int(tltrX - 200), int(tltrY + 500)), cv2.FONT_HERSHEY_SIMPLEX, 2, (1, 160, 1), 6)
        np.set_printoptions(precision=3)
        if dimA != 0.2 and dimB != 2:
            return([dimB,dimA])
            #cv2.imshow("Image", orig)
#            plt.imsave('crack%s.png'%dimB,orig,dpi=300)
            plt.imshow(orig, interpolation='bicubic')
            plt.imsave('dimension.png',orig)

ImageDir = 'CrackImage/'
lw = np.zeros(shape=(10,2))
i = 0;
for frame in np.linspace(0,8,9):
    if(len(str(int(frame))))==1:
        frame = 'cra00'+'0'+str(int(frame))+'.png'
    else:
        frame = 'cra00'+str(int(frame))+'.png'
    ImagePath=ImageDir+frame
    u = CrackLen(ImagePath)
    lw[i,:]=np.nan_to_num(u)
    lw = np.nan_to_num(lw)
    i = i+1
    print(u)

plt.rcParams.update({'font.size': 16})
plt.plot(np.linspace(0,9,10),lw[:,0], marker='o',label='Length',color='firebrick')
plt.plot(np.linspace(0,9,10),lw[:,1], marker='s',label='Width',color='darkblue')
plt.xlabel('Frame')
plt.ylabel('Length / Width')
plt.legend(frameon=False)
plt.tight_layout()
plt.savefig('CrackLenSum.png')
np.savetxt('cracklength.txt',lw,fmt='%1.4e')
plt.show()
