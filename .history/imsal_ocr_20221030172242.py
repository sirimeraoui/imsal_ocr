# details in the readme file
import pytesseract
# pip install pillow
from PIL import Image
import arabic_reshaper
from bidi.algorithm import get_display

img = "./assets/pr.png"
img = Image.open(img)

ocr_result = pytesseract.image_to_string(img, lang='ara')
def arabic(text):
    reshaped_text = arabic_reshaper.reshape(ocr_result)    # correct its shape
    bidi_text = get_display(reshaped_text)   
    return bidi_text
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
# print("month:",dict['month'])
# for i in dict['prayersTime']:
#     print("day:",i)
# for i in dict['prayerNames']:
#     print("lang1:",i)

