
from random import randint, choice


def select_random_integer(num_options=3):
    return randint(1, num_options)


def play_monty_hall(switch_door, num_options=3):
    prize_door = select_random_integer(num_options)
    player_door = select_random_integer(num_options)
    monty_options = [i for i in range(1, num_options + 1) if i not in (prize_door, player_door)]
    monty_choice = choice(monty_options)
    # print(f"player_choice initial is: {player_choice}")
    if switch_door:
        player_options = [i for i in range(1, num_options + 1) if i not in (player_door, monty_choice)]
        player_door = choice(player_options)
    # print(f"player_choice final is: {player_choice}")
    win = False
    if player_door == prize_door:
        win = True
    return prize_door, player_door, win


if __name__ == "__main__":
    win_choice, player_choice, victory = play_monty_hall(False)
    print(f"Prize door is: {win_choice}, Player door is: {player_choice}, Result is: {victory}")

