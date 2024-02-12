class Data:
    def __init__(self, app, workbook, worksheet):
        self.app = app
        self.workbook = workbook
        self.worksheet = worksheet

    
    def create_labels(self):
        label_list = ["Name", "Level", "XP", "Health", "Max Health", "Weapon", "Damage"]
        
        for i in range(len(label_list)):
            self.worksheet["A" + str(i+1)].value = label_list[i]
        self.workbook.save(self.app.data_file)
        print("Labels created.")


    def save_data(self):
        player = self.app.player

        to_save_list = [player.name, player.level, player.xp, player.health, player.max_health, player.weapon, player.damage]

        for i in range(len(to_save_list)):
            self.worksheet["B" + str(i+1)].value = to_save_list[i]
        self.workbook.save(self.app.data_file)
        print("Data saved.")


    def load_data(self):
        player = self.app.player

        player.name = self.worksheet["B1"].value
        player.level = self.worksheet["B2"].value
        player.xp = self.worksheet["B3"].value
        player.health = self.worksheet["B4"].value
        player.max_health = self.worksheet["B5"].value
        player.weapon = self.worksheet["B6"].value
        player.damage = self.worksheet["B7"].value
        print("Data loaded.")