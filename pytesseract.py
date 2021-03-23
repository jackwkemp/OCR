import cv2
import pytesseract

img = cv2.imread("your_image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))

# Detecting Numbers
hImg, wImg, _ = img.shape
custom_config = r'--oem 3 --psm 6'
boxes = pytesseract.image_to_data(img, config=custom_config)
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        # print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 2)
            cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
