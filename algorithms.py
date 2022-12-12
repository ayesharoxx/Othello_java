#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import cv2

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dist_thresholding(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1 ,des2 ,k=1500)
    l = []
    for i in matches:
        l1 = []
        for j in i:
            if j.distance < threshold_value:
                l1.append(j)
              
        l.append(l1)
    return l


def nn(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1 ,des2 ,k=1)
    l = []
    for i in matches:
        l1 = []
        for j in i:
            if j.distance < threshold_value or threshold_value==-1:
                l1.append(j)
            else:
                l1.append([])
              
        l.append(l1[0])
    return l

def nndr(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1 ,des2 ,k=2)
    l = []
    for i in range(len(matches)):
        l1 = []
        if((matches[i][0].distance/matches[i][1].distance)<threshold_value):
            l1.append(matches[i][0])
        else:
            l1.append([])
        l.append(l1)


    return l

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
