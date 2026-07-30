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
action_symbols = ['↑','↓','←','→']

# Delivery points (Goal States)
goals = [(0,4), (4,4)]

# Reward Function
def reward(state):
    if state in goals:
        return 10
    return -1

# Transition Function
def next_state(state, action):

    x, y = state

    dx, dy = actions[action]

    nx = min(max(x + dx, 0), ROWS - 1)
    ny = min(max(y + dy, 0), COLS - 1)

    return (nx, ny)

# Initialize Value Function
V = np.zeros((ROWS, COLS))

# Random Initial Policy
policy = np.random.randint(0, 4, (ROWS, COLS))

policy_stable = False

while not policy_stable:

    # ---------- Policy Evaluation ----------
    while True:

        delta = 0

        for i in range(ROWS):
            for j in range(COLS):

                if (i, j) in goals:
                    continue

                old_value = V[i, j]

                action = policy[i, j]

                ns = next_state((i, j), action)

                V[i, j] = reward(ns) + gamma * V[ns]

                delta = max(delta, abs(old_value - V[i, j]))

        if delta < theta:
            break

    # ---------- Policy Improvement ----------
    policy_stable = True

    for i in range(ROWS):
        for j in range(COLS):

            if (i, j) in goals:
                continue

            old_action = policy[i, j]

            action_values = []

            for a in range(4):
                ns = next_state((i, j), a)
                action_values.append(reward(ns) + gamma * V[ns])

            policy[i, j] = np.argmax(action_values)

            if old_action != policy[i, j]:
                policy_stable = False

# Display Value Function
print("Optimal Value Function\n")
print(np.round(V, 2))

# Display Policy
print("\nOptimal Policy\n")

for i in range(ROWS):
    for j in range(COLS):

        if (i, j) in goals:
            print(" G ", end=" ")

        else:
            print(action_symbols[policy[i, j]], end="  ")

    print()
