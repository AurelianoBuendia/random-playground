from random import randint, sample
import numpy as np


def select_random_integer(num_options: int):
    return randint(1, num_options)


def play_monty_hall(switch_door: bool, num_options: int = 3):
    if num_options < 3 or num_options > 100:
        raise ValueError("Minimum number of doors is 3 and maximum is 100.")
    prize_door = select_random_integer(num_options)
    player_door = select_random_integer(num_options)
    doors = list(range(1, num_options + 1))
    monty_options = [door for door in doors if door not in (prize_door, player_door)]
    total_options = num_options - 2
    monty_choices = sample(monty_options, k=total_options)
    # print(f"\nprize door is: {prize_door}")
    # print(f"player_choice initial is: {player_door}")
    if switch_door:
        unavailable = [player_door]  # Player chose switch, so his current door is forbidden
        unavailable.extend(monty_choices)  # All doors opened by Monty are forbidden
        player_options = [i for i in doors if i not in unavailable]
        player_door = player_options[0] # There should be only one option left, so we can just take the first one
    # print(f"player_choice final is: {player_door}")
    win = False
    if player_door == prize_door:
        # print("player wins!")
        win = True
    return prize_door, player_door, win


def repeat_experiments(num_repetitions: int, switch_door: bool, num_options: int = 3):
    results = []
    for i in range(num_repetitions):
        results.append(play_monty_hall(switch_door, num_options))
    return np.array(results)


if __name__ == "__main__":
    num_trials = 1000000
    results = repeat_experiments(num_trials, True)
    wins = results[:, 2].sum()
    print(f"Switch door ON: {(wins / results.shape[0]) * 100:.2f}% wins in {num_trials} runs.")
    results = repeat_experiments(num_trials, False)
    wins = results[:, 2].sum()
    print(f"Switch door OFF: {(wins / results.shape[0]) * 100:.2f}% wins in {num_trials} runs.")
