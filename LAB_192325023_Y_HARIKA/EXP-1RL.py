import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random

class CleaningRobotEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.size = 5

        # Dirt cells (+1 reward)
        self.dirt = [(1,2), (2,4), (4,1)]

        # Obstacle cells (-1 reward)
        self.obstacles = [(1,1), (3,3)]

        # Actions:
        # 0=Up, 1=Down, 2=Left, 3=Right
        self.action_space = spaces.Discrete(4)

        # Robot position
        self.observation_space = spaces.Box(
            low=0,
            high=self.size-1,
            shape=(2,),
            dtype=np.int32
        )

        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.robot = [0,0]
        self.cleaned = set()

        return np.array(self.robot), {}

    def step(self, action):

        x, y = self.robot

        if action == 0:      # Up
            x -= 1
        elif action == 1:    # Down
            x += 1
        elif action == 2:    # Left
            y -= 1
        elif action == 3:    # Right
            y += 1

        x = max(0, min(4, x))
        y = max(0, min(4, y))

        self.robot = [x, y]

        reward = 0

        if (x, y) in self.obstacles:
            reward = -1

        if (x, y) in self.dirt and (x, y) not in self.cleaned:
            reward = 1
            self.cleaned.add((x, y))

        done = len(self.cleaned) == len(self.dirt)

        return np.array(self.robot), reward, done, False, {}

    def render(self):

        grid = np.full((5,5), ".")

        for d in self.dirt:
            if d not in self.cleaned:
                grid[d] = "D"

        for o in self.obstacles:
            grid[o] = "X"

        grid[self.robot[0], self.robot[1]] = "R"

        print(grid)
        print()


# -------------------------
# Random Policy Simulation
# -------------------------

env = CleaningRobotEnv()

state, _ = env.reset()

total_reward = 0

print("Initial Grid\n")
env.render()

done = False

while not done:

    action = env.action_space.sample()   # Random Policy

    state, reward, done, _, _ = env.step(action)

    total_reward += reward

    env.render()

print("Total Reward =", total_reward)
print("Cleaned Dirt =", len(env.cleaned))
