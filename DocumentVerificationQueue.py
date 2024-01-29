from Queue import Queue


class DocumentVerificationQueue(Queue):
    def __init__(self):
        super().__init__("DocumentVerificationQueue", 60, "FIFO", 10)
        self.alpha = 1
        self.beta = 2

    def generate_interarrival_time(self):
        # Use RandomVariateGenerator to generate gamma-distributed random number
        random_number = self.random_generator.gammavariate(alpha=self.alpha, beta=self.beta)

        # To be sure that interarrival time is positive
        if random_number > 0:
            return random_number * self.output_unit
        else:
            return 0

    def fetch_task(self):
        if not self.tasks:
            return None  # No task in the queue

        # Fetch the task at the front of the queue (FIFO)
        task = self.tasks[0]

        return task

