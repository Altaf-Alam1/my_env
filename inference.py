import os
from env import Env, Action
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "")
HF_TOKEN = os.getenv("HF_TOKEN", "")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run():
    env = Env()
    obs = env.reset()
    total_reward = 0

    while True:
        action = Action(category="Billing", priority="High")

        obs, reward, done, _ = env.step(action)
        total_reward += reward

        if done:
            break

    return total_reward


if __name__ == "__main__":
    print("START")
    score = run()
    print("SCORE:", score)
    print("END")
