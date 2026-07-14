import numpy as np

# Grid size
ROWS = 5
COLS = 5

# Discount factor
gamma = 0.9

# Convergence threshold
theta = 0.001

# Actions: Up, Down, Left, Right
actions = [(-1,0), (1,0), (0,-1), (0,1)]
action_symbols = ['↑', '↓', '←', '→']

# Pick-up locations (Goal States)
pickup_points = [(0,4), (4,2)]

# Reward Function
def reward(state):
    if state in pickup_points:
        return 10       # Reward for reaching pickup point
    return -1           # Cost for each move

# Transition Function
def next_state(state, action):

    x, y = state

    dx, dy = actions[action]

    nx = min(max(x + dx, 0), ROWS - 1)
    ny = min(max(y + dy, 0), COLS - 1)

    return (nx, ny)

# Initialize Value Function
V = np.zeros((ROWS, COLS))

# ---------- Value Iteration ----------
while True:

    delta = 0
    new_V = np.copy(V)

    for i in range(ROWS):
        for j in range(COLS):

            if (i, j) in pickup_points:
                continue

            action_values = []

            for a in range(4):
                ns = next_state((i, j), a)
                action_values.append(reward(ns) + gamma * V[ns])

            new_V[i, j] = max(action_values)

            delta = max(delta, abs(new_V[i, j] - V[i, j]))

    V = new_V

    if delta < theta:
        break

# ---------- Extract Optimal Policy ----------
policy = np.empty((ROWS, COLS), dtype=str)

for i in range(ROWS):
    for j in range(COLS):

        if (i, j) in pickup_points:
            policy[i, j] = 'P'
            continue

        action_values = []

        for a in range(4):
            ns = next_state((i, j), a)
            action_values.append(reward(ns) + gamma * V[ns])

        best_action = np.argmax(action_values)

        policy[i, j] = action_symbols[best_action]

# ---------- Display Output ----------
print("Optimal Value Function:\n")
print(np.round(V, 2))

print("\nOptimal Dispatch Policy:\n")

for row in policy:
    print(" ".join(row))
