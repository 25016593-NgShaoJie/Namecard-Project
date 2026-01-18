import cv2
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('test.jpg')

if img is None:
    print("Error: Could not load test.jpg! Check file path.")
    exit()

# Optional: Show with matplotlib (works even with headless OpenCV)
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img_rgb)
# plt.title("Test Image - Press Close to continue")
# plt.axis('off')
# plt.show()  # This will block until you close the window

# Preprocessing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 255, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# OCR
custom_config = r'--oem 3 --psm 3'
text = pytesseract.image_to_string(thresh, config=custom_config, lang='eng')

# print("╔════════════════════════════════════════════════════╗")
# print("║          ALL EXTRACTED TEXT FROM test.jpg          ║")
# print("╚════════════════════════════════════════════════════╝")
# print(text.strip())
# print("\n(End of extracted text)")

textlist = text.lower()
textlist = textlist.split("\n")
for i in textlist: # postal code
    data = i.split()
    for j in data:
        if j.find("singapore") == 0:
            print(i)

for i in textlist: # phone numbers
    data = i.split()
    for j in data:
        if j.find("office") == 0:
            print(i)
        elif j.find("hp") == 0:
            print(i)

for i in textlist: # website
    data = i.split()
    for j in data:
        if j.find("www") == 0:
            print(i)

for i in textlist: # email
    if i.find("@") == 0:
        print(i)
    data = i.split()
    for j in data:
        if j.find("@") == 0:
            print(i)
        email = j.split()
        for x in email:
            if x.find("@") == 0:
                print(i)


print(textlist)