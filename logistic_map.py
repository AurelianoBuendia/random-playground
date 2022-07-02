
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def calculate_logistic_map_element(curr_element, big_r):
    return big_r * curr_element * (1 - curr_element)


def create_logistic_map(x0, num_points, big_r=2):
    # X_t+1 = R * X_t * (1 − X_t)
    input_list = [x0]
    for i in range(1, num_points):
        input_list.append(calculate_logistic_map_element(input_list[i - 1], big_r))
    logistic_map = np.array(input_list)
    return logistic_map


if __name__ == "__main__":
    start_values = [0.2, 0.5, 0.99]
    big_r_values = [2.0, 3.49, 4.0]
    num_points = 100
    figure, axes = plt.subplots(nrows=3, ncols=3, figsize=(16, 12))
    x = 0
    for big_r in big_r_values:
        y = 0
        # Uncomment the lines below to observe the behavior of the logistic map for R = 4.0 with
        # small variations of the initial value
        if big_r == 4.0:
            start_values = [0.2, 0.2000001, 0.2000000100002]
        for start in start_values:
            print(str(start), str(big_r))
            l_map = create_logistic_map(start, num_points, big_r)
            plot = sns.lineplot(data=l_map, ax=axes[x, y])
            plot.set_xlabel(f"R = {big_r}")
            plot.set_ylabel(f"x0 = {start}")
            y += 1
        x += 1
    figure.show()
