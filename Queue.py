from random import Random

from Task import Task
from constants import seed


class Queue:
    def __init__(self, name, output_unit, policy, service_mean):
        self.name = name
        self.output_unit = output_unit
        self.policy = policy
        self.tasks = []
        self.service_mean = service_mean
        self.random_generator = Random()
        self.random_generator.seed(seed)

    def generate_interarrival_time(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def generate_service_time(self):
        return self.random_generator.expovariate(1 / self.service_mean)

    def generate_task(self):
        interarrival_time = self.generate_interarrival_time()
        service_time = self.generate_service_time()
        task = Task(interarrival_time=interarrival_time, service_time=service_time)
        self.tasks.append(task)

    def fetch_task(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def generate_task(self, task_number):
        interarrival_time = self.generate_interarrival_time()
        task = {"TaskNumber": task_number, "InterarrivalTime": interarrival_time}
        self.tasks.append(task)
