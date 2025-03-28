import gymnasium as gym
import gym_so100

env = gym.make("gym_so100/modulab-v0", render_mode="human")
observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    image = env.render()

    if terminated or truncated:
        observation, info = env.reset()

env.close()
