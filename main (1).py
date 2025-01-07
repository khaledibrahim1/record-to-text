import speech_recognition as sr
import arabic_reshaper
from bidi.algorithm import get_display
from tkinter import *
from tkinter import font

def voiceReco():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        try:
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio, language='ar-AR')
            reshaped_text = arabic_reshaper.reshape(text)
            bidi_text = get_display(reshaped_text)
            try:
                print(bidi_text)
            except UnicodeEncodeError:
                print(bidi_text.encode('utf-8', errors='replace').decode('utf-8'))
            textF.delete("1.0", "end")
            textF.insert(END, bidi_text)
            textF.tag_add("center", "1.0", "end")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Tkinter setup
root = Tk()
root.geometry("500x300")
root.title("khaled")

ButtonFont = font.Font(size=20)
LabelFont = font.Font(size=15)

Label(root, text="النص", font=LabelFont).pack()

textF = Text(root, height=5, width=52, font=LabelFont)
textF.tag_configure("center", justify='center')
textF.pack()

Button(root, text="سجل", font=ButtonFont, command=voiceReco).place(x=220, y=200)

root.mainloop()
