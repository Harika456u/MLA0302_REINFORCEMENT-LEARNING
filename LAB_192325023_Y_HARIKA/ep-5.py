# Value Iteration for Taxi Dispatching System

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

goal = tuple(map(int, input("Enter pickup location (row col): ").split()))

num_obstacles = int(input("Enter number of blocked locations: "))
obstacles = set()

print("Enter blocked locations (row col):")
for _ in range(num_obstacles):
    obstacles.add(tuple(map(int, input().split())))

gamma = float(input("Enter discount factor (e.g., 0.9): "))

# Initialize Value Function
V = [[0 for _ in range(cols)] for _ in range(rows)]

actions = [(-1,0),(1,0),(0,-1),(0,1)]
action_name = ["UP","DOWN","LEFT","RIGHT"]

# Value Iteration
while True:

    delta = 0

    for i in range(rows):
        for j in range(cols):

            if (i,j) == goal or (i,j) in obstacles:
                continue

            old = V[i][j]
            values = []

            for dx,dy in actions:

                ni = i + dx
                nj = j + dy

                if 0 <= ni < rows and 0 <= nj < cols:

                    if (ni,nj) in obstacles:
                        reward = -5
                        value = reward + gamma * V[i][j]
                    elif (ni,nj) == goal:
                        reward = 10
                        value = reward + gamma * V[ni][nj]
                    else:
                        reward = -1
                        value = reward + gamma * V[ni][nj]

                    values.append(value)

            V[i][j] = max(values)

            delta = max(delta, abs(old - V[i][j]))

    if delta < 0.001:
        break

# Display Value Function
print("\nOptimal State Values:\n")

for row in V:
    for value in row:
        print(f"{value:6.2f}", end=" ")
    print()

# Display Optimal Policy
print("\nOptimal Policy:\n")

for i in range(rows):

    for j in range(cols):

        if (i,j) == goal:
            print(" G ", end=" ")
            continue

        if (i,j) in obstacles:
            print(" X ", end=" ")
            continue

        best_action = 0
        best_value = -99999

        for k,(dx,dy) in enumerate(actions):

            ni = i + dx
            nj = j + dy

            if 0 <= ni < rows and 0 <= nj < cols:

                if (ni,nj) not in obstacles:

                    if V[ni][nj] > best_value:
                        best_value = V[ni][nj]
                        best_action = k

        print(action_name[best_action][0], end="  ")

    print()
