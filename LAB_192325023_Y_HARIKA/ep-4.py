import random

# User Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

goal = tuple(map(int, input("Enter goal position (row col): ").split()))

num_obstacles = int(input("Enter number of obstacles: "))
obstacles = set()

print("Enter obstacle positions (row col):")
for _ in range(num_obstacles):
    obstacles.add(tuple(map(int, input().split())))

gamma = float(input("Enter discount factor (e.g., 0.9): "))

actions = [(-1,0),(1,0),(0,-1),(0,1)]
action_name = ["UP","DOWN","LEFT","RIGHT"]

# Initialize Value Function and Policy
V = {(i,j):0 for i in range(rows) for j in range(cols)}
policy = {(i,j):random.randint(0,3) for i in range(rows) for j in range(cols)}

stable = False

while not stable:

    # Policy Evaluation
    while True:
        delta = 0

        for i in range(rows):
            for j in range(cols):

                state = (i,j)

                if state == goal or state in obstacles:
                    continue

                old_value = V[state]

                action = policy[state]
                dx, dy = actions[action]

                ni = max(0, min(rows-1, i+dx))
                nj = max(0, min(cols-1, j+dy))

                next_state = (ni,nj)

                if next_state in obstacles:
                    next_state = state

                reward = 10 if next_state == goal else -1

                V[state] = reward + gamma * V[next_state]

                delta = max(delta, abs(old_value - V[state]))

        if delta < 0.001:
            break

    # Policy Improvement
    stable = True

    for i in range(rows):
        for j in range(cols):

            state = (i,j)

            if state == goal or state in obstacles:
                continue

            old_action = policy[state]

            best_action = old_action
            best_value = float("-inf")

            for a in range(4):

                dx, dy = actions[a]

                ni = max(0, min(rows-1, i+dx))
                nj = max(0, min(cols-1, j+dy))

                next_state = (ni,nj)

                if next_state in obstacles:
                    next_state = state

                reward = 10 if next_state == goal else -1

                value = reward + gamma * V[next_state]

                if value > best_value:
                    best_value = value
                    best_action = a

            policy[state] = best_action

            if old_action != best_action:
                stable = False

print("\nOptimal Policy:")

for i in range(rows):
    for j in range(cols):

        state = (i,j)

        if state == goal:
            print(" G ", end=" ")
        elif state in obstacles:
            print(" X ", end=" ")
        else:
            print(action_name[policy[state]][0], end="  ")
    print()

print("\nState Values:")

for i in range(rows):
    for j in range(cols):
        print(f"{V[(i,j)]:6.2f}", end=" ")
    print()
