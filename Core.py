import time
from abc import ABC, abstractmethod
from threading import Thread

from Task import Task


class Core(ABC):
    def __init__(self, name, switch_time_period, queue_lock):
        self.name = name
        self.switch_time_period = switch_time_period
        self.current_queue = None
        self.current_task = None
        self.queue_lock = queue_lock  # Add a lock for queue synchronization
        self.stop_thread = False  # Flag to signal the thread to stop

    def start_processing_thread(self):
        processing_thread = Thread(target=self._process_task)
        processing_thread.start()
        return processing_thread

    def stop_processing_thread(self):
        self.stop_thread = True

    def fetch_task(self) -> Task:
        with self.queue_lock:  # Acquire the lock before accessing the queue
            if self.current_queue:
                if not self.current_task:
                    return self.current_queue.fetch_task()
                else:
                    return self.current_task

    def _process_task(self):
        total_elapsed_time = 0
        switch_time = 0
        switch_time += total_elapsed_time
        while not self.stop_thread:
            current_task = self.fetch_task()

            if current_task:
                with self.queue_lock:  # Acquire the lock before modifying the queue
                    if current_task.service_time <= switch_time - total_elapsed_time:
                        # Release the lock before simulating processing time
                        self.queue_lock.release()

                        # Simulate running the entire task
                        run_time = current_task.service_time
                        total_elapsed_time += run_time
                        time.sleep(run_time)  # Simulating processing time

                        current_task.service_time = 0  # Task is completed

                        # Re-acquire the lock to modify the queue
                        self.queue_lock.acquire()
                        # Remove the task if completed
                        self.current_queue.remove_task(current_task)
                        self.queue_lock.release()

                        self.current_task = None
                    else:
                        # Release the lock before simulating processing time
                        self.queue_lock.release()

                        # Simulate running the task for the remaining time before switch
                        run_time = (switch_time - total_elapsed_time)
                        total_elapsed_time += run_time

                        time.sleep(run_time)  # Simulating processing time

                        # Re-acquire the lock to modify the queue
                        self.queue_lock.acquire()

                        current_task.service_time -= run_time
                        # Move the task to the end of the queue
                        self.current_queue.remove_task(current_task)
                        self.current_queue.add_task(current_task)
                        self.queue_lock.release()

                        self.current_task = None

                        # Update switch time and call switch_queue to change the queue
                        switch_time += self.switch_time_period
                        self.switch_queue()

    @abstractmethod
    def switch_queue(self):
        pass
