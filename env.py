from pydantic import BaseModel

class Observation(BaseModel):
    text: str

class Action(BaseModel):
    category: str
    priority: str

class SupportEnv:
    def __init__(self):
        self.data = [
            {"text": "Payment failed", "category": "Billing", "priority": "High"},
            {"text": "App crashes", "category": "Technical", "priority": "High"},
            {"text": "Change password", "category": "Account", "priority": "Low"},
        ]
        self.index = 0

    def reset(self):
        self.index = 0
        return Observation(text=self.data[self.index]["text"])

    def step(self, action: Action):
        expected = self.data[self.index]

        reward = 0.0
        if action.category == expected["category"]:
            reward += 0.5
        if action.priority == expected["priority"]:
            reward += 0.5

        self.index += 1
        done = self.index >= len(self.data)

        obs = None if done else Observation(text=self.data[self.index]["text"])

        return obs, reward, done, {}

    def state(self):
        return self.data[self.index]