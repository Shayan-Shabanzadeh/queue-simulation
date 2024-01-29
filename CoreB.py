from ApplicationSubmissionQueue import ApplicationSubmissionQueue
from Core import Core
from ReviewRequestQueue import ReviewRequestQueue


class CoreB(Core):
    def __init__(self, queues):
        super().__init__(queues=queues)
        self.application_submission_queue = None
        self.review_request_queue = None

        for queue in queues:
            if isinstance(queue, ApplicationSubmissionQueue):
                self.application_submission_queue = queue
            elif isinstance(queue, ReviewRequestQueue):
                self.review_request_queue = queue

        if None in [self.application_submission_queue, self.review_request_queue]:
            raise ValueError("All required queues must be provided before creating CoreB")
        self.name = "Core type B"
        self.switch_time_period = 7
        self.current_queue = self.application_submission_queue

    def switch_queue(self):
        if self.current_queue == self.application_submission_queue:
            # Current queue is WritingQueue
            probability_stay = 0.85
            if self.random_generator.random() < probability_stay:
                # Stay in the current queue
                return
            else:
                # Switch to ComplaintsQueue
                self.current_queue = self.review_request_queue
        elif self.current_queue == self.review_request_queue:
            # Current queue is ComplaintsQueue
            probability_stay = 0.95
            if self.random_generator.random() < probability_stay:
                # Stay in the current queue
                return
            else:
                # Switch to WritingQueue
                self.current_queue = self.application_submission_queue
        self.queue_lock = self.current_queue
