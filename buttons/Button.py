import customtkinter as ctk


class Button:
    """A class to represent a button widget in tkinter"""
    def __init__(self, parent, text, command=None):
        """Initialize the button widget with the given text, background color, and foreground color"""
        self.button = ctk.CTkButton(parent, text=text, command=command)
        self.button.pack(padx=10, pady=10, fill="both")
