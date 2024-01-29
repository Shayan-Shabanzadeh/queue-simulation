import uuid


class Task:
    def __init__(self, interarrival_time, service_time):
        self.interarrival_time = interarrival_time
        self.service_time = service_time
        self.id = uuid.uuid4()
        self.start_execution_time = 0
        self.end_execution_time = 0
        self.time_in_the_queue = 0
        self.arrival_time = 0

    def __str__(self):
        return f"Task ID: {self.id}, Interarrival Time: {self.interarrival_time}, " \
               f"Service Time: {self.service_time}, Arrival Time: {self.arrival_time}, " \
               f"Start Execution Time: {self.start_execution_time}, " \
               f"End Execution Time: {self.end_execution_time}, " \
               f"Time in the Queue: {self.time_in_the_queue}"
