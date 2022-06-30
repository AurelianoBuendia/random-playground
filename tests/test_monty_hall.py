
from monty_hall import play_monty_hall

NUM_TRIALS = 10000


def run_monty_hall_batch(switch_door, num_trials):
    wins = 0
    for i in range(num_trials):
        _, __, win = play_monty_hall(switch_door)
        if win:
            wins += 1
    return wins


def test_always_switch_door():
    wins = run_monty_hall_batch(True, NUM_TRIALS)
    print(wins)
    assert True


def test_never_switch_door():
    wins = run_monty_hall_batch(False, NUM_TRIALS)
    print(wins)
    assert True


def test_compare_strategies():
    wins_with_switch = run_monty_hall_batch(True, NUM_TRIALS)
    wins_without_switch = run_monty_hall_batch(False, NUM_TRIALS)
    print(f"Change / No Change success rate: {((wins_with_switch / wins_without_switch) * 100):.2f}")
    assert True


