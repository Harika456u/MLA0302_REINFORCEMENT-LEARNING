import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# True click probabilities
true_ctr = [0.10, 0.15, 0.25, 0.30, 0.20]

n_ads = len(true_ctr)
rounds = 1000

# --------------------------
# Epsilon Greedy
# --------------------------
epsilon = 0.1

counts = np.zeros(n_ads)
values = np.zeros(n_ads)
rewards_eps = []

for t in range(rounds):

    if np.random.rand() < epsilon:
        ad = np.random.randint(n_ads)
    else:
        ad = np.argmax(values)

    reward = np.random.rand() < true_ctr[ad]

    counts[ad] += 1

    values[ad] += (reward - values[ad]) / counts[ad]

    rewards_eps.append(reward)

# --------------------------
# UCB
# --------------------------

counts = np.zeros(n_ads)
values = np.zeros(n_ads)
rewards_ucb = []

for t in range(rounds):

    if t < n_ads:
        ad = t
    else:
        ucb = values + np.sqrt(2*np.log(t+1)/(counts+1e-5))
        ad = np.argmax(ucb)

    reward = np.random.rand() < true_ctr[ad]

    counts[ad]+=1
    values[ad]+= (reward-values[ad])/counts[ad]

    rewards_ucb.append(reward)

# --------------------------
# Thompson Sampling
# --------------------------

alpha=np.ones(n_ads)
beta=np.ones(n_ads)

rewards_ts=[]

for t in range(rounds):

    samples=np.random.beta(alpha,beta)

    ad=np.argmax(samples)

    reward=np.random.rand()<true_ctr[ad]

    if reward:
        alpha[ad]+=1
    else:
        beta[ad]+=1

    rewards_ts.append(reward)

# --------------------------
# Plot
# --------------------------

ctr_eps=np.cumsum(rewards_eps)/np.arange(1,rounds+1)
ctr_ucb=np.cumsum(rewards_ucb)/np.arange(1,rounds+1)
ctr_ts=np.cumsum(rewards_ts)/np.arange(1,rounds+1)

plt.figure(figsize=(10,6))
plt.plot(ctr_eps,label='Epsilon-Greedy')
plt.plot(ctr_ucb,label='UCB')
plt.plot(ctr_ts,label='Thompson Sampling')

plt.xlabel("Rounds")
plt.ylabel("Click Through Rate")
plt.title("Bandit Algorithm Comparison")
plt.legend()
plt.grid()
plt.show()

print("Final CTR")
print("Epsilon Greedy:",ctr_eps[-1])
print("UCB:",ctr_ucb[-1])
print("Thompson Sampling:",ctr_ts[-1])
