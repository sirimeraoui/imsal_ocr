#go to https://github.com/UB-Mannheim/tesseract/wiki
#install tesseract 4 64x
#pip install pytesseract
import pytesseract
# pip install pillow
from PIL import Image

img = "./assets/pr.png"
img = Image.open(img)

ocr_result = pytesseract.image_to_string(img)

list1 = ocr_result.split("\n")
list1 = [el for el in list1 if el.strip()]

prayersTime =[] 
for i in list1[4:len(list1)]:
     prayersTime.append(i)
dict = {
    "month":list1[0],
    "prayerNames":[list1[1],list1[2],list1[3]],
    "prayersTime": prayersTime,
}
# current results 
print("month:",dict['month'])
for i in dict['prayersTime']:
    print("day:",i)
for i in dict['prayerNames']:
    print("lang1:",i)
