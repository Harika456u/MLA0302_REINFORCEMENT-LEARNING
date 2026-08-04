import random

# User Input
num_customers = int(input("Enter number of customers: "))
episodes = int(input("Enter number of episodes: "))
alpha = float(input("Enter learning rate (e.g., 0.1): "))

# States
states = ["Active", "At Risk", "Churned"]

# Initialize Value Function
V = {state: 0.0 for state in states}

for ep in range(episodes):

    episode = []

    for i in range(num_customers):

        state = random.choice(states)

        # Reward based on customer status
        if state == "Active":
            reward = 10
        elif state == "At Risk":
            reward = -5
        else:
            reward = -10

        episode.append((state, reward))

    # Monte Carlo Policy Evaluation
    G = 0

    for state, reward in reversed(episode):
        G += reward
        V[state] = V[state] + alpha * (G - V[state])

print("\nTraining Completed!")

print("\nEstimated State Values")

for state in states:
    print(f"{state} : {V[state]:.2f}")

print("\nCustomer Churn Prediction")

for state in states:
    if V[state] > 5:
        print(f"{state} -> Low Churn Risk")
    elif V[state] > -5:
        print(f"{state} -> Medium Churn Risk")
    else:
        print(f"{state} -> High Churn Risk")
