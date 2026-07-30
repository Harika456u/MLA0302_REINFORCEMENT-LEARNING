import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Actions
actions = ["Buy", "Sell", "Hold"]

# Initial policy probabilities
policy = np.array([1/3, 1/3, 1/3], dtype=float)

learning_rate = 0.05
episodes = 500

rewards = []
cumulative_reward = 0

for episode in range(episodes):

    # Select action according to policy
    action = np.random.choice(3, p=policy)

    # Simulate market movement
    market = np.random.choice(["Up", "Down"])

    # Reward calculation
    if action == 0:          # Buy
        reward = 10 if market == "Up" else -5

    elif action == 1:        # Sell
        reward = 10 if market == "Down" else -5

    else:                    # Hold
        reward = 1

    cumulative_reward += reward
    rewards.append(cumulative_reward)

    # Simple policy gradient update
    gradient = np.zeros(3)
    gradient[action] = reward

    policy = policy + learning_rate * gradient

    # Normalize probabilities
    policy = np.maximum(policy, 0.01)
    policy = policy / np.sum(policy)

print("Final Policy Probabilities:\n")

for i in range(3):
    print(actions[i], ":", round(policy[i], 3))

print("\nTotal Reward:", cumulative_reward)

# Plot
plt.figure(figsize=(10,5))
plt.plot(rewards, color='blue')

plt.title("Policy Gradient Learning for Investment Strategy")
plt.xlabel("Episodes")
plt.ylabel("Cumulative Reward")

plt.grid(True)
plt.show()
