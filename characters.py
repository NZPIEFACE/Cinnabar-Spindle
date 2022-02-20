from dataclasses import dataclass
import json

@dataclass(order=True, frozen=True)
class Character():
    id: int
    name: str
    weapon: str
    element: str

    def print(self):
        print(f"Name: {self.name}")
        print(f"Weapon: {self.weapon}; Element: {self.element}; ID: {self.id}")
        return

    @staticmethod
    def dict_to_Char(dict):
        return Character(
            dict["id"],
            dict["name"],
            dict["weapon"],
            dict["element"]
        )


@dataclass
class Team():
    name: str
    team: list[Character]

    def print(self):
        print(f"Team name: {self.name}")
        print(f"Members: {', '.join(sorted([x.name for x in self.team]))}")
        return

    @staticmethod
    def dict_to_Team(dict):
        team = []

        for c in dict["team"]:
            team.append(character_dict[c])

        return Team(dict["name"], team)

character_list = []
character_dict = {}

team_list = []
team_dict = {}

character_appearance_dict = {}

with open("data.json") as f:
    obj = json.load(f)

    for i, c in enumerate(obj["characters"]):
        char = Character.dict_to_Char(c)
        character_list.append(char)
        character_dict[char.name] = char
        character_appearance_dict[char.name] = []
        if "aliases" in c:
            for alias in c["aliases"]:
                character_dict[alias] = char

    for i, t in enumerate(obj["teams"]):
        team = Team.dict_to_Team(t)
        team_list.append(team)
        team_dict[team.name] = team

        for c in team.team:
            character_appearance_dict[c.name].append(team)

if __name__ == "__main__":
    for i in character_appearance_dict:
        print(f"{i} {len(character_appearance_dict[i])}")
        #print("; ".join([t.name for t in character_appearance_dict[i]]))

    print(f"Total {len(team_list)}")