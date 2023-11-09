class Warrior:
    def __init__(self):
        self.experience = 100
        self.level = self.experience // 100
        self.titles = [
            "Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master",
            "Greatest"
        ]
        self.rank = self.titles[self.level//10]
        self.achievements = []

    def update(self, gain):
        self.experience = self.experience + gain if self.experience + gain < 10000 else 10000
        self.level = self.experience // 100
        self.rank = self.titles[self.level // 10]

    def training(self, req):
        if req[2] <= self.level:
            self.update(req[1])
            self.achievements.append(req[0])
            return req[0]
        else:
            return "Not strong enough"

    def battle(self,enm_lvl):
        if 0 < enm_lvl < 101:
            if enm_lvl == self.level:
                self.update(10)
                return "A good fight"
            elif self.level - enm_lvl == 1:
                self.update(5)
                return "A good fight"
            elif self.level - enm_lvl > 1:
                return "Easy fight"
            elif self.level // 10 < enm_lvl // 10 and enm_lvl - self.level > 4:
                return "You've been defeated"
            else:
                self.update((enm_lvl - self.level)**2 * 20)
                return "An intense fight"


        else:
            return "Invalid level"
