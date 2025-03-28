from gymnasium.envs.registration import register

register(
    id="gym_so100/modulab-v0",
    entry_point="gym_so100.tasks:Lift",
    max_episode_steps=300,
    kwargs={"obs_type": "state"},
)
