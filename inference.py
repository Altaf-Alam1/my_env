import os
from env import Env, Action
from openai import OpenAI

# Required env vars
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN", "dummy-token")

HF_TOKEN = os.getenv("HF_TOKEN", "dummy-token")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run():
    env = Env()
    obs = env.reset()

    step_count = 0
    rewards = []
    done = False
    success = False

    print(f"[START] task=support env=openenv model={MODEL_NAME}")

    while not done:
        step_count += 1

        action = Action(category="Billing", priority="High")

        obs, reward, done, _ = env.step(action)
        rewards.append(f"{reward:.2f}")

        print(f"[STEP] step={step_count} action=classify reward={reward:.2f} done={str(done).lower()} error=null")

    success = True if sum([float(r) for r in rewards]) > 0 else False

    print(f"[END] success={str(success).lower()} steps={step_count} rewards={','.join(rewards)}")


if __name__ == "__main__":
    run()
