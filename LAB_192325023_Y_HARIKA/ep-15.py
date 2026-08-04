import random

# User Input
num_agents = int(input("Enter number of customer service representatives: "))
episodes = int(input("Enter number of episodes: "))

alpha = 0.1
epsilon = 0.2

# Initialize Q-table
Q = [[0.0 for _ in range(num_agents)] for _ in range(num_agents)]

for ep in range(episodes):

    state = random.randint(0, num_agents - 1)

    visited = []

    total_reward = 0

    for step in range(10):

        # Epsilon-Greedy Policy
        if random.random() < epsilon:
            action = random.randint(0, num_agents - 1)
        else:
            action = Q[state].index(max(Q[state]))

        # Simulate call handling time
        handling_time = random.randint(2, 10)

        # Reward = Negative handling time (minimize time)
        reward = -handling_time

        total_reward += reward

        visited.append((state, action, reward))

        state = random.randint(0, num_agents - 1)

    # Monte Carlo Update
    G = 0

    for state, action, reward in reversed(visited):

        G = reward + G

        Q[state][action] = Q[state][action] + alpha * (
            G - Q[state][action]
        )

print("\nTraining Completed!")

print("\nOptimal Assignment Policy")

for i in range(num_agents):
    best = Q[i].index(max(Q[i]))
    print(f"State {i} -> Assign Representative {best}")

print("\nQ-Table")

for row in Q:
    print([round(x, 2) for x in row])
