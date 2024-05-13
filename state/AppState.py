import customtkinter as ctk


class AppState:
    base_url = "http://localhost:8080"
    token = None

    def __init__(self):
        self.username = ctk.StringVar(value="not logged in")
