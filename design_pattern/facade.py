# Subsystem classes
class Amplifier:
    def on(self):
        print("Amplifier is on")

    def set_volume(self, level):
        print(f"Amplifier volume set to {level}")

    def off(self):
        print("Amplifier is off")

class Tuner:
    def on(self):
        print("Tuner is on")

    def set_frequency(self, frequency):
        print(f"Tuner frequency set to {frequency} MHz")

    def off(self):
        print("Tuner is off")

class DVDPlayer:
    def on(self):
        print("DVD Player is on")

    def play(self, movie):
        print(f"Playing movie: {movie}")

    def stop(self):
        print("DVD Player stopped")

    def eject(self):
        print("DVD ejected")

    def off(self):
        print("DVD Player is off")

class Projector:
    def on(self):
        print("Projector is on")

    def off(self):
        print("Projector is off")

    def wide_screen_mode(self):
        print("Projector in widescreen mode")

# Facade class
class HomeTheaterFacade:
    def __init__(self, amp, tuner, dvd, projector):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.projector = projector

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.amp.on()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)
        self.projector.on()
        self.projector.wide_screen_mode()

    def end_movie(self):
        print("Shutting down the movie theater...")
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()
        self.projector.off()

# Usage
amp = Amplifier()
tuner = Tuner()
dvd = DVDPlayer()
projector = Projector()

home_theater = HomeTheaterFacade(amp, tuner, dvd, projector)
home_theater.watch_movie("Inception")
# Output:
# Get ready to watch a movie...
# Amplifier is on
# Amplifier volume set to 5
# DVD Player is on
# Playing movie: Inception
# Projector is on
# Projector in widescreen mode

home_theater.end_movie()
# Output:
# Shutting down the movie theater...
# Amplifier is off
# DVD Player stopped
# DVD ejected
# DVD Player is off
# Projector is off
