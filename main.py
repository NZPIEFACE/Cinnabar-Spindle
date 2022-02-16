from dataclasses import dataclass
import characters


@dataclass
class Team():
    name: str
    team: list[characters.Character]

class Guess():
    def __init__(self, guess: Team):
        self.team = guess

    def compare_to_answer(self, answer: Team) -> list[str]:
        guess_answer = ["grey"] * 4
        found = answer.team.copy()

        for i, c in enumerate(self.team.team):
            if answer.team.count(c) >= 1:
                guess_answer[i] = "green"
                found.remove(c)

        for i, c in enumerate(self.team.team):
            if guess_answer[i] == "green":
                continue

            for f in found:
                if c.element == f.element:
                    guess_answer[i] = "yellow"
                    found.remove(f)
                    break

        return guess_answer

National = Team("National", [characters.Xiangling, characters.Bennett, characters.Xingqiu, characters.Chongyun])
Better_National = Guess(Team("Better National", [characters.Xiangling, characters.Bennett, characters.Xingqiu, characters.Sucrose]))
Shenhe_National = Guess(Team("Shenhe National", [characters.Xiangling, characters.Shenhe, characters.Bennett, characters.Xingqiu]))

print(Better_National.compare_to_answer(National))
print(Shenhe_National.compare_to_answer(National))