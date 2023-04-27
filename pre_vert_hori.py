import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR'

def sana():
    # Load in image, convert to grayscale, and threshold
    image = cv2.imread('pngImgs/t13.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # Find and remove horizontal lines
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (35, 2))
    detect_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    cnts = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(thresh, [c], -1, (0, 0, 0), 3)

    # Find and remove vertical lines
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 35))
    detect_vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
    cnts = cv2.findContours(detect_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(thresh, [c], -1, (0, 0, 0), 3)

    # Mask out unwanted areas for result
    result = cv2.bitwise_and(image, image, mask=thresh)
    result[thresh == 0] = (255, 255, 255)

    cv2.imshow('thresh', thresh)
    cv2.imshow('result', result)
    cv2.waitKey()
# import cv2
#
# # Load the image
# img = cv2.imread('pngImgs/t13.png')
#
# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Threshold the image
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
#
# # Apply morphological erosion to remove small artifacts
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# eroded = cv2.erode(thresh, kernel, iterations=1)
#
# # Apply morphological dilation to expand the characters
# dilated = cv2.dilate(eroded, kernel, iterations=5)
#
# # Find contours in the image
# contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Iterate through each contour and extract the bounding box
# for contour in contours:
#     (x, y, w, h) = cv2.boundingRect(contour)
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
# # Display the result
# cv2.imshow('Result', img)
# cv2.waitKey(0)