from ComplaintsQueue import ComplaintsQueue
from Core import Core
from WritingQueue import WritingQueue


class CoreA(Core):
    def __init__(self, queues):
        super().__init__(queues=queues)

        self.writing_queue = None
        self.complaints_queue = None

        for queue in queues:
            if isinstance(queue, WritingQueue):
                self.writing_queue = queue
            elif isinstance(queue, ComplaintsQueue):
                self.complaints_queue = queue

        if None in [self.writing_queue, self.complaints_queue]:
            raise ValueError("All required queues must be provided before creating CoreA")
        self.name = "Core type A"
        self.switch_time_period = 5
        self.current_queue = self.writing_queue

    def switch_queue(self):
        if self.current_queue == self.writing_queue:
            # Current queue is WritingQueue
            probability_stay = 0.8
            if self.random_generator.random() < probability_stay:
                # Stay in the current queue
                return
            else:
                # Switch to ComplaintsQueue
                self.current_queue = self.complaints_queue
        elif self.current_queue == self.complaints_queue:
            # Current queue is ComplaintsQueue
            probability_stay = 0.9
            if self.random_generator.random() < probability_stay:
                # Stay in the current queue
                return
            else:
                # Switch to WritingQueue
                self.current_queue = self.writing_queue
