import customtkinter as ctk

from buttons.Button import Button
from request_data_generators.ShelterRequestGen import ShelterRequestGen


class HomeTabSelection(ctk.CTkFrame):
    """A class to represent a home tab selection frame in tkinter"""
    def __init__(self, main):
        """Initialize the home tab selection frame with the given window"""
        super().__init__(main)

        self.main = main

        self.home_button = Button(self, "Home", command=self.home)

        self.login_tab_button = Button(self, "Login", command=self.login_tab)

        self.tab2_button = Button(self, "Auto Shelter", command=self.auto_shelter_tab)

        self.pack(side="left", fill="both")

    def home(self):
        self.main.show_frame(self.main.home_frame)

    def login_tab(self):
        self.main.show_frame(self.main.login_frame)

    def auto_shelter_tab(self):
        ShelterRequestGen.preload_data_into_mem()
