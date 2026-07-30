import numpy as np
import matplotlib.pyplot as plt

# Revenue probability for each price option
# (Higher value = more likely customer buys)
probabilities = [0.25, 0.40, 0.55, 0.70, 0.50]

n_arms = len(probabilities)
rounds = 1000


# -----------------------------
# Epsilon-Greedy
# -----------------------------
def epsilon_greedy(epsilon=0.1):

    counts = np.zeros(n_arms)
    rewards = np.zeros(n_arms)

    total_reward = 0
    revenue = []

    for i in range(rounds):

        if np.random.rand() < epsilon:
            arm = np.random.randint(n_arms)
        else:
            arm = np.argmax(rewards / (counts + 1e-5))

        reward = np.random.binomial(1, probabilities[arm])

        counts[arm] += 1
        rewards[arm] += reward

        total_reward += reward
        revenue.append(total_reward)

    return revenue


# -----------------------------
# UCB
# -----------------------------
def ucb():

    counts = np.zeros(n_arms)
    rewards = np.zeros(n_arms)

    revenue = []
    total_reward = 0

    for arm in range(n_arms):

        reward = np.random.binomial(1, probabilities[arm])

        counts[arm] += 1
        rewards[arm] += reward

        total_reward += reward
        revenue.append(total_reward)

    for t in range(n_arms, rounds):

        ucb_values = rewards/(counts+1e-5) + np.sqrt(2*np.log(t+1)/(counts+1e-5))

        arm = np.argmax(ucb_values)

        reward = np.random.binomial(1, probabilities[arm])

        counts[arm] += 1
        rewards[arm] += reward

        total_reward += reward
        revenue.append(total_reward)

    return revenue


# -----------------------------
# Thompson Sampling
# -----------------------------
def thompson():

    alpha = np.ones(n_arms)
    beta = np.ones(n_arms)

    revenue = []
    total_reward = 0

    for i in range(rounds):

        samples = np.random.beta(alpha, beta)

        arm = np.argmax(samples)

        reward = np.random.binomial(1, probabilities[arm])

        if reward == 1:
            alpha[arm] += 1
        else:
            beta[arm] += 1

        total_reward += reward
        revenue.append(total_reward)

    return revenue


# Run all algorithms
eps = epsilon_greedy()
ucb_reward = ucb()
ts = thompson()

# Plot comparison
plt.figure(figsize=(10,6))
plt.plot(eps, label="Epsilon-Greedy")
plt.plot(ucb_reward, label="UCB")
plt.plot(ts, label="Thompson Sampling")

plt.xlabel("Pricing Decisions")
plt.ylabel("Cumulative Revenue")
plt.title("Dynamic Pricing using Multi-Armed Bandit")
plt.legend()
plt.grid(True)

plt.show()

# Final Revenue
print("Final Revenue")
print("Epsilon-Greedy :", eps[-1])
print("UCB            :", ucb_reward[-1])
print("Thompson       :", ts[-1])
