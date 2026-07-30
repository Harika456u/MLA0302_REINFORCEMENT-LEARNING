import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Representatives and success probabilities
representatives = ["CSR A", "CSR B", "CSR C"]
success_prob = [0.60, 0.80, 0.70]

episodes = 1000

returns = np.zeros(3)
visits = np.zeros(3)

episode_rewards = []

for _ in range(episodes):

    # Random assignment policy
    rep = np.random.randint(3)

    # Simulate call resolution
    success = np.random.rand() < success_prob[rep]

    if success:
        reward = 10
    else:
        reward = -5

    returns[rep] += reward
    visits[rep] += 1

    episode_rewards.append(reward)

# Monte Carlo Value Function
value_function = returns / visits

print("Estimated State Values\n")

for i in range(3):
    print(f"{representatives[i]} : {value_function[i]:.2f}")

# Running average reward
running_avg = np.cumsum(episode_rewards) / np.arange(1, episodes + 1)

plt.figure(figsize=(10,5))
plt.plot(running_avg)

plt.title("Monte Carlo Estimated Average Reward")
plt.xlabel("Episodes")
plt.ylabel("Average Reward")

plt.grid(True)
plt.show()
