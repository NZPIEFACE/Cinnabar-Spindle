from dataclasses import dataclass
import characters

class Guess():
    def __init__(self, guess: characters.Team):
        self.team = guess

    def compare_to_answer(self, answer: characters.Team) -> list[str]:
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

class Game():
    def __init__(self, answer: characters.Team):
        self.answer = answer
        self.guesses_left = 4 # SUBJECT TO CHANGE

    def play(self):
        print("Guess a team.")


National = characters.team_dict["OG National"]
Better_National = Guess(characters.team_dict["Better National"])
Shenhe_National = Guess(characters.team_dict["Shenhe National"])

National.print()