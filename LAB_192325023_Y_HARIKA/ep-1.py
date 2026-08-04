import random

# Directions
moves = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

# Check valid position
def valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

# User Input
n = int(input("Enter grid size: "))

grid = [["." for _ in range(n)] for _ in range(n)]

dirt = set()
d = int(input("Enter number of dirt cells: "))
print("Enter dirt positions (row column):")
for _ in range(d):
    r, c = map(int, input().split())
    if valid(r, c, n):
        dirt.add((r, c))

obstacles = set()
o = int(input("Enter number of obstacle cells: "))
print("Enter obstacle positions (row column):")
for _ in range(o):
    r, c = map(int, input().split())
    if valid(r, c, n):
        obstacles.add((r, c))

print("\nChoose Policy")
print("1. Random Policy")
print("2. Greedy Policy")
choice = int(input("Enter choice: "))

robot = [0, 0]
reward = 0
path = [(0, 0)]

max_steps = n * n * 2

for _ in range(max_steps):

    if not dirt:
        break

    if choice == 1:
        possible = []
        for dx, dy in moves.values():
            nx, ny = robot[0] + dx, robot[1] + dy
            if valid(nx, ny, n):
                possible.append((nx, ny))
        robot = list(random.choice(possible))

    elif choice == 2:
        target = min(
            dirt,
            key=lambda p: abs(robot[0] - p[0]) + abs(robot[1] - p[1])
        )

        x, y = robot

        if target[0] > x:
            x += 1
        elif target[0] < x:
            x -= 1
        elif target[1] > y:
            y += 1
        elif target[1] < y:
            y -= 1

        if valid(x, y, n):
            robot = [x, y]

    pos = tuple(robot)
    path.append(pos)

    if pos in dirt:
        reward += 1
        dirt.remove(pos)
        print("Cleaned Dirt at", pos)

    elif pos in obstacles:
        reward -= 1
        print("Hit Obstacle at", pos)

print("\nRobot Path:")
print(path)

print("\nTotal Reward:", reward)
print("Remaining Dirt:", len(dirt))

if len(dirt) == 0:
    print("Cleaning Completed!")
else:
    print("Cleaning Incomplete!")
