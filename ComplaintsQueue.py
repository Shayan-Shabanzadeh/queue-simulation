from Queue import Queue


class ComplaintsQueue(Queue):
    def __init__(self, lambda_parameter):
        super().__init__("ComplaintsQueue", 60, "FIFO", 25)
        self.lambda_parameter = lambda_parameter

    def generate_interarrival_time(self):
        random_number = self.random_generator.expovariate(lambd=self.lambda_parameter)

        # To be sure that interarrival time is positive
        if random_number > 0:
            return random_number * self.output_unit
        else:
            return 0

    def process_tasks(self):
        # Implement processing logic for this specific queue type
        pass
