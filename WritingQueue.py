import numpy as np

from Queue import Queue


class WritingQueue(Queue):
    def __init__(self):
        super().__init__("WritingQueue", 1, "SPT", 30)
        self.entry_mean = 40
        self.entry_variance = 36

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

        # Find the task with the shortest processing time
        shortest_task = min(self.tasks, key=lambda task: task.service_time)

        # Remove the task from the queue
        self.tasks.remove(shortest_task)

        return shortest_task
