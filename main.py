import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            finished = []
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    finished.append(participant)
            for participant in finished:
                self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = {place: runner.name for place, runner in result.items()}
            print(formatted_result)

    def _tournament_test_helper(self, participants, expected_last):
        tournament = Tournament(90, *participants)
        results = tournament.start()
        self.assertTrue(results[len(results)].name == expected_last.name)
        self.__class__.all_results.append(results)

    def test_usain_and_nick(self):
        self._tournament_test_helper([self.usain, self.nick], self.nick)

    def test_andrey_and_nick(self):
        self._tournament_test_helper([self.andrey, self.nick], self.nick)

    def test_usain_andrey_and_nick(self):
        self._tournament_test_helper([self.usain, self.andrey, self.nick], self.nick)


if __name__ == '__main__':
    unittest.main()
