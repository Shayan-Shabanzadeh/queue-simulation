from random import Random

import numpy as np

from Queue import Queue


class ReviewRequestQueue(Queue):
    def __init__(self):
        super().__init__("ReviewRequestQueue", 1, "SIRO", 10)
        self.entry_mean = 15
        self.entry_variance = 36
        self.random_task_fetcher = Random()
        from constants import seed
        self.random_task_fetcher.seed(seed)

    def generate_interarrival_time(self):
        random_number = self.random_generator.normalvariate(self.entry_mean, np.sqrt(self.entry_variance))

        # To be sure that interarrival time is positive
        if random_number > 0:
            return random_number * self.output_unit
        else:
            return 0

    def fetch_task(self):
        if not self.tasks:
            return None  # No task in the queue

        # Fetch a task randomly from the queue (SIRO)
        random_index = self.random_task_fetcher.randint(0, len(self.tasks))
        task = self.tasks[random_index]

        return task
