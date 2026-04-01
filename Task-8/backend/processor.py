from collections import deque
import numpy as np

WINDOW_SIZE = 10

class Processor:
    def __init__(self):
        self.values = deque(maxlen=WINDOW_SIZE)

    def process(self, new_value):
        self.values.append(new_value)

        avg = np.mean(self.values)
        std = np.std(self.values) if len(self.values) > 1 else 1

        z_score = (new_value - avg) / std

        return {
            "value": new_value,
            "moving_avg": round(avg, 2),
            "z_score": round(z_score, 2),
            "alert": bool(abs(z_score) > 2)
        }