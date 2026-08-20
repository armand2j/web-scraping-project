from tkinter import *

window_width: int = 500
window_height: int = 500

root = Tk()

icon = PhotoImage(file="assets/images/logo.png")

root.title("Footy")
root.wm_iconphoto(False, icon)
root.geometry(f"{window_width}x{window_height}")
root.config(background="#422E2E")

root.mainloop()
