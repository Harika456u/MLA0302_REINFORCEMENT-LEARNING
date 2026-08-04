import random

# User Input
num_contents = int(input("Enter number of content items: "))
num_users = int(input("Enter number of users: "))
epsilon = float(input("Enter epsilon value (e.g., 0.1): "))

# Initialize rewards and selection counts
rewards = [0] * num_contents
counts = [0] * num_contents

print("\nSimulating Content Recommendations...\n")

for user in range(num_users):

    # Epsilon-Greedy Selection
    if random.random() < epsilon:
        content = random.randint(0, num_contents - 1)
    else:
        avg_rewards = []

        for i in range(num_contents):
            if counts[i] == 0:
                avg_rewards.append(0)
            else:
                avg_rewards.append(rewards[i] / counts[i])

        content = avg_rewards.index(max(avg_rewards))

    # Simulate user feedback (Click = 1, No Click = 0)
    click = random.choice([0, 1])

    rewards[content] += click
    counts[content] += 1

print("\nRecommendation Results")

for i in range(num_contents):

    if counts[i] == 0:
        ctr = 0
    else:
        ctr = rewards[i] / counts[i]

    print(f"Content {i+1}")
    print("  Selected :", counts[i], "times")
    print("  Clicks   :", rewards[i])
    print("  CTR      :", round(ctr, 2))
    print()

best = 0
best_ctr = 0

for i in range(num_contents):
    if counts[i] != 0:
        ctr = rewards[i] / counts[i]
        if ctr > best_ctr:
            best_ctr = ctr
            best = i

print("Best Recommended Content:", best + 1)
print("Highest CTR:", round(best_ctr, 2))
