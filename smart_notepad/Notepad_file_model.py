import os
import string
from tkinter import filedialog

class File_model:
    def __init__(self):
        self.url = ""
        self.key = string.ascii_letters+"".join(str(x) for x in range(0,10))
        self.offset=5

    def encrypt(self, plaintext):
        result = ""
        for i in plaintext:
            try:
                x = self.key.index(i)+self.offset
                v = x%62
                result += self.key[v]

            except ValueError:
                result+=i
        return result

    def decrypt(self, ciphertext):
        result = ""
        for i in ciphertext:
            try:
                x = self.key.index(i)-self.offset
                v = x%62
                result+=self.key[v]

            except ValueError:
                result+=i
        return result

    def open_file(self):
        self.url = filedialog.askopenfilename(title="Select File", filetype = [("Text Document", "*.*")])

    def new_file(self):
        self.url=""

    def save_as(self, msg):
        encrypted_text = self.encrypt(msg)
        self.url = filedialog.asksaveasfile(mode = "w", defaultextension = ".ntxt", filetype= [("All Documents", "*.*"),("Text Documnet", ".txt")])
        self.url.write(encrypted_text)
        file_path=self.url.name
        self.url.close()
        self.url = file_path

    def save_file(self, msg):
        if self.url == "":
            self.url = filedialog.asksaveasfilename(title = "Select filename", defaultextension = ".ntxt", filetype = [("text document","*.*")])
        file_name, file_extension = os.path.splitext(self.url)

        if file_extension == ".ntxt":
            msg = self.encrypt(msg)
            with open(self.url,"w",encoding = "utf-8") as fw:
                fw.write(msg)

    def read_file(self, url=''):
        if url!="":
            self.url = url

        else:
            self.open_file()

        base = os.path.basename(self.url)
        file_name, file_extention = os.path.splitext(self.url)
        fr = open(self.url, "r")
        contents= fr.read()
        if file_extention==".ntxt":
            self.decrypt(contents)
        fr.close()
        return contents,base





