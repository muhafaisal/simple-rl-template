import random

class Environment:
    def __init__(self):
        self.steps_left = 10

    def get_observation(self) -> list[float]:
        return [0.0, 0.0, 0.0]
    
    def get_actions(self) -> list[int]:
        return [0, 1]
    
    def is_done(self) -> bool:
        return self.steps_left == 0
    
    def action(self, actionL: int) -> float:
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()