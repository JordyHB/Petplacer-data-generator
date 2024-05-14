import customtkinter as ctk


class HomeFrame(ctk.CTkFrame):
    """"A class to represent a home frame in tkinter"""
    def __init__(self, main):
        """Initialize the home frame with the given window"""
        super().__init__(main)

        self.main = main

        self.banner = (
            ctk.CTkLabel(self, text="Welcome to this auto dummy data generator for PetPlacer", font=("Arial", 18))
        )

        self.banner.pack(pady=(5, 0), anchor="n")

        # Adjust the wrap length of the label when the window is resized
        self.banner.bind("<Configure>", self.adjust_label_wrap_length)

    def adjust_label_wrap_length(self, event):
        min_wrap_length = 300
        self.banner.configure(wraplength=max(event.width, min_wrap_length))
