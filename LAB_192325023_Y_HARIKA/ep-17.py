import random

# User Input
episodes = int(input("Enter number of episodes: "))
learning_rate = float(input("Enter learning rate (e.g., 0.1): "))
discount_factor = float(input("Enter discount factor (e.g., 0.9): "))
epsilon = float(input("Enter epsilon value (e.g., 0.2): "))

# MountainCar parameters
position = -0.5
velocity = 0.0

actions = [-1, 0, 1]   # Left, No Push, Right

# Q-Table
Q = {}

def get_state(pos, vel):
    p = round(pos, 1)
    v = round(vel, 2)
    return (p, v)

def get_q(state):
    if state not in Q:
        Q[state] = [0.0, 0.0, 0.0]
    return Q[state]

for ep in range(episodes):

    position = -0.5
    velocity = 0.0

    total_reward = 0

    for step in range(200):

        state = get_state(position, velocity)

        # Epsilon-Greedy
        if random.random() < epsilon:
            action = random.randint(0, 2)
        else:
            action = get_q(state).index(max(get_q(state)))

        force = actions[action]

        # MountainCar Physics
        velocity += 0.001 * force - 0.0025 * (3 * position)
        velocity = max(min(velocity, 0.07), -0.07)

        position += velocity
        position = max(min(position, 0.6), -1.2)

        if position == -1.2 and velocity < 0:
            velocity = 0

        if position >= 0.5:
            reward = 100
            done = True
        else:
            reward = -1
            done = False

        next_state = get_state(position, velocity)

        q = get_q(state)
        next_q = get_q(next_state)

        q[action] = q[action] + learning_rate * (
            reward + discount_factor * max(next_q) - q[action]
        )

        total_reward += reward

        if done:
            print("Episode", ep + 1, "Goal Reached in", step + 1, "steps")
            break

    if not done:
        print("Episode", ep + 1, "Goal Not Reached")

print("\nTraining Completed!")

print("\nSample Q-Table Entries:")
count = 0
for state in Q:
    print(state, ":", [round(x, 2) for x in Q[state]])
    count += 1
    if count == 10:
        break
