import customtkinter as ctk

class Battle:
    def __init__(self, app):
        self.app = app
        self.players_turn = True
        self.line_index = 1


    def fight(self, player: object, enemy: object) -> None:
        self.app.camp_action_frame.grid_forget()
        self.player = player
        self.enemy = enemy
        self.app.create_battle_gui()

        if self.players_turn:
            self.app.create_battle_gui()
            self.app.enemy_frame.pack_forget()

        else:
            self.app.create_enemy_gui()
            self.app.battle_action_frame.grid_forget()

            self.app.main_frame.after(1500, self.enemy_attack)


    def player_attack(self) -> None:
        self.enemy.take_damage()
        self.players_turn = False

        combat_label = ctk.CTkLabel(self.app.main_frame, text=f"{self.line_index}: {self.player.name} hit {self.enemy.name}({self.enemy.race}) for {self.player.damage} damge, using {self.player.weapon}.")
        combat_label.pack()
        self.app.main_frame.after(10, self.app.main_frame._parent_canvas.yview_moveto, 1.0)

        self.line_index += 1

        combat_label = ctk.CTkLabel(self.app.main_frame, text=f"{self.line_index}: {self.enemy.name}({self.enemy.race}) has {self.enemy.health} left.")
        combat_label.pack()
        self.app.main_frame.after(10, self.app.main_frame._parent_canvas.yview_moveto, 1.0)

        self.line_index += 1

        self.continue_fight()


    def enemy_attack(self):
        self.enemy.attack()
        self.players_turn = True

        combat_label = ctk.CTkLabel(self.app.main_frame, text=f"{self.line_index}: {self.enemy.name} hit {self.player.name} for {self.enemy.damage} damge, using {self.enemy.weapon}.")
        combat_label.pack()
        self.app.main_frame.after(10, self.app.main_frame._parent_canvas.yview_moveto, 1.0)

        self.line_index += 1
        
        combat_label = ctk.CTkLabel(self.app.main_frame, text=f"{self.line_index}: {self.player.name} has {self.player.health} left.")
        combat_label.pack()
        self.app.main_frame.after(10, self.app.main_frame._parent_canvas.yview_moveto, 1.0)

        self.line_index += 1

        self.continue_fight()


    def continue_fight(self) -> None:
        if self.enemy.health > 0 and self.player.health > 0:
            self.fight(self.player, self.enemy)

        else:
            print("Fight over.")