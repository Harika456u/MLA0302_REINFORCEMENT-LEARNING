import random
import math

# User Input
num_ads = int(input("Enter number of advertisements: "))
rounds = int(input("Enter number of rounds: "))
epsilon = float(input("Enter epsilon value (e.g., 0.1): "))

# True click probabilities (randomly generated)
true_prob = [random.uniform(0.1, 0.9) for _ in range(num_ads)]

# ---------------- Epsilon Greedy ----------------
eg_rewards = [0] * num_ads
eg_counts = [0] * num_ads
eg_total = 0

for t in range(rounds):

    if random.random() < epsilon:
        ad = random.randint(0, num_ads - 1)
    else:
        avg = [
            eg_rewards[i] / eg_counts[i] if eg_counts[i] > 0 else 0
            for i in range(num_ads)
        ]
        ad = avg.index(max(avg))

    reward = 1 if random.random() < true_prob[ad] else 0
    eg_rewards[ad] += reward
    eg_counts[ad] += 1
    eg_total += reward

# ---------------- UCB ----------------
ucb_rewards = [0] * num_ads
ucb_counts = [0] * num_ads
ucb_total = 0

for t in range(rounds):

    if 0 in ucb_counts:
        ad = ucb_counts.index(0)
    else:
        ucb = []

        for i in range(num_ads):
            avg = ucb_rewards[i] / ucb_counts[i]
            bonus = math.sqrt((2 * math.log(t + 1)) / ucb_counts[i])
            ucb.append(avg + bonus)

        ad = ucb.index(max(ucb))

    reward = 1 if random.random() < true_prob[ad] else 0
    ucb_rewards[ad] += reward
    ucb_counts[ad] += 1
    ucb_total += reward

# ---------------- Thompson Sampling ----------------
ts_success = [1] * num_ads
ts_failure = [1] * num_ads
ts_total = 0

for t in range(rounds):

    samples = [
        random.betavariate(ts_success[i], ts_failure[i])
        for i in range(num_ads)
    ]

    ad = samples.index(max(samples))

    reward = 1 if random.random() < true_prob[ad] else 0

    if reward == 1:
        ts_success[ad] += 1
    else:
        ts_failure[ad] += 1

    ts_total += reward

# ---------------- Results ----------------
print("\nSimulation Completed!\n")

print("Epsilon-Greedy Total Clicks :", eg_total)
print("UCB Total Clicks            :", ucb_total)
print("Thompson Sampling Clicks    :", ts_total)

best = max(eg_total, ucb_total, ts_total)

if best == eg_total:
    print("\nBest Algorithm : Epsilon-Greedy")
elif best == ucb_total:
    print("\nBest Algorithm : UCB")
else:
    print("\nBest Algorithm : Thompson Sampling")
