import gym
from stable_baselines3 import SAC, PPO, TD3, A2C
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.logger import configure

import __init__

if __name__ == "__main__":

    # setup parameters

    env_name = "DoorOpenEnv-v1"  # should be  DoorOpenEnv-v1
    # env = gym.make(env_name)  # regular env (SAC)
    env = make_vec_env(env_name, n_envs=8)  # vector env (PPO)
    eval_env = gym.make(env_name)  # regular env for evaluation
    logger = configure("../outcomes/tensorboard_log/open_door/ppo", ["stdout", "tensorboard"])
    model_path = "../outcomes/models/ppo_open_door"

    # print("begin checking env")
    # check_env(env)
    # print("finished checking env")

    model = PPO("MlpPolicy", env=env, verbose=1)
    # model = SAC.load(path=model_path, env=env, force_reset=True)
    model.set_logger(logger)
    model.learn(total_timesteps=1_000_000, eval_env=eval_env, eval_freq=10_000, n_eval_episodes=5,
                eval_log_path="../outcomes/evaluation/open_door/ppo")
    model.save(model_path)

