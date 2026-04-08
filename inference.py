from env import SupportEnv, Action

env = SupportEnv()
obs = env.reset()

total = 0

while True:
    action = Action(category="Billing", priority="High")

    obs, reward, done, _ = env.step(action)
    total += reward

    if done:
        break

print("Score:", total)
