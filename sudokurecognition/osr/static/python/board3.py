import cv2
import numpy as np

def border(image):
    height, width, channels = image.shape
    if height > width:
        relation = 1000 / height
        height = 1000
        width = int(round(width * relation))
    else:
        relation = 1000 / width
        height = int(round(height * relation))
        width = 1000
    im_scaled = cv2.resize(image, (width, height))

    im_gray = cv2.cvtColor(im_scaled, cv2.COLOR_BGR2GRAY)
    im_gaussian = cv2.medianBlur(im_gray,5)
    th3 = cv2.adaptiveThreshold(im_gaussian,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
              cv2.THRESH_BINARY,11,2)
    im_bw = np.copy(th3)
    contours,hierarchy = cv2.findContours(th3,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # ************************************************************************
    # ************************* BUSQUEDA BORDE DEL BOARD *********************
    #*************************************************************************
    b = []
    [x,y,w,h] = [0,0,0,0]
    a = w * h
    for cnt in contours:
        [x,y,w,h] = cv2.boundingRect(cnt)
        if abs(height - h) > 10 and abs(width - w) > 10:
            if b == []:
                b = cnt
            else:
                if a < w * h:
                    b = cnt
                    a = w * h

    if b != []:
        cv2.drawContours(im_scaled,[b],0,(0,255,255),2)
    return im_scaled

if __name__ == "__main__":
    image = cv2.imread("examples/1.jpg")
    cv2.imwrite("board_border.jpg", border(image))
