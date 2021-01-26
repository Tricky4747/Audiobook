import pyttsx3
import PyPDF2
import  time
book = open("competitive programming.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages

start_page = int(input("Starting page number: ")) - 1
end_page = int(input("Ending page number: "))


pageno = start_page

voiceid = int(input("VoiceID(0 - male, 1 - female): "))
speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[voiceid].id)
speaker.setProperty("rate", 170)


def speak(text):
    speaker.say(text)
    speaker.runAndWait()


for num in range(start_page, end_page):
    page = pdf_reader.getPage(pageno)
    pagetext = page.extractText().replace(".", "   ")
    speak(pagetext)
    pageno += 1
