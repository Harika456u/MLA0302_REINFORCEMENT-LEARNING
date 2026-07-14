import gymnasium as gym
from gymnasium import spaces
import numpy as np

class WarehouseEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.size = 5

        self.action_space = spaces.Discrete(4)

        self.observation_space = spaces.Discrete(self.size * self.size)

        self.goal = (4,4)

        self.item = (2,2)

        self.obstacles = [(1,1), (3,2)]

    def get_next_state(self, state, action):

        x = state // self.size
        y = state % self.size

        if action == 0:      # Up
            x -= 1
        elif action == 1:    # Down
            x += 1
        elif action == 2:    # Left
            y -= 1
        elif action == 3:    # Right
            y += 1

        x = max(0, min(self.size-1, x))
        y = max(0, min(self.size-1, y))

        reward = 0

        if (x,y) in self.obstacles:
            reward = -2

        elif (x,y) == self.item:
            reward = 2

        elif (x,y) == self.goal:
            reward = 5

        next_state = x*self.size + y

        return next_state, reward


env = WarehouseEnv()

gamma = 0.9

theta = 0.001

num_states = env.observation_space.n

num_actions = env.action_space.n

V = np.zeros(num_states)

# Random Policy
policy = np.ones((num_states, num_actions)) / num_actions


while True:

    delta = 0

    for s in range(num_states):

        v = V[s]

        new_v = 0

        for a in range(num_actions):

            next_state, reward = env.get_next_state(s, a)

            new_v += policy[s][a] * (reward + gamma * V[next_state])

        V[s] = new_v

        delta = max(delta, abs(v - new_v))

    if delta < theta:
        break


print("State Value Function:\n")

print(V.reshape((5,5)))
