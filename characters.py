from dataclasses import dataclass

@dataclass
class Character():
    name: str
    weapon: str
    element: str

Xiangling = Character("Xiangling", "Polearm", "Pyro")
Bennett = Character("Bennett", "Sword", "Pyro")
Xingqiu = Character("Xingqiu", "Sword", "Hydro")
Sucrose = Character("Sucrose", "Catalyst", "Anemo")
Chongyun = Character("Chongyun", "Claymore", "Cryo")
Shenhe = Character("Shenhe", "Polearm", "Cryo")