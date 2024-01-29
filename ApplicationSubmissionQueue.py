from Queue import Queue


class ApplicationSubmissionQueue(Queue):
    def __init__(self):
        super().__init__("ApplicationSubmissionQueue", 1, "SPT", 5)
        self.lambda_parameter = 0.06

    def generate_interarrival_time(self):
        random_number = self.random_generator.expovariate(lambd=self.lambda_parameter)

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

        return shortest_task
