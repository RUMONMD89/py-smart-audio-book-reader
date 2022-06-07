import pyttsx3
import PyPDF2
book = open('apl90b.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
friend = pyttsx3.init()
for num in range(1, 2):
    page = pdfreader.getPage(num)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()
