import pandas as pd

# Read dataset
df = pd.read_csv("cleaning_robot_grid.csv")

# Grid size
ROWS = 5
COLS = 5

# Create reward grid
reward_grid = [[0 for j in range(COLS)] for i in range(ROWS)]

# Store cell type
cell_type = [["" for j in range(COLS)] for i in range(ROWS)]

# Fill grid
for index, row in df.iterrows():
    r = int(row["Row"])
    c = int(row["Col"])
    reward_grid[r][c] = int(row["Reward"])
    cell_type[r][c] = row["CellType"]

# Display Grid
print("\nReward Grid")
for row in reward_grid:
    print(row)

# Policies
print("\nChoose Policy")
print("1. Move Right then Down")
print("2. Move Down then Right")
print("3. Zig-Zag")

choice = int(input("Enter Policy (1-3): "))

r = 0
c = 0

visited = set()
total_reward = 0

print("\nRobot Navigation\n")

while True:

    if (r, c) not in visited:

        visited.add((r, c))

        reward = reward_grid[r][c]
        total_reward += reward

        print("State :", f"S{r}{c}")
        print("Position :", (r, c))
        print("Cell :", cell_type[r][c])
        print("Reward :", reward)
        print("--------------------------")

    # Goal reached
    if cell_type[r][c] == "Goal":
        break

    # Policy 1
    if choice == 1:

        if c < COLS - 1:
            c += 1
        elif r < ROWS - 1:
            r += 1

    # Policy 2
    elif choice == 2:

        if r < ROWS - 1:
            r += 1
        elif c < COLS - 1:
            c += 1

    # Policy 3
    else:

        if r % 2 == 0:

            if c < COLS - 1:
                c += 1
            else:
                r += 1

        else:

            if c > 0:
                c -= 1
            else:
                r += 1

print("\nGoal Reached Successfully!")

print("Total Reward =", total_reward)
print("Visited States =", len(visited))
