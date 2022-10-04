class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def give_likes(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return f"{self._name} - {self.year}- {self._likes} like(s)"


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f"{self._name} - {self.year} - {self.duration} minutes - {self._likes} like(s)"


class Series(Program):
    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season

    def __str__(self):
        return f"{self._name} - {self.year} - {self.season} seasons - {self._likes} like(s)"


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    @property
    def lists(self):
        return self._programs

    def __len__(self):
        return len(self._programs)


avengers = Movie("Avengers - Infinite War", 2018, 150)
flash = Series("Flash", 2014, 7)
spider_man = Movie("Spider man - no way home", 2021, 157)
final_space = Series("Final space", 2018, 3)


avengers.give_likes()
flash.give_likes()
spider_man.give_likes()
final_space.give_likes(), final_space.give_likes()


Series_and_movies = [avengers, spider_man, flash, final_space]
weekend_playlist = Playlist("Weekend", Series_and_movies)

print(f"playlist size: {len(weekend_playlist)}")

len(weekend_playlist)

for program in weekend_playlist:
    print(program)

print(f'its here or not? {final_space in weekend_playlist}')
