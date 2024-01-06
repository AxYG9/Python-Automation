import pyttsx3, PyPDF2

pdfreder = PyPDF2.PdfFileReader(open('book.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdreader.getPage(page_num).extractText()
    clen_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clen_text, 'audio.mp3')
speaker.runAndWait()

speaker.stop()