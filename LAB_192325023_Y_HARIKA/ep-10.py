import random

# User Input
num_agents = int(input("Enter number of customer service representatives: "))
num_calls = int(input("Enter number of incoming calls: "))
episodes = int(input("Enter number of simulation episodes: "))

# Initialize Value Function
V = [0.0] * num_agents
returns = [[] for _ in range(num_agents)]

for ep in range(episodes):

    episode = []

    for call in range(num_calls):

        # Randomly assign an agent
        agent = random.randint(0, num_agents - 1)

        # Simulated handling time (2 to 10 minutes)
        handling_time = random.randint(2, 10)

        # Reward (less handling time = higher reward)
        reward = 10 - handling_time

        episode.append((agent, reward))

    # Monte Carlo Value Estimation
    G = 0

    for agent, reward in reversed(episode):

        G += reward

        returns[agent].append(G)

        V[agent] = sum(returns[agent]) / len(returns[agent])

print("\nEstimated Value Function")

for i in range(num_agents):
    print(f"Representative {i+1}: {V[i]:.2f}")

best_agent = V.index(max(V))

print("\nBest Representative:", best_agent + 1)
print("Highest Estimated Value:", round(max(V), 2))
