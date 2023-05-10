

class Options():
    def __init__(self):
        try:
            with open("options.txt", "r") as f:
                lines = f.readlines()
                self.volume = float(lines[0].split(":")[1].strip())
                self.music_enabled = bool(lines[1].split(":")[1].strip())
        except FileNotFoundError:
            self.volume = 1.0
            self.music_enabled = True
            self.write_options()

    def write_options(self):
        with open("options.txt", "w") as f:
            f.write(f"Volume: {self.volume}\n")
            f.write(f"Music Enabled: {self.music_enabled}\n")