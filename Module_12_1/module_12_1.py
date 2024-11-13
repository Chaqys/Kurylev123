import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner("Test Runner")
        for one in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    def test_run(self):
        runner_1 = Runner("Test Runner_1")
        for two in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)
    def test_challenge(self):
        runner_2 = Runner("Test Runner_2")
        runner_3 = Runner("Test Runner_3")
        for three in range(10):
            runner_2.run()
        for four in range(10):
            runner_3.walk()
        self.assertNotEqual(runner_2.distance, runner_3.distance)

if __name__ == "__main__":
    unittest.main()
