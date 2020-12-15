import tkinter as tk

# window options
textWidth = 50


def launch_config():
    window = tk.Tk()

    window.title("Configure Aternos Bot")
    window.geometry('600x300')

    label = tk.Label(window, text="Hello, this is the configuration window "
                                  "for your Aternos discord bot.\n"
                                  "Please fill in all the fields.")
    label.grid(row=0, column=0)
    label.place(x=125, y=20)

    bot_token_label = tk.Label(window, text="Bot Token: ")
    bot_token_label.place(x=120/1.5, y=130/1.5)
    bot_token_entry = tk.Entry(window, width=textWidth)
    bot_token_entry.place(x=280/1.5, y=130/1.5)

    username_label = tk.Label(window, text="Aternos Username: ")
    username_label.place(x=120/1.5, y=160/1.5)
    username_entry = tk.Entry(window, width=textWidth)
    username_entry.place(x=280/1.5, y=160/1.5)

    password_label = tk.Label(window, text="Aternos Password: ")
    password_label.place(x=120/1.5, y=190/1.5)
    password_entry = tk.Entry(window, width=textWidth)
    password_entry.place(x=280/1.5, y=190/1.5)

    save_button = tk.Button(window, text="Save configuration",
                            bg="#1a6600", fg="white")
    save_button['command'] = lambda: save_configuration(bot_token_entry,
                                                        username_entry,
                                                        password_entry, window)
    save_button.place(x=250, y=250/1.5)

    window.mainloop()


def save_configuration(token_entry, username_entry, password_entry, window):
    if token_entry.get() != "" and username_entry.get() != "" and \
       password_entry.get() != "":
        bot_token = f"BOT_TOKEN= {token_entry.get()}"
        username = f"\nUSERNAME_C= {username_entry.get()}"
        password = f"\nPASSWORD_C= {password_entry.get()}"
        with open(".env", "w") as f:
            f.write(bot_token)
            f.write(username)
            f.write(password)
        window.destroy()
    else:
        error = tk.Label(window, text="ERROR: You must fill in all fields.")
        error.place(x=250, y=65)


if __name__ == "__main__":
    launch_config()
