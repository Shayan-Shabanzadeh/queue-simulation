from Queue import Queue
from RandomGenerator import RandomLCGGenerator, RandomVariateGenerator
from constants import seed, a, c, m


class ComplaintsQueue(Queue):
    def __init__(self, name, output_unit, lambda_parameter, policy):
        super().__init__(name, output_unit, policy)
        self.lambda_parameter = lambda_parameter
        self.random_generator = RandomLCGGenerator(seed=seed, a=a, m=m, c=c)

    def generate_interarrival_time(self):
        u = self.random_generator.generate()

        interarrival_time = RandomVariateGenerator.randomExpVariateGenerator(u=u,
                                                                             lambda_parameter=self.lambda_parameter)

        # To be sure that interarrival time is positive
        interarrival_time = max(0, interarrival_time)
        return interarrival_time * self.output_unit

    def process_tasks(self):
        # Implement processing logic for this specific queue type
        pass
