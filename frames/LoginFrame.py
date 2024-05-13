import customtkinter as ctk
import requests


class LoginFrame(ctk.CTkFrame):
    """A class to represent a login frame in tkinter"""

    def __init__(self, window, app_state):
        """Initialize the login frame with the given window"""
        super().__init__(window)
        self.app_state = app_state

        # creates the variable that shows the error message
        self.error_message = ctk.StringVar()

        # creates the grid to center the data
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # creates the inner frame to more easily center the login form
        self.inner_frame = ctk.CTkFrame(self)

        self.username_label = ctk.CTkLabel(self.inner_frame, text="Username", font=("Arial", 16))
        self.username_label.pack(side="top")

        self.username_entry = ctk.CTkEntry(self.inner_frame, font=("Arial", 16))
        self.username_entry.pack(side="top")

        self.password_label = ctk.CTkLabel(self.inner_frame, text="Password", font=("Arial", 16))
        self.password_label.pack(side="top")

        self.password_entry = ctk.CTkEntry(self.inner_frame, show="*", font=("Arial", 16))
        self.password_entry.pack(side="top")

        self.login_button = ctk.CTkButton(self.inner_frame, text="Login", command=self.login, font=("Arial", 16),
                                          height=42)
        self.login_button.pack(side="top", pady=(10, 0))

        self.inner_frame.grid(row=1, column=1, rowspan=3, columnspan=1, sticky="s", pady=(0, 20))

        # adds the banner texts
        self.banner = ctk.CTkLabel(self, text="Login:", font=("Arial", 24))
        self.banner.grid(row=0, column=1, columnspan=1, sticky="", pady=(10, 20))

        # Error label
        self.error_label = ctk.CTkLabel(self, font=("Arial", 16), textvariable=self.error_message, text_color="red")

        # events
        # binds the enter key to the login function
        self.password_entry.bind("<Return>", lambda event: self.login())


    def login(self):
        request_data = {
            "username": self.username_entry.get(),
            "password": self.password_entry.get()
        }

        try:
            response = requests.post(f'{self.app_state.base_url}/auth', json=request_data)
            if response.status_code == 200:
                self.app_state.token = response.json()["jwt"]
                self.app_state.username.set(self.username_entry.get())
            elif response.status_code == 401:
                self.error_message.set("Invalid username or password")
                self.error_label.grid(row=4, column=1, columnspan=1, sticky="n", pady=(0, 20))
                self.error_label.after(4000, lambda: self.error_label.grid_forget())
            else:
                self.error_message.set("Unknown error" + str(response.status_code))
                self.error_label.grid(row=4, column=1, columnspan=1, sticky="n", pady=(0, 20))
                self.error_label.after(4000, lambda: self.error_label.grid_forget())

        except requests.exceptions.ConnectionError:
            print("Connection error")
            self.error_message.set("Connection error")
            self.error_label.grid(row=4, column=1, columnspan=1, sticky="n", pady=(0, 20))
            self.error_label.after(4000, lambda: self.error_label.grid_forget())

