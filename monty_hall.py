from random import randint, sample
import numpy as np


def select_random_integer(num_options: int):
    return randint(1, num_options)


def play_monty_hall(switch_door: bool, num_options: int = 3):
    if num_options < 3:
        raise ValueError("Minimum number of doors is 3.")
    prize_door = select_random_integer(num_options)
    player_door = select_random_integer(num_options)
    doors = list(range(1, num_options + 1))
    monty_options = [i for i in doors if i not in (prize_door, player_door)]
    total_options = num_options - 2
    monty_choices = sample(monty_options, k=total_options)
    # print(f"player_choice initial is: {player_choice}")
    if switch_door:
        unavailable = [player_door]  # Player chose switch, so his current door is forbidden
        unavailable.extend(monty_choices)  # All doors opened by Monty are forbidden
        player_options = [i for i in doors if i not in unavailable]
        player_door = player_options[0]
    # print(f"player_choice final is: {player_choice}")
    win = False
    if player_door == prize_door:
        win = True
    return prize_door, player_door, win


def repeat_experiments(num_repetitions: int, switch_door: bool, num_options: int):
    results = []
    for i in range(num_repetitions):
        results.append(play_monty_hall(switch_door, num_options))
    return np.array(results)


if __name__ == "__main__":
    num_trials = 1000000
    results = repeat_experiments(num_trials, True, 100)
    wins = results[:, 2].sum()
    print(f"Switch door ON: {(np.float64(wins / results.shape[0]) * 100):.2f}% wins of {num_trials:,} runs.")
    results = repeat_experiments(num_trials, False, 100)
    wins = results[:, 2].sum()
    print(f"Switch door OFF: {(np.float64(wins / results.shape[0]) * 100):.2f}% wins of {num_trials:,} runs.")
