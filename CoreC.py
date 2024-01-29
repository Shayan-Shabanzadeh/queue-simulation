from ApplicationSubmissionQueue import ApplicationSubmissionQueue
from Core import Core
from DocumentVerificationQueue import DocumentVerificationQueue
from ReviewRequestQueue import ReviewRequestQueue


class CoreC(Core):
    def __init__(self, queues):
        super().__init__(queues=queues)

        self.application_submission_queue = None
        self.review_request_queue = None
        self.document_verification_queue = None

        for queue in queues:
            if isinstance(queue, ApplicationSubmissionQueue):
                self.application_submission_queue = queue
            elif isinstance(queue, ReviewRequestQueue):
                self.review_request_queue = queue
            elif isinstance(queue, DocumentVerificationQueue):
                self.document_verification_queue = queue
        if None in [self.application_submission_queue, self.review_request_queue, self.document_verification_queue]:
            raise ValueError("All required queues must be provided before creating CoreC")
        self.name = "Core type C"
        self.switch_time_period = 10
        self.current_queue = self.application_submission_queue

    def switch_queue(self):
        if self.current_queue == self.application_submission_queue:
            # Current queue is ApplicationSubmissionQueue
            probability_stay = 0.8
            probability_review = 0.1

            random_value = self.random_generator.random()

            if random_value < probability_stay:
                # Stay in the current queue
                return
            elif random_value < probability_stay + probability_review:
                # Switch to ReviewRequestQueue
                self.current_queue = self.review_request_queue
            else:
                # Switch to DocumentVerificationQueue
                self.current_queue = self.document_verification_queue

        elif self.current_queue == self.review_request_queue:
            # Current queue is ReviewRequestQueue
            probability_stay = 0.75
            probability_verification = 0.1

            random_value = self.random_generator.random()

            if random_value < probability_stay:
                # Stay in the current queue
                return
            elif random_value < probability_stay + probability_verification:
                # Switch to DocumentVerificationQueue
                self.current_queue = self.document_verification_queue
            else:
                # Switch to ApplicationSubmissionQueue
                self.current_queue = self.application_submission_queue

        elif self.current_queue == self.document_verification_queue:
            # Current queue is DocumentVerificationQueue
            probability_stay = 0.9
            probability_submission = 0.05

            random_value = self.random_generator.random()

            if random_value < probability_stay:
                # Stay in the current queue
                return
            elif random_value < probability_stay + probability_submission:
                # Switch to ApplicationSubmissionQueue
                self.current_queue = self.application_submission_queue
            else:
                # Switch to ReviewRequestQueue
                self.current_queue = self.review_request_queue

        self.queue_lock = self.current_queue
