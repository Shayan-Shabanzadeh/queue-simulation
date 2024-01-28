class Queue:
    def __init__(self, name, output_unit, policy):
        self.name = name
        self.output_unit = output_unit
        self.policy = policy
        self.tasks = []

    def generate_interarrival_time(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def generate_task(self, task_number):
        interarrival_time = self.generate_interarrival_time()
        task = {"TaskNumber": task_number, "InterarrivalTime": interarrival_time}
        self.tasks.append(task)
