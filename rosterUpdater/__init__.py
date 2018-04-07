# IEEE Roster Updater
#
# Written by: Shuta Suzuki (shutas@umich.edu)

from tkinter import Tk, Label, Button

class RosterUpdater(object):
    def __init__(self, window):
        self.window = window
        self.window.geometry("750x500")
        self.window.title("IEEE Roster Updater")

        self.appLabel = Label(window, text="UMichIEEE Roster Updater", justify="center", font=("Arial Bold", 50))
        self.appLabel.pack()
        self.versionLabel = Label(window, text="Version 1.0", justify="center", font=("Arial", 18))
        self.versionLabel.pack()

if __name__ == "__main__":
    myWindow = Tk()
    myRosterUpdater = RosterUpdater(myWindow)
    myWindow.mainloop()