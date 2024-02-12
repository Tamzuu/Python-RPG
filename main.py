import os
import random

import openpyxl as op
import customtkinter as ctk

from package import *

class App():
    def __init__(self):
        self.APPNAME = "RPG"
        self.FILENAME = "RPG Data.xlsx"

        self.window_setup()
        self.file_setup()

    
    def file_setup(self):
        self.local_folder = os.path.expandvars(rf"%APPDATA%\{self.APPNAME}")
        self.data_file = os.path.expandvars(rf"%APPDATA%\{self.APPNAME}\{self.FILENAME}")

        os.makedirs(self.local_folder, exist_ok=True)

        data_file_exists = os.path.isfile(self.data_file)
        
        if data_file_exists:
            self.load_file()

            self.data = Data(self, self.workbook, self.worksheet)
            self.player = Player()
            self.data.load_data()
            self.create_camp_gui()
            self.create_gui()
            self.battle = Battle(self)

        else:
            self.create_file()

            self.data = Data(self, self.workbook, self.worksheet)
            self.data.create_labels()
            self.create_new_character()


    def window_setup(self):
        self.WINDOW = ctk.CTk()
        self.WINDOW.geometry(str(WIDTH) + "x" + str(HEIGHT))
        self.WINDOW.title(self.APPNAME)
        self.WINDOW.resizable(False, False)
        self.WINDOW.grid_propagate(False)

    
    def load_file(self):
        self.workbook = op.load_workbook(self.data_file)
        self.worksheet = self.workbook.active
        print("File loaded.")


    def create_file(self):
        self.workbook = op.Workbook()
        self.worksheet = self.workbook.active

        self.workbook.save(self.data_file)
        print("New file created.")


    def create_gui(self):
        self.create_main_gui()
        self.create_camp_gui()


    def create_main_gui(self):
        self.main_frame = ctk.CTkScrollableFrame(self.WINDOW, fg_color="transparent", width=WIDTH, height=HEIGHT*3/4)
        self.main_frame.place(anchor="n", relx=0.5, rely=0)
        

    def create_camp_gui(self):
        self.camp_action_frame = ctk.CTkFrame(self.WINDOW, fg_color="black", width=WIDTH, height=HEIGHT/4)
        self.camp_action_frame.place(anchor="center", relx=0.5, rely=0.9)
        self.camp_action_frame.grid_propagate(False)

        adventure_button = ctk.CTkButton(self.camp_action_frame, border_color=border_color, fg_color="black", text="Adventure", border_width=border_width, height=HEIGHT/14, width=WIDTH/2.5, command=self.adventure)
        adventure_button.grid(row=0, column=1, padx=30, pady=(25, 10))

        inventory_button = ctk.CTkButton(self.camp_action_frame, border_color=border_color, fg_color="black", text="Inventory", border_width=border_width, height=HEIGHT/14, width=WIDTH/2.5)
        inventory_button.grid(row=0, column=2, padx=30, pady=(25, 10))

        rest_button = ctk.CTkButton(self.camp_action_frame, border_color=border_color, fg_color="black", text="Rest", border_width=border_width, height=HEIGHT/14, width=WIDTH/2.5)
        rest_button.grid(row=1, column=1, padx=30, pady=(10, 25))

        train_button = ctk.CTkButton(self.camp_action_frame, border_color=border_color, fg_color="black", text="Train", border_width=border_width, height=HEIGHT/14, width=WIDTH/2.5)
        train_button.grid(row=1, column=2, padx=30, pady=(10, 25))

        self.camp_action_frame.columnconfigure(0, weight=1)
        self.camp_action_frame.columnconfigure(3, weight=1)


    def create_battle_gui(self):
        self.battle_action_frame = ctk.CTkFrame(self.WINDOW, fg_color="black", width=WIDTH, height=HEIGHT/4)
        self.battle_action_frame.place(anchor="center", relx=0.5, rely=0.9)
        self.battle_action_frame.grid_propagate(False)

        self.enemy_frame = ctk.CTkFrame(self.WINDOW, fg_color="black", width=WIDTH, height=HEIGHT/4)
        self.enemy_frame.place(anchor="center", relx=0.5, rely=0.9)
        self.enemy_frame.pack_propagate(False)
        self.enemy_frame.place_forget()

        attack_button = ctk.CTkButton(self.battle_action_frame, border_color=border_color, fg_color="black", text="Attack", border_width=border_width, height=HEIGHT/14, width=WIDTH/2.5, command=self.battle.player_attack)
        attack_button.grid(row=0, column=1, padx=30, pady=(25, 10))

        special_attack_button = ctk.CTkButton(self.battle_action_frame, border_color=border_color, fg_color="black", text="Special Attack", border_width=border_width, height=HEIGHT/14, width=WIDTH/2.5)
        special_attack_button.grid(row=0, column=2, padx=30, pady=(25, 10))

        inventory_button = ctk.CTkButton(self.battle_action_frame, border_color=border_color, fg_color="black", text="Inventory", border_width=border_width, height=HEIGHT/14, width=WIDTH/2.5)
        inventory_button.grid(row=1, column=1, padx=30, pady=(10, 25))

        flee_button = ctk.CTkButton(self.battle_action_frame, border_color=border_color, fg_color="black", text="Flee", border_width=border_width, height=HEIGHT/14, width=WIDTH/2.5)
        flee_button.grid(row=1, column=2, padx=30, pady=(10, 25))

        self.battle_action_frame.columnconfigure(0, weight=1)
        self.battle_action_frame.columnconfigure(3, weight=1)


    def create_enemy_gui(self):
        self.enemy_frame = ctk.CTkFrame(self.WINDOW, fg_color="black", width=WIDTH, height=HEIGHT/4)
        self.enemy_frame.place(anchor="center", relx=0.5, rely=0.9)
        self.enemy_frame.pack_propagate(False)

        enemy_label = ctk.CTkLabel(self.enemy_frame, text="Enemy's turn")
        enemy_label.pack()


    def create_new_character(self):
        welcome_frame = ctk.CTkFrame(self.WINDOW)
        welcome_frame.pack()
        welcome_label = ctk.CTkLabel(welcome_frame, text="Welcome", font=("Papyrus", 20))
        welcome_label.pack()
        name_input_field = ctk.CTkEntry(welcome_frame, placeholder_text="Enter your name", font=("Papyrus", 20))
        name_input_field.pack()
        name_input_button = ctk.CTkButton(welcome_frame, text="Enter", font=("Papyrus", 20), command=lambda: self.enter(welcome_frame, name_input_field))
        name_input_button.pack()


    def enter(self, welcome_frame, name_input_field):
        if name_input_field.get().isalpha():
            self.player = Player(name_input_field.get())
            welcome_frame.destroy()
            self.create_gui()
            self.data.save_data()
            self.battle = Battle(self)


    def adventure(self):
        self.enemy = Orc(self)
        self.battle.fight(self.player, self.enemy)
        self.create_battle_gui()


    def run(self):
        self.WINDOW.mainloop()

App().run()