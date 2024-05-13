import customtkinter as ctk


class UserBar(ctk.CTkFrame):
    """shows the user info and logout button"""
    def __init__(self, window, app_state):
        super().__init__(window)

        self.current_user_label = ctk.CTkLabel(self, textvariable=app_state.username)
        self.current_user_label.pack(side="right", padx=15)

        self.pack(fill="x")
