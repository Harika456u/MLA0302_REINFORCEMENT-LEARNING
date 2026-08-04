import random

# User Input
episodes = int(input("Enter number of episodes: "))
learning_rate = float(input("Enter learning rate (e.g., 0.1): "))
discount_factor = float(input("Enter discount factor (e.g., 0.9): "))
epsilon = float(input("Enter epsilon value (e.g., 0.2): "))

# Machine settings (Actions)
actions = ["Low", "Medium", "High"]

# Product Quality Rewards
reward_table = {
    "Low": 5,
    "Medium": 8,
    "High": 10
}

# Q-Table
Q = [[0.0 for _ in range(3)] for _ in range(3)]

for ep in range(episodes):

    state = random.randint(0, 2)

    for step in range(10):

        # Epsilon-Greedy Policy
        if random.random() < epsilon:
            action = random.randint(0, 2)
        else:
            action = Q[state].index(max(Q[state]))

        reward = reward_table[actions[action]]

        next_state = random.randint(0, 2)

        # Q-Learning Update
        Q[state][action] = Q[state][action] + learning_rate * (
            reward + discount_factor * max(Q[next_state]) - Q[state][action]
        )

        state = next_state

print("\nTraining Completed!")

print("\nOptimal Machine Settings:")

for state in range(3):
    best = Q[state].index(max(Q[state]))
    print(f"State {state} --> {actions[best]}")

print("\nQ-Table")

for row in Q:
    print([round(x, 2) for x in row])
