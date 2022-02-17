from dataclasses import dataclass
import characters
import random

class Guess():
    def __init__(self, guess: list[characters.Character]):
        self.team = guess

    def compare_to_answer(self, answer: characters.Team) -> list[str]:
        guess_answer = ["grey"] * 4
        found = answer.team.copy()

        for i, c in enumerate(self.team):
            if answer.team.count(c) >= 1:
                guess_answer[i] = "green"
                found.remove(c)

        for i, c in enumerate(self.team):
            if guess_answer[i] == "green":
                continue

            for f in found:
                if c.element == f.element:
                    guess_answer[i] = "yellow"
                    found.remove(f)
                    break

        return guess_answer

def traveler_exception(char: characters.Character, team: list[characters.Character]):
    # amc 18
    # gmc 19
    # emc 35
    traveler_ids = [18, 19, 35] # just update this in future patches

    # not a traveler
    for id in traveler_ids:
        if char.id == id:
            break
    else:
        return False

    for i, id in enumerate(traveler_ids):
        if char.id != id: # not this traveler
            continue

        # it is this traveler and you ened to see the other travelers
        other_ids = traveler_ids[:i] + traveler_ids[i+1:]

        for other in other_ids:
            for team_char in team:
                if other == team_char.id:
                    return True
    
    return False

class Game():
    def __init__(self, answer: characters.Team):
        self.answer = answer
        self.guesses_left = 4 # SUBJECT TO CHANGE
        self.guesses_made = 0
        self.guess_results = []

    def play(self):
        while self.guesses_left > 0:
            self.guesses_made += 1
            self.guesses_left -= 1

            if self.play_round() == True:
                break

        print(f"This was the team. You made {self.guesses_made} guesses.")
        self.answer.print()

    def play_round(self):
        print(f"Guess a team. You have {self.guesses_left + 1} guess(es) left")

        team_list = []
        team_number = 1
        while team_number < 5:
            char_name = input(f"Team member {team_number}: ")

            if char_name not in characters.character_dict:
                print("That wasn't a valid character.")
                continue
            
            char = characters.character_dict[char_name]

            if char in team_list:
                print("This character is already in the team.")
                continue

            if traveler_exception(char, team_list):
                print("Traveler can only be in one place at a time.")
                continue

            # can be added as not in team
            team_list.append(char)
            team_number += 1
        # exit from loop after team >= 4
        guess = Guess(team_list)
        guess_result = guess.compare_to_answer(self.answer)

        print(guess_result)
        print()
        self.guess_results.append(guess_result)

        for s in guess_result:
            if s != "green":
                return False
        else:
            print("You got it right!")
            return True


if __name__ == "__main__":
    game = Game(random.choice(characters.team_list))
    game.play()
    input() # Hanging input before the thing closes