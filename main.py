import sys
import os

SCRIPT_DIR = f'module'
sys.path.append(os.path.dirname(SCRIPT_DIR))

from module.agent import Agent
from module.environment import Environment

if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)
    
    print('Total reward got: %.4f' % agent.total_reward)