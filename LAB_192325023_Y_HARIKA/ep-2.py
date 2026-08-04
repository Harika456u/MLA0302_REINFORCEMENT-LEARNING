# Policy Evaluation for Warehouse Robot

gamma = float(input("Enter discount factor (0-1): "))
theta = float(input("Enter convergence threshold (e.g., 0.001): "))

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

goal = tuple(map(int, input("Enter goal position (row col): ").split()))

n_items = int(input("Enter number of item locations: "))
items = []
print("Enter item positions (row col):")
for _ in range(n_items):
    items.append(tuple(map(int, input().split())))

n_obstacles = int(input("Enter number of obstacles: "))
obstacles = []
print("Enter obstacle positions (row col):")
for _ in range(n_obstacles):
    obstacles.append(tuple(map(int, input().split())))

# Initialize value function
V = [[0.0 for _ in range(cols)] for _ in range(rows)]

# Actions: Up, Down, Left, Right
actions = [(-1,0),(1,0),(0,-1),(0,1)]

while True:
    delta = 0

    for i in range(rows):
        for j in range(cols):

            if (i,j) == goal:
                continue

            old_value = V[i][j]
            value = 0

            for dx, dy in actions:

                ni = i + dx
                nj = j + dy

                if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                    ni, nj = i, j

                reward = 0

                if (ni, nj) in items:
                    reward = 2
                elif (ni, nj) == goal:
                    reward = 5
                elif (ni, nj) in obstacles:
                    reward = -2

                value += 0.25 * (reward + gamma * V[ni][nj])

            V[i][j] = value
            delta = max(delta, abs(old_value - value))

    if delta < theta:
        break

print("\nState Value Function:\n")

for row in V:
    for val in row:
        print(f"{val:7.2f}", end=" ")
    print()
