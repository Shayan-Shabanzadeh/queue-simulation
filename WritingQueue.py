import numpy as np

from Queue import Queue


class WritingQueue(Queue):
    def __init__(self, entry_mean, entry_variance):
        super().__init__("WritingQueue", 1, "SPT", 30)
        self.entry_mean = entry_mean
        self.entry_variance = entry_variance

    def generate_interarrival_time(self):
        random_number = self.random_generator.normalvariate(self.entry_mean, np.sqrt(self.entry_variance))

        # To be sure that interarrival time is positive
        if random_number > 0:
            return random_number * self.output_unit
        else:
            return 0

