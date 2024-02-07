import tkinter as tk

root = tk.Tk()

root.geometry("400x275")

# title bar
root.title("WIP Python GUI Calculator")

# favicom
icon_image = tk.PhotoImage(file='images/calculator_icon.png')
# Set the icon image for the window
root.wm_iconphoto(True, icon_image)

root.mainloop()
