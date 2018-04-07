# IEEE Roster Updater
#
# Written by: Shuta Suzuki (shutas@umich.edu)

from time import sleep
from tkinter import Tk, Label, Button, Menu, Toplevel, Message, Button, END
from tkinter.scrolledtext import ScrolledText
from selenium import webdriver

class RosterUpdater(object):
    def __init__(self, window):
        """Display GUI for Roster Updater."""
        # General Window Settings
        self.window = window
        self.window.title("IEEEUMich Tools")

        # Menu Bar
        self.menu_bar = Menu(self.window)
        self.file_menu = Menu(self.menu_bar)
        self.file_menu.add_command(label="About", command=self.display_about)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.window.config(menu=self.menu_bar)

        # Heading Labels
        self.app_label = Label(window, text="IEEEUMich Roster Updater", justify="center", font=("Arial Bold", 46))
        self.app_label.grid(row=0, column=0, padx=100, pady=(20, 0))
        self.version_label = Label(window, text="Version Alpha", justify="center", font=("Arial", 18))
        self.version_label.grid(row=1, column=0, pady=(0, 50))

        # Uniqname Text Field
        self.entry_label = Label(window, text="Enter new uniqnames here:", justify="center", font=("Arial", 20))
        self.entry_label.grid(row=2, column=0)
        self.text_field = ScrolledText(window, borderwidth=2, relief="solid")
        self.text_field.grid(row=3, column=0, pady=(0, 50))

        # Submit Button
        self.username = None
        self.password = None
        self.submit_button = Button(window, text="submit", command=self.submit)
        self.submit_button.grid(row=4, column=0, pady=(0, 50))

    def display_about(self):
        """Display About Window."""
        # General About Window Settings
        about_window = Tk()
        about_window.title("About")

        about_text = ("IEEEUMich Roster Updater is a tool aimed to automate "
                     "or at least alleviate the pain of manually adding new "
                     "members to our email roster on MCommunity.\n\n"
                     "This tool was created by Shuta Suzuki (shutas@umich.edu)"
                     ".\n\n"
                     "Last Updated: 4/7/2018\n\n"
                     "You can click 'OK' to close this window."
                    )

        # About Text Content
        about_label = Message(about_window, text=about_text, font=("Arial", 16), width=500)
        about_label.grid(row=0, column=0, padx=50, pady=(50, 0))

        # OK Button
        ok_button = Button(about_window, text="OK", command=about_window.destroy)
        ok_button.grid(row=1, column=0, pady=(50, 50))


    def submit(self):
        """Handle Submitted Uniqnames."""
        submitted_text = self.text_field.get(1.0, END).strip()
        uniqname_list = submitted_text.split()
        for count, uniqname in enumerate(uniqname_list):
            print("Student " + str(count) + ": " + uniqname)
        
        driver = webdriver.Chrome("rosterUpdater/drivers/mac/chromedriver")
        driver.get("https://mcommunity.umich.edu/")
        #log_in_link = driver.find_element_by_link_text("Log In")
        log_in_link = driver.find_element_by_class_name("gwt-Anchor")
        log_in_link.click()
        username_text_field = driver.find_element_by_id("login")
        password_text_field = driver.find_element_by_id("password")
        login_button = driver.find_element_by_id("loginSubmit")
        username_text_field.send_keys("shutas")
        password_text_field.send_keys("NMB48sayaka")
        login_button.click()
        driver.quit()

if __name__ == "__main__":
    my_window = Tk()
    my_roster_updater = RosterUpdater(my_window)
    my_window.mainloop()