from random import Random
import matplotlib
from matplotlib import pyplot as plt
from Task import Task
matplotlib.use('TkAgg')


class Queue:
    def __init__(self, name, output_unit, policy, service_mean):
        self.name = name  # Queue type name [Writing, Complaint, Verification, Application, Review]
        self.output_unit = output_unit  # Queue type Distribution output type sec/60sec
        self.policy = policy  # Queue type policy --> [SPT, FIFO, SIRO]
        self.tasks = []  # Tasks queue
        self.service_mean = service_mean  # Service-time distribution (exponential) mean (1 / lambda parameter)
        self.random_generator = Random()
        from constants import seed
        self.random_generator.seed(seed)

    def generate_interarrival_time(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def generate_service_time(self):
        return self.random_generator.expovariate(1 / self.service_mean)

    def generate_task(self, task_arrival_time):
        interarrival_time = self.generate_interarrival_time()
        service_time = self.generate_service_time()
        task = Task(arrival_time=task_arrival_time, interarrival_time=interarrival_time, service_time=service_time)
        return task

    def generate_tasks(self, simulation_time):
        task_arrival_time = 0
        while task_arrival_time < simulation_time:
            task = self.generate_task(task_arrival_time)
            task_arrival_time += task.interarrival_time
            task.arrival_time = task_arrival_time
            self.tasks.append(task)

    def remove_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print(f"Task {task} not found in the queue {self.name}")

    def add_task(self, task: Task):
        self.tasks.append(task)

    def generate_plot_interarrival_tasks(self, plot=None):
        if plot is None:
            plot = plt

        plot.figure(figsize=(8, 6))
        interarrival_times = [task.interarrival_time for task in self.tasks]

        plot.hist(interarrival_times, bins=30, alpha=0.5, label=self.name)
        plot.title("Distribution of Interarrival Times for " + self.name)
        plot.xlabel("Interarrival Time (minutes)")
        plot.ylabel("Frequency")
        plot.legend()
        plot.show()

    def generate_linechart_interarrival_times(self):
        arrival_times = [task.arrival_time for task in self.tasks]
        interarrival_times = [task.interarrival_time for task in self.tasks]
        print("Total Customers for " + self.name + ": " + str(len(interarrival_times)))

        # Plotting a line chart
        plt.figure(figsize=(12, 5))
        plt.plot(arrival_times, interarrival_times, marker='o', linestyle='-', markersize=1)
        plt.title('Interarrival Times in' + self.name)
        plt.xlabel('Arrival Time')
        plt.ylabel('Interarrival Time')

        plt.grid(True)
        plt.show()


def fetch_task(self):
    raise NotImplementedError("Subclasses must implement this method.")
