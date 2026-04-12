from fastapi import FastAPI
from env import Env, Action

app = FastAPI()

env = Env()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}

@app.post("/step")
def step(action: dict):
    act = Action(**action)
    obs, reward, done, _ = env.step(act)
    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }
