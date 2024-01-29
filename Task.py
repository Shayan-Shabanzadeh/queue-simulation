import uuid


class Task:
    def __init__(self, interarrival_time, service_time):
        self.interarrival_time = interarrival_time
        self.service_time = service_time
        self.id = uuid.uuid4()
