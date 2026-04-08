from env import Env

def main():
    env = Env()
    obs = env.reset()

    print("START")

    total = 0
    done = False

    while not done:
        action = {
            "category": "Billing",
            "priority": "High"
        }

        obs, reward, done, _ = env.step(type("Action", (), action))
        total += reward

    print("SCORE:", total)
    print("END")


if __name__ == "__main__":
    main()
