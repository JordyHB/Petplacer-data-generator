import customtkinter as ctk


class AppState:
    """A class to represent the state of the application"""
    def __init__(self):
        self.username = ctk.StringVar(value="not logged in")
        self.base_url = "http://localhost:8080"
        self.token = None
