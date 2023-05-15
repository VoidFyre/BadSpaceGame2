

class Scores():
    def __init__(self):
        try:
            with open("scores.txt", "r") as f:
                lines = f.readlines()
                self.high_score = int(lines[0].split(":")[1].strip())
        except FileNotFoundError:
            self.high_score = 0
            self.write_scores(0)

    def write_scores(self, new_score):
        if new_score > self.high_score:
            with open("scores.txt", "w") as f:
                f.write(f"High Score: {new_score}\n")