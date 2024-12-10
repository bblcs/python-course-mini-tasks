import numpy as np
import matplotlib.pyplot as plt
import time


def step_python(field):
    return [
        [
            (
                1
                if (
                    field[i][j]
                    and 2
                    <= sum(
                        field[i2][j2]
                        for i2 in range(max(0, i - 1), min(len(field), i + 2))
                        for j2 in range(max(0, j - 1), min(len(field[0]), j + 2))
                    )
                    - field[i][j]
                    <= 3
                )
                or sum(
                    field[i2][j2]
                    for i2 in range(max(0, i - 1), min(len(field), i + 2))
                    for j2 in range(max(0, j - 1), min(len(field[0]), j + 2))
                )
                - field[i][j]
                == 3
                else 0
            )
            for j in range(len(field[0]))
        ]
        for i in range(len(field))
    ]


def step_numpy(field):
    neighbors = (
        sum(np.roll(np.roll(field, i, 0), j, 1) for i in (-1, 0, 1) for j in (-1, 0, 1))
        - field
    )
    return (neighbors == 3) | (field & (neighbors == 2))


def benchmark(f, field, steps=128):
    start = time.time()
    for _ in range(steps):
        field = f(field)
    return time.time() - start


size, steps = 1024, 128
initial = np.random.randint(2, size=(size, size))

time_python = benchmark(step_python, initial.tolist(), steps)
time_numpy = benchmark(step_numpy, initial, steps)

plt.bar(["python list", "numpy"], [time_python, time_numpy])
plt.ylabel("time (s)")
plt.show()
