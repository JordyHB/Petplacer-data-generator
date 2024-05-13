import customtkinter as ctk

from frames.HomeTabSelection import HomeTabSelection
from frames.LoginFrame import LoginFrame
from frames.UserBar import UserBar
from state.AppState import AppState

# Set the appearance mode and default color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pet Placer Dummy Data Generator")
        self.geometry("600x400")

        self.app_state = AppState()

        # inserts the user bar
        self.user_bar = UserBar(self, self.app_state)

        # inserts home tab selection frame
        self.tab_selection = HomeTabSelection(main=self)

        # registers login frame
        self.login_frame = LoginFrame(self, self.app_state)

        # dummy frame for testing
        self.frame2 = ctk.CTkFrame(self)
        label2 = ctk.CTkLabel(self.frame2, text="this is tab 2")
        label2.pack()

        self.currently_shown_frame = self.frame2

        # starts the loop showing the initial frame
        self.show_frame(self.currently_shown_frame)
        self.mainloop()

    def show_frame(self, frame):

        # Forgets the old frame
        self.currently_shown_frame.pack_forget()

        # Show the selected frame and set it as the currently shown frame
        self.currently_shown_frame = frame
        frame.pack(side="top", fill="both", expand=True)


App()
