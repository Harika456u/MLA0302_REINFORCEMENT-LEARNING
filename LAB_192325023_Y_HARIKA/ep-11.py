import random

# User Input
episodes = int(input("Enter number of episodes: "))
initial_price = float(input("Enter initial stock price: "))

actions = ["Buy", "Sell", "Hold"]

# Q-Tables (Online and Target)
Q_online = [[0 for _ in range(3)] for _ in range(3)]
Q_target = [[0 for _ in range(3)] for _ in range(3)]

alpha = 0.1
gamma = 0.9
epsilon = 0.2

total_profit = 0

for ep in range(episodes):

    state = random.randint(0, 2)
    stock_price = initial_price
    holding = False
    buy_price = 0

    print("\nEpisode", ep + 1)

    for step in range(10):

        # Epsilon-Greedy Action Selection
        if random.random() < epsilon:
            action = random.randint(0, 2)
        else:
            action = Q_online[state].index(max(Q_online[state]))

        reward = 0

        if action == 0:  # Buy
            if not holding:
                holding = True
                buy_price = stock_price
                print("Bought at", stock_price)

        elif action == 1:  # Sell
            if holding:
                reward = stock_price - buy_price
                total_profit += reward
                holding = False
                print("Sold at", stock_price, "Profit:", reward)

        else:  # Hold
            reward = 0
            print("Holding...")

        # Simulate stock price change
        stock_price += random.randint(-5, 5)

        next_state = random.randint(0, 2)

        # Double DQN Update
        best_action = Q_online[next_state].index(max(Q_online[next_state]))
        target = reward + gamma * Q_target[next_state][best_action]

        Q_online[state][action] += alpha * (
            target - Q_online[state][action]
        )

        state = next_state

    # Update Target Network
    Q_target = [row[:] for row in Q_online]

print("\nTraining Completed")

print("Total Profit:", round(total_profit, 2))

print("\nOnline Q Table")
for row in Q_online:
    print(row)

print("\nTarget Q Table")
for row in Q_target:
    print(row)
