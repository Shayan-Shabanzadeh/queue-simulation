from abc import ABC, abstractmethod


class Core(ABC):
    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time
        self.current_queue = None
        self.current_task = None
        self.remaining_processing_time = 0

    def assign_queue(self, queue):
        self.current_queue = queue

    def fetch_task(self):
        if self.current_queue:
            if not self.current_task:
                self.current_task = self.current_queue.fetch_task()
                if self.current_task:
                    self.remaining_processing_time = self.processing_time
            else:
                self.remaining_processing_time -= 1
                if self.remaining_processing_time == 0:
                    self.current_queue.remove_task(self.current_task)
                    self.current_task = None

    @abstractmethod
    def change_queue_condition(self):
        pass

    @abstractmethod
    def process_task(self):
        pass
