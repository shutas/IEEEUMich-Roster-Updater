# IEEE Roster Updater
#
# Written by: Shuta Suzuki (shutas@umich.edu)

from tkinter import Tk, Label, Button, Menu, Toplevel, Message, Button

class RosterUpdater(object):
    def __init__(self, window):
        """Display GUI for Roster Updater."""
        # General Window Settings
        self.window = window
        self.window.title("IEEEUMich Tools")

        # Menu Bar
        self.menuBar = Menu(self.window)
        self.fileMenu = Menu(self.menuBar)
        self.fileMenu.add_command(label="About", command=self.displayAbout)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.window.config(menu=self.menuBar)

        # Heading Labels
        self.appLabel = Label(window, text="IEEEUMich Roster Updater", justify="center", font=("Arial Bold", 46))
        self.appLabel.grid(row=0, column=0, padx=100, pady=(20, 0))
        self.versionLabel = Label(window, text="Version 1.0", justify="center", font=("Arial", 18))
        self.versionLabel.grid(row=1, column=0)

    def displayAbout(self):
        """Display About Window."""
        # Generael About Window Settings
        aboutWindow = Tk()
        aboutWindow.title("About")

        aboutText = ("IEEEUMich Roster Updater is a tool aimed to automate "
                     "the process of adding new members to the email roster. "
                     "Click 'OK' to close this window.")

        # About Text Content
        aboutLabel = Message(aboutWindow, text=aboutText, font=("Arial", 20))
        aboutLabel.grid(row=0, column=0, padx=50, pady=(50, 0))

        # OK Button
        okButton = Button(aboutWindow, text="OK", command=aboutWindow.destroy)
        okButton.grid(row=1, column=0, pady=(0, 50))

if __name__ == "__main__":
    myWindow = Tk()
    myRosterUpdater = RosterUpdater(myWindow)
    myWindow.mainloop()