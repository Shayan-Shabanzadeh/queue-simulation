from random import Random

from Queue import Queue
from constants import seed


class DocumentVerificationQueue(Queue):
    def __init__(self, name, output_unit, alpha, beta, policy):
        super().__init__(name, output_unit, policy)
        self.alpha = alpha
        self.beta = beta
        self.random_generator = Random()
        self.random_generator.seed(seed)

    def generate_interarrival_time(self):
        # Use RandomVariateGenerator to generate gamma-distributed random number
        random_number = self.random_generator.gammavariate(alpha=self.alpha, beta=self.beta)

        # To be sure that interarrival time is positive
        if random_number > 0:
            return random_number * self.output_unit
        else:
            return 0

    def process_tasks(self):
        # Implement processing logic for this specific queue type
        pass
