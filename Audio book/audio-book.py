from gtts import gTTS
from PyPDF2 import PdfReader

with open('instr.pdf', 'rb') as pdf_file:
  reader = PdfReader(pdf_file)
  count = len(reader.pages)
  store = []

  for i in range(count):
    try:
      page = reader.pages[i]
      store.append(page.extract_text())
    except Exception as e:
      print(f"Error found in page {i} : {e}")
      exit()

combination = " ".join(store).strip()

if combination:
  print(combination)

  language = 'en'
  constructor = gTTS(text=combination, lang=language, slow=False)
  constructor.save("SER.mp3")
  print("Audio file created")
else:
  print("No readavle content in pdf")