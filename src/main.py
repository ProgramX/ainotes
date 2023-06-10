
# Author: Mujtaba
# Date: June 2023

# This file is a part of "AI Notes" Version 0.1
# It implements a basic notepad ui interface which has very limited functionality.
# It must be noted that it is less likely that I continue development in Tkinter,
# I have decided to use Flutter for portability, but its not sure.

import tkinter as tk
from tkinter import filedialog, messagebox, ttk, font

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill="both", expand=True)

        self.line_label = tk.Label(self.root, text="Line: 1")
        self.line_label.pack(side="left")
        self.column_label = tk.Label(self.root, text="Column: 1")
        self.column_label.pack(side="left")
        self.chars_label = tk.Label(self.root, text="Chars: 0")
        self.chars_label.pack(side="left")
        self.lines_label = tk.Label(self.root, text="Lines: 0")
        self.lines_label.pack(side="left")

        self.current_line = 1
        self.current_column = 1
        self.text_area.bind("<KeyRelease>", self.update_cursor_info)

        self.create_menus()

        self.settings_window = None
        self.font_size_var = tk.StringVar()
        self.font_style_var = tk.StringVar()

        self.toggle_button = tk.Button(self.root, text="Disable AI", relief="flat", bg="green", fg="white",
                                       font=("Arial", 10, "bold"), command=self.toggle_button_clicked)

        self.toggle_button.pack(side="bottom", anchor="se")

        self.button_state = False

    def toggle_button_clicked(self):
        if self.button_state:
            self.toggle_button.configure(bg="green", fg="black", font=("Arial", 10, "bold"))
        else:
            self.toggle_button.configure(bg="yellow", fg="black", font=("Arial", 10, "bold"))

        self.button_state = not self.button_state

        if self.toggle_button['bg'] == "green":
            self.toggle_button['fg'] = "white"
            self.toggle_button['text'] = "Disable AI"
        else:
            self.toggle_button['text'] = "Enable AI"

    def create_menus(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New File", command=self.new_file)
        file_menu.add_command(label="Open File", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        options_menu = tk.Menu(menu_bar, tearoff=0)
        options_menu.add_command(label="Settings", command=self.open_settings)
        menu_bar.add_cascade(label="Options", menu=options_menu)

        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label="Credits", command=self.show_credits)
        menu_bar.add_cascade(label="About", menu=about_menu)

        self.root.config(menu=menu_bar)

    def new_file(self):
        self.text_area.delete("1.0", "end")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete("1.0", "end")
            self.text_area.insert("1.0", content)

    def save_file(self):
        messagebox.showinfo("Save", "File saved successfully.")

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            content = self.text_area.get("1.0", "end")
            with open(file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Save", "File saved successfully.")

    def open_settings(self):
        if self.settings_window is not None:
            self.settings_window.destroy()

        self.settings_window = tk.Toplevel(self.root)
        self.settings_window.title("Settings")
        self.settings_window.geometry("400x300")

        options_frame = tk.Frame(self.settings_window)
        options_frame.pack(side="left", fill="both", expand=True)

        settings_frame = tk.Frame(self.settings_window)
        settings_frame.pack(side="right", fill="both", expand=True)

        options_label = tk.Label(options_frame, text="Options", font=("Arial", 12, "bold"))
        options_label.pack(padx=10, pady=10)

        options_listbox = tk.Listbox(options_frame, selectmode="single")
        options_listbox.pack(fill="both", expand=True)
        options_listbox.bind("<<ListboxSelect>>", self.update_settings)

        options_list = ["Font Size and Style"]
        for option in options_list:
            options_listbox.insert(tk.END, option)

        settings_label = tk.Label(settings_frame, text="Settings", font=("Arial", 12, "bold"))
        settings_label.pack(padx=10, pady=10)

        font_size_label = tk.Label(settings_frame, text="Font Size:")
        font_size_label.pack()

        font_size_entry = tk.Entry(settings_frame, textvariable=self.font_size_var)
        font_size_entry.pack(padx=10, pady=5)

        font_style_label = tk.Label(settings_frame, text="Font Style:")
        font_style_label.pack()

        font_style_combobox = ttk.Combobox(settings_frame, textvariable=self.font_style_var)
        font_style_combobox["values"] = font.families()
        font_style_combobox.pack(padx=10, pady=5)

        apply_button = tk.Button(settings_frame, text="Apply Settings", command=self.apply_settings)
        apply_button.pack(padx=10, pady=10)

    def update_settings(self, event):
        selection = event.widget.curselection()
        if selection:
            option = event.widget.get(selection[0])
            if option == "Font Size and Style":
                current_font = self.text_area["font"]
                font_size = current_font.cget("size")
                font_style = current_font.cget("family")
                self.font_size_var.set(str(font_size))
                self.font_style_var.set(font_style)

    def apply_settings(self):
        font_size = int(self.font_size_var.get())
        font_style = self.font_style_var.get()
        self.text_area.configure(font=(font_style, font_size))

        # Update window size based on the text area content
        text_width = self.text_area.winfo_width()
        text_height = self.text_area.winfo_height()

        # Adjust the window height to accommodate the additional labels
        line_label_height = self.line_label.winfo_height()
        self.root.geometry(f"{text_width}x{text_height + line_label_height}")

        # Update the cursor information
        self.update_cursor_info(None)

    def show_credits(self):
        messagebox.showinfo("Credits", "Original Author: Mujtaba\nThis software is made for students and content creators.")

    def update_cursor_info(self, event):
        self.current_line, self.current_column = self.text_area.index(tk.INSERT).split(".")
        self.line_label.config(text=f"Line: {self.current_line}")
        self.column_label.config(text=f"Column: {self.current_column}")
        self.chars_label.config(text=f"Chars: {len(self.text_area.get('1.0', 'end-1c'))}")
        text_lines = self.text_area.get('1.0', 'end-1c').split('\n')
        num_lines = len(text_lines)
        self.lines_label.config(text=f"Lines: {num_lines}")


if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
