import random
from game_environment.commons_env import HarvestCommonsEnv
from game_environment.constants import *

# init basic params
num_agents = 6
vision = 11
n_actions = 8
ep_length = 100
episode_path = "video_example"
wait_time = 0.2
# build environment
env = HarvestCommonsEnv(ascii_map=HARVEST_MAP, num_agents=num_agents, render=True)
env.reset()

# one episode with random movements and rendering
for t in range(ep_length):
    actions = {f"agent-{i}": random.randint(0, n_actions-1) for i in range(num_agents)}
    n_observation, n_rewards, n_done, _ = env.step(actions=actions)
    env.render(wait_time=wait_time)



