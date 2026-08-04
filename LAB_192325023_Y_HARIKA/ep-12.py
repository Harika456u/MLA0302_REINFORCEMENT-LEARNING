import random

# User Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

goal = tuple(map(int, input("Enter goal position (row col): ").split()))

n_obstacles = int(input("Enter number of obstacles: "))
obstacles = set()

print("Enter obstacle positions (row col):")
for _ in range(n_obstacles):
    obstacles.add(tuple(map(int, input().split())))

episodes = int(input("Enter number of episodes: "))

# Parameters
alpha = 0.1
gamma = 0.9
epsilon = 0.2

actions = ["UP", "DOWN", "LEFT", "RIGHT"]

# Q-table
Q = {}

def get_q(state):
    if state not in Q:
        Q[state] = [0.0] * 4
    return Q[state]

def choose_action(state):
    if random.random() < epsilon:
        return random.randint(0, 3)
    return get_q(state).index(max(get_q(state)))

for ep in range(episodes):

    state = (0, 0)
    action = choose_action(state)

    while state != goal:

        r, c = state

        if action == 0:
            nr, nc = r - 1, c
        elif action == 1:
            nr, nc = r + 1, c
        elif action == 2:
            nr, nc = r, c - 1
        else:
            nr, nc = r, c + 1

        # Boundary check
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            nr, nc = r, c

        next_state = (nr, nc)

        if next_state in obstacles:
            reward = -1
        elif next_state == goal:
            reward = 10
        else:
            reward = -0.1

        next_action = choose_action(next_state)

        q = get_q(state)
        next_q = get_q(next_state)

        # SARSA Update
        q[action] = q[action] + alpha * (
            reward + gamma * next_q[next_action] - q[action]
        )

        state = next_state
        action = next_action

print("\nTraining Completed!\n")

print("Q-Table:")
for state in sorted(Q):
    print(state, ":", [round(x, 2) for x in Q[state]])
