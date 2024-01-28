from random import Random

import numpy as np

from Queue import Queue
from constants import seed


class WritingQueue(Queue):
    def __init__(self, name, entry_mean, entry_variance, output_unit, policy):
        super().__init__(name, output_unit, policy)
        self.entry_mean = entry_mean
        self.entry_variance = entry_variance
        self.random_generator = Random()
        self.random_generator.seed(seed)

    def generate_interarrival_time(self):
        random_number = self.random_generator.normalvariate(self.entry_mean, np.sqrt(self.entry_variance))

        # To be sure that interarrival time is positive
        if random_number > 0:
            return random_number * self.output_unit
        else:
            return 0

    def process_tasks(self):
        # Implement processing logic for this specific queue type
        pass