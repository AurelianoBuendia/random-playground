import pytest
from monty_hall import play_monty_hall

NUM_TRIALS = 10000


class TestClass:
    @staticmethod
    def run_monty_hall_batch(switch_door, num_trials, num_doors=3):
        wins = 0
        for i in range(num_trials):
            _, _, win = play_monty_hall(switch_door, num_doors)
            if win:
                wins += 1
        return wins

    def test_always_switch_door(self):
        wins = TestClass.run_monty_hall_batch(True, NUM_TRIALS)
        print(wins)
        assert wins >= 0

    def test_never_switch_door(self):
        wins = TestClass.run_monty_hall_batch(False, NUM_TRIALS)
        print(wins)
        assert wins >= 0

    def test_compare_strategies_classic(self):
        wins_with_switch = TestClass.run_monty_hall_batch(True, NUM_TRIALS)
        wins_without_switch = TestClass.run_monty_hall_batch(False, NUM_TRIALS)
        print(f"\nNumber of wins with change: {wins_with_switch} from {NUM_TRIALS} trials")
        print(f"\nNumber of wins without change: {wins_without_switch} from {NUM_TRIALS} trials")
        print(f"\nSuccess rate with change: {((wins_with_switch / NUM_TRIALS) * 100):.2f}%")
        print(f"\nSuccess rate without change: {((wins_without_switch / NUM_TRIALS) * 100):.2f}%")
        assert wins_with_switch >= wins_without_switch

    def test_compare_strategies_with_five_doors(self):
        wins_with_switch = TestClass.run_monty_hall_batch(True, NUM_TRIALS, num_doors=5)
        wins_without_switch = TestClass.run_monty_hall_batch(False, NUM_TRIALS, num_doors=5)
        print(f"\nNumber of wins with change and five doors: {wins_with_switch} from {NUM_TRIALS} trials")
        print(f"\nNumber of wins without change and five doors: {wins_without_switch} from {NUM_TRIALS} trials")
        print(f"\nSuccess rate with change: {((wins_with_switch / NUM_TRIALS) * 100):.2f}%")
        print(f"\nSuccess rate without change: {((wins_without_switch / NUM_TRIALS) * 100):.2f}%")
        assert wins_with_switch >= wins_without_switch

    def test_compare_strategies_with_hundred_doors(self):
        wins_with_switch = TestClass.run_monty_hall_batch(True, NUM_TRIALS, num_doors=100)
        wins_without_switch = TestClass.run_monty_hall_batch(False, NUM_TRIALS, num_doors=100)
        print(f"\nNumber of wins with change and hundred doors: {wins_with_switch} from {NUM_TRIALS} trials")
        print(f"\nNumber of wins without change and hundred doors: {wins_without_switch} from {NUM_TRIALS} trials")
        print(f"\nSuccess rate with change: {((wins_with_switch / NUM_TRIALS) * 100):.2f}%")
        print(f"\nSuccess rate without change: {((wins_without_switch / NUM_TRIALS) * 100):.2f}%")
        assert wins_with_switch >= wins_without_switch
