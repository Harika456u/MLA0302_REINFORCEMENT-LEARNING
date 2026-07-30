import numpy as np
import matplotlib.pyplot as plt

# Grid size
rows = 4
cols = 5

start = (0, 0)
goal = (3, 4)

obstacles = [(1,1), (1,3), (3,0)]
traffic = [(0,2), (2,2)]

reward = 0
position = start

path = [position]

steps = 0
max_steps = 50

while position != goal and steps < max_steps:

    x, y = position

    # Greedy policy
    if x < goal[0]:
        new = (x+1, y)
    elif y < goal[1]:
        new = (x, y+1)
    else:
        break

    # Obstacle handling
    if new in obstacles:
        reward -= 20

        # Try moving right instead
        if y + 1 < cols:
            new = (x, y+1)

    # Boundary check
    if not (0 <= new[0] < rows and 0 <= new[1] < cols):
        reward -= 10
        break

    # Traffic signal
    if new in traffic:
        print("Stopped at Traffic Signal:", new)

    reward -= 1

    position = new
    path.append(position)

    steps += 1

if position == goal:
    reward += 100

print("Final Position:", position)
print("Total Reward:", reward)
print("Steps:", steps)

# Visualization

grid = np.zeros((rows, cols))

for obs in obstacles:
    grid[obs] = -1

for t in traffic:
    grid[t] = 2

grid[goal] = 5

plt.imshow(grid, cmap='coolwarm')

for p in path:
    plt.plot(p[1], p[0], 'ko')

plt.title("Autonomous Car Navigation")
plt.show()
