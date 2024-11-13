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

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


import runner_and_tournament as run_turn
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [
            run_turn.Runner('Усэйн', 10),
            run_turn.Runner('Андрей', 9),
            run_turn.Runner('Ник', 3),
        ]

    @classmethod
    def tearDownClass(cls):
        for i, f in cls.all_results.items():
            print("{}:".format(i))
            for e, d in f.items():
                print("{}: {}".format(e, d))

    def test_1(self):
        turn_1 = run_turn.Tournament(90, self.runners[0], self.runners[2])
        result = turn_1.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Усейн и Ник"] = result

    def test_2(self):
        turn_2 = run_turn.Tournament(90, self.runners[1], self.runners[2])
        result = turn_2.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Андрей и Ник"] = result

    def test_3(self):
        turn_3 = run_turn.Tournament(90, *self.runners)
        result = turn_3.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Усейн, Андрей и Ник"] = result

if __name__ == '__main__':
    unittest.main()