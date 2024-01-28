from Queue import Queue
from RandomGenerator import RandomLCGGenerator, RandomVariateGenerator
from constants import seed, a, c, m


class WritingQueue(Queue):
    def __init__(self, name, entry_mean, entry_variance, output_unit, policy):
        super().__init__(name, output_unit, policy)
        self.entry_mean = entry_mean
        self.entry_variance = entry_variance
        self.random_generator = RandomLCGGenerator(seed=seed, a=a, m=m, c=c)

    def generate_interarrival_time(self):
        u1 = self.random_generator.generate()
        u2 = self.random_generator.generate()

        random_number = RandomVariateGenerator.randomBoxMullerGenerator(u1=u1, u2=u2, mean=self.entry_mean,
                                                                        variance=self.entry_variance)
        # To be sure that interarrival time is positive
        interarrival_time = max(0, random_number)
        return interarrival_time * self.output_unit

    def process_tasks(self):
        # Implement processing logic for this specific queue type
        pass
