import tkinter
import tkinter.messagebox
from tkinter import ttk
import customtkinter
from customtkinter import CTkImage
import sys
import subprocess
import winreg
import os

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Not NetHawk.py")
        self.geometry(f"{1200}x{600}")
        self.minsize(900, 600)


        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=8, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Not NetHawk",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Start Scan",
                                                        command=self.start_scan_botton)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Stop Scan",
                                                        command=self.stop_scan_botton)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Save Results",
                                                        command=self.save_results)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:",
                                                            anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create center frame
        self.main_entry_frame = customtkinter.CTkFrame(self)
        self.main_entry_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.main_entry_frame.columnconfigure((1, 2, 3, 4), weight=1)
        self.main_entry_frame.grid_rowconfigure(0, weight=0)
        self.main_entry_frame.grid_rowconfigure(1, weight=0)
        self.main_entry_frame.grid_rowconfigure(2, weight=1)
        self.main_entry_frame.grid_rowconfigure(3, weight=0)
        self.main_entry_frame.grid_rowconfigure(4, weight=1)

        # row 0
        self.label_start_scan = customtkinter.CTkLabel(master=self.main_entry_frame, text="Start Scan IP:",
                                                       font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label_start_scan.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.start_entry = customtkinter.CTkEntry(self.main_entry_frame, placeholder_text="192.168.0.1")
        self.start_entry.grid(row=0, column=1, padx=(0, 20), pady=(10, 10), sticky="nsew")
        self.label_end_scan = customtkinter.CTkLabel(master=self.main_entry_frame, text="End Scan IP:",
                                                     font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label_end_scan.grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.end_entry = customtkinter.CTkEntry(self.main_entry_frame, placeholder_text="192.168.0.254")
        self.end_entry.grid(row=0, column=3, padx=(0, 20), pady=(10, 10), sticky="nsew")

        # row 1 and 2
        # Create the results treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#333", foreground="#fff", fieldbackground="#333")
        self.style.map("Treeview", background=[("selected", "#444")])
        self.style.configure('Treeview.Heading', background="#444", foreground="#fff")
        self.label_treeview = customtkinter.CTkLabel(master=self.main_entry_frame, width=250, text="Results",
                                                     font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label_treeview.grid(row=1, column=0, columnspan=4, rowspan=1, padx=(10, 0),
                                 pady=(10, 0), sticky='new')
        self.results_columns = ('IP Address', 'Hostname', 'MAC Address', 'Ping', 'Connectivity')
        self.results_treeview = ttk.Treeview(self.main_entry_frame, columns=self.results_columns,
                                             show='headings')
        self.results_treeview.grid(row=2, column=0, columnspan=4, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # Configure the results treeview columns
        for column in self.results_columns:
            self.results_treeview.heading(column, text=column)
            self.results_treeview.column(column, anchor='center')
            self.results_treeview.column(column, width=150)

        # row 3 - add code for this row later
        # Create the output console
        self.console_output = customtkinter.CTkTextbox(self.main_entry_frame, width=250)
        self.console_output.configure(font=('Consolas', 12, 'bold'))
        self.console_output.grid(row=3, column=0, columnspan=4, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # row 4 - add progress bar from its frame
        self.progressbar_1 = customtkinter.CTkProgressBar(self.main_entry_frame)
        self.progressbar_1.grid(row=4, column=0, columnspan=4, padx=(20, 10), pady=(10, 10), sticky="ews")
        self.main_entry_frame.grid_rowconfigure(4, weight=0)

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Ping Threshold",
                                                        font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="ew")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="25ms",
                                                           variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="50ms",
                                                           variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="100ms",
                                                           variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_4 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="250ms",
                                                           variable=self.radio_var, value=3)
        self.radio_button_4.grid(row=4, column=2, pady=10, padx=20, sticky="n")

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(master=self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(5, 0), sticky="nsew")
        self.label_checkbox_group = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text="Options",
                                                           font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label_checkbox_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="ew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="Mac Address")
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="Host Name")
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="w")
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="Ping")
        self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="w")

        self.exit_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", text="Exit",
                                                     border_width=2, text_color=("gray10", "#DCE4EE"),
                                                     command=self.exit)
        self.exit_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # set default values
        self.start_entry.insert(0, "192.168.0.1") # this will have user's subnet in the end
        self.end_entry.insert(0, "192.168.0.254") # this will have user's subnet in the end
        self.sidebar_button_2.configure(state="disabled")
        self.sidebar_button_3.configure(state="disabled")
        self.checkbox_1.select()
        self.checkbox_2.select()
        self.checkbox_3.select()
        self.radio_button_3.select()
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.progressbar_1.configure(mode="indeterminnate", progress_color="green")
        self.progressbar_1.start()
        self.console_output.insert("0.0", "Console\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def get_os_dark_mode(self):
        if sys.platform == "win32":
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                     "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
                value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
                print(value)
                return "Light" if value == 1 else "Dark"
            except:
                return None
        elif sys.platform == "darwin":
            try:
                cmd = "defaults read -g AppleInterfaceStyle"
                output = subprocess.check_output(cmd, shell=True)
                print(output)
                return "Light" if output.strip() == b'Light' else "Dark"
            except:
                return None
        elif sys.platform.startswith("linux"):
            try:
                cmd = "gsettings get org.gnome.desktop.interface gtk-theme"
                output = os.popen(cmd).read()
                print(output)
                return "Light" if "Adwaita" in output else "Dark"
            except:
                return None
        else:
            return None

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        if new_appearance_mode.lower() == "light":
            self.treeview_light()
        elif new_appearance_mode.lower() == "dark":
            self.treeview_dark()
        else:
            if self.get_os_dark_mode().lower() == "light":
                self.treeview_light()
            else:
                self.treeview_dark()
        # get current treeview data
        treeview_data = []
        for child in self.results_treeview.get_children():
            treeview_data.append(self.results_treeview.item(child)['values'])

        # save properties of the old treeview
        treeview_style = self.results_treeview.cget("style")
        treeview_width = self.results_treeview.winfo_width()
        treeview_height = self.results_treeview.winfo_height()

        # destroy old treeview
        self.results_treeview.destroy()

        # create new treeview with updated style
        self.results_treeview = ttk.Treeview(self.main_entry_frame, columns=self.results_columns, show='headings',
                                             style=treeview_style)
        self.results_treeview.grid(row=2, column=0, columnspan=4, padx=(20, 0), pady=(20, 0), sticky="new")

        # set size of the new treeview to match the old one
        for idx, column in enumerate(self.results_columns):
            self.results_treeview.column(column, width=treeview_width)
        self.results_treeview.configure(height=treeview_height)

        # configure the columns of the new treeview
        for column in self.results_columns:
            self.results_treeview.heading(column, text=column)
            self.results_treeview.column(column, anchor='center')
            self.results_treeview.column(column, width=150)

        # add data to the new treeview
        for data in treeview_data:
            self.results_treeview.insert('', 'end', values=data)

    def treeview_light(self):
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#fff", foreground="#000", fieldbackground="#fff")
        self.style.map("Treeview", background=[("selected", "#eee")])
        self.style.configure('Treeview.Heading', background="#ccc", foreground="#000")

    def treeview_dark(self):
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#333", foreground="#fff", fieldbackground="#333")
        self.style.map("Treeview", background=[("selected", "#444")])
        self.style.configure('Treeview.Heading', background="#444", foreground="#fff")

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def start_scan_botton(self):
        print("start scan click")

    def stop_scan_botton(self):
        print("stop scan click")

    def save_results(self):
        print("save_results button press")

    def exit(self):
        return exit()


if __name__ == "__main__":
    app = Gui()
    app.mainloop()