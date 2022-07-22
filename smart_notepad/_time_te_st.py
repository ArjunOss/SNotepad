# import datetime
#
# x = datetime.time.
#
# print(x)

# import time
#
# ti = time.gmtime()[7:]
#
# x = ti[7:]
#
# print(time.asctime())
#
# print(time.time())

# from time import strftime
#
# def time():
#
#     string = strftime('%H:%M:%S %p')
#     print(string)
#
# time()

# import time
#
# x = time.time()
# print(x)

#
# # importing whole module
# from tkinter import *
# # from tkinter.ttk import *
#
# # importing strftime function to
# # retrieve system's time
# from time import strftime
#
# # creating tkinter window
# root = Tk()
# root.title('Clock')

# # This function is used to
# # display time on the label
# def time():
#     string = strftime('%H:%M:%S %p')
#     lbl.config(text = string)
#     lbl.after(1000, time)
#
# # Styling the label widget so that clock
# # will look more attractive
# lbl = Label(root, font = ('calibri', 40, 'bold'),
#             background = 'purple',
#             foreground = 'white')
#
# # Placing clock at the centre
# # of the tkinter window
# # lbl.pack(anchor = 'center')
# lbl.grid()
# time()
#
# mainloop()



# importing only those functions which
# are needed
#from tkinter import Tk, mainloop, TOP
#from tkinter.ttk import Button

# time function used to calculate time
from time import time

# creating tkinter window



from tkinter import *
import time

root = Tk()

root.geometry("200x200")

l1 = Label(root)
def ti():
    st = time.perf_counter()
    # st = time.monotonic()
    x = int(st).__format__("%H:%M:%S")
    # x = st
    l1.configure(text = x)
    l1.after(1, ti)

l1.pack()
ti()

root.mainloop()