# Taylor Tam 6/10
# non-slide area detection
# filter out blurry images first

import cv2
import numpy as np


class ContourDetection:
    def __init__(self, path, min_percent=75.0):
        self.path = path
        self.minPercent = min_percent

    # determines the percent that the contour occupies given contour-area and image
    def percent(self, contour_area, image):
        height, width, channel = image.shape
        image_area = height * width
        return (contour_area / image_area) * 100

    def contoured_area(self, display_output):
        image = cv2.imread(self.path)

        # to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # kernel to sharpen the image
        kernel1 = np.array([[0, -1, 0],
                            [-1, 5, -1],
                            [0, -1, 0]])
        image_sharp = cv2.filter2D(src=gray, ddepth=-1, kernel=kernel1)

        # convert to a binary image, using Gaussian adaptive threshold
        thresh = cv2.adaptiveThreshold(image_sharp, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)
        new_image = thresh

        # find contours
        contours, hierarchy = cv2.findContours(image=new_image, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

        # filter contours by open/closed
        use_contours = []
        for i in range(len(contours)):
            opened = hierarchy[0][i][2] < 0 and hierarchy[0][i][3] < 0
            if opened:
                use_contours.append(contours[i])

        # Erase small contours, and contours which small aspect ratio (close to a square)
        for c in use_contours:
            area = cv2.contourArea(c)
            # Erase small contours base don area
            if area < 20:
                cv2.fillPoly(new_image, pts=[c], color=0)
                continue
            rect = cv2.minAreaRect(c)
            (x, y), (w, h), angle = rect
            aRatio = max(w, h) / min(w, h)

            # Assume line must be long and narrow
            if (aRatio < 1.5):
                cv2.fillPoly(new_image, pts=[c], color=0)
                continue

        new_image = cv2.morphologyEx(new_image, cv2.MORPH_CLOSE,
                                     cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (51, 51)))
        # find contours again
        contours2, hierarchy2 = cv2.findContours(image=new_image, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

        # find the largest length contour (since this will be the most defined area)
        max_len = 0
        max_contour = None
        for i in range(len(contours2)):
            len_contour = cv2.arcLength(contours2[i], False)
            if len_contour > max_len:
                max_len = len_contour
                max_contour = contours2[i]

        # only draw the MOST defined, long contour
        # this contour is drawn on a copy of the image (img_copy) and then the original image is just image
        img_copy = image.copy()

        cv2.drawContours(img_copy, max_contour, -1, (0, 0, 255), 3)

        if display_output:
            cv2.imshow("Contours", img_copy)
            cv2.imshow("Original", image)
            cv2.waitKey(0)

        # find area of contour
        contour_area = cv2.contourArea(max_contour)

        # return if the percent of the contoured area is acceptable (above threshold) or not
        return self.percent(contour_area, image) > self.minPercent
