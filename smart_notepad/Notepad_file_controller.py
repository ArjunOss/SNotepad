import Notepad_file_model
import speech_recognition as s

class File_controller:
    def __init__(self):
        self.file_model = Notepad_file_model.File_model()

    def save_file(self,msg):
        self.file_model.save_file(msg)

    def save_as(self, msg):
        self.file_model.save_as(msg)

    def read_file(self, url):
        self.file_model.read_file(url)

    def new_file(self):
        self.file_model.new_file()

    def take_query(self):
        sr = s.Recognizer()
        print("Say something")
        with s.Microphone() as m:
            audio = sr.listen(m)
            sr.adjust_for_ambient_noise(m, duration=3)
            text = sr.recognize_google(audio, language='en-IN')
            return text