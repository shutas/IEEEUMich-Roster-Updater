# IEEE Roster Updater
#
# Written by: Shuta Suzuki (shutas@umich.edu)

from tkinter import Tk, Label, Button


def main():
    window = Tk()
    window.geometry("500x500")

    window.title("IEEE Roster Updater")

    label = Label(window, text="Hello World!", font=("Arial Bold", 50))
    label.grid(column=0, row=0)

    button = Button(window, text="Click Me!", command=submit(label))
    button.grid(column=1, row=0)

    window.mainloop()

def submit(label):
    label.configure(text="Button was clicked!!!")

if __name__ == "__main__":
    main()