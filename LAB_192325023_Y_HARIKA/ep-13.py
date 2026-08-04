import random

# User Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

goal = tuple(map(int, input("Enter food position (row col): ").split()))
ghost = tuple(map(int, input("Enter ghost position (row col): ").split()))

episodes = int(input("Enter number of episodes: "))

# Parameters
alpha = 0.1
gamma = 0.9
epsilon = 0.2

actions = ["UP", "DOWN", "LEFT", "RIGHT"]

Q = {}

def get_q(state):
    if state not in Q:
        Q[state] = [0.0] * 4
    return Q[state]

for ep in range(episodes):

    state = (0, 0)

    while state != goal:

        # Epsilon-Greedy Action Selection
        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            action = get_q(state).index(max(get_q(state)))

        r, c = state

        if action == 0:
            nr, nc = r - 1, c
        elif action == 1:
            nr, nc = r + 1, c
        elif action == 2:
            nr, nc = r, c - 1
        else:
            nr, nc = r, c + 1

        # Boundary Check
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            nr, nc = r, c

        next_state = (nr, nc)

        # Rewards
        if next_state == goal:
            reward = 10
        elif next_state == ghost:
            reward = -10
        else:
            reward = -1

        # Q-Learning Update
        q = get_q(state)
        next_q = get_q(next_state)

        q[action] = q[action] + alpha * (
            reward + gamma * max(next_q) - q[action]
        )

        state = next_state

print("\nTraining Completed!\n")

print("Learned Q-Table:\n")
for state in sorted(Q):
    print(state, ":", [round(x, 2) for x in Q[state]])
