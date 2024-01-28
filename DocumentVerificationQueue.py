from Queue import Queue
from RandomGenerator import RandomVariateGenerator


class DocumentVerificationQueue(Queue):
    def __init__(self, name, output_unit,alpha, beta, policy):
        super().__init__(name, output_unit, policy)
        self.alpha = alpha
        self.beta = beta

    def generate_interarrival_time(self):
        # Use RandomVariateGenerator to generate gamma-distributed random number
        random_number = RandomVariateGenerator.randomGammaGenerator(self.alpha, self.beta)

        # To be sure that interarrival time is positive
        interarrival_time = max(0, random_number)
        return interarrival_time * self.output_unit

    def process_tasks(self):
        # Implement processing logic for this specific queue type
        pass
