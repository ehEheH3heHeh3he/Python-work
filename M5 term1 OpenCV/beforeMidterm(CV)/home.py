import cv2

line_start = None
line_end = None

def draw_line(event, x, y, flags, param):
    global line_start, line_end

    if event == cv2.EVENT_LBUTTONDOWN:
        line_start = (x, y)
    
    elif event == cv2.EVENT_LBUTTONUP:
        line_end = (x, y)
        cv2.line(image, line_start, line_end, (0, 0, 255), 2)
        cv2.imshow("Image", image)

image = cv2.imread('nig.png')

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_line)

while True:
    cv2.imshow("Image", image)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cv2.destroyAllWindows()