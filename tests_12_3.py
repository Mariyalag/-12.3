import unittest
from run import Runner
from run import Tournament

def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            raise unittest.SkipTest('Тесты в этом кейсе заморожены.')
        else:
            return test_func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Maria")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Ket")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Olga")
        runner2 = Runner("Sem")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for results in cls.all_results.values():
            print(results)

    @skip_if_frozen
    def test_race_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = {rank: runner.name for rank, runner in results.items()}
        self.assertEqual(self.all_results[len(self.all_results)][1], "Усэйн")

    @skip_if_frozen
    def test_race_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = {rank: runner.name for rank, runner in results.items()}
        self.assertEqual(self.all_results[len(self.all_results)][1], "Андрей")

    @skip_if_frozen
    def test_race_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = {rank: runner.name for rank, runner in results.items()}
        self.assertEqual(self.all_results[len(self.all_results)][1], "Усэйн")

if __name__ == "__main__":
    unittest.main()

