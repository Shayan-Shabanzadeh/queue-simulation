import logging
import time
from abc import ABC, abstractmethod
from random import Random
from threading import Thread, Lock

from Task import Task

# Set up the logging format with color and an empty line
logging.basicConfig(format='\033[92m%(message)s\033[0m\n', level=logging.INFO)


class ColoredFormatter(logging.Formatter):
    COLORS = {
        'ERROR': '\033[91m',  # Red
        'WARNING': '\033[93m',  # Yellow
        'INFO': '\033[92m',  # Green
        'DEBUG': '\033[94m',  # Blue
        'CRITICAL': '\033[95m',  # Magenta
    }

    def format(self, record):
        log_message = super().format(record)
        return f"{self.COLORS.get(record.levelname, '')}{log_message}\033[0m"


# Add an additional handler with color to the root logger
colored_console_handler = logging.StreamHandler()
colored_console_handler.setFormatter(ColoredFormatter())
logging.getLogger('').addHandler(colored_console_handler)


class Core(ABC):

    _id_counter = 0

    def __init__(self, queues):
        Core._id_counter += 1
        self.id = Core._id_counter
        self.name = "Abstract core "
        self.switch_time_period = 0
        self.current_queue = None
        self.queues = queues
        self.current_task = None
        self.queue_locks = {queue: Lock() for queue in queues}  # Create a lock for each queue
        self.processing_thread = None
        self.stop_thread = False  # Flag to signal the thread to stop
        self.random_generator = Random()
        from constants import seed
        self.random_generator.seed(seed)

    def start_processing_thread(self):
        self.processing_thread = Thread(target=self._process_task)
        self.processing_thread.start()
        return self.processing_thread

    def stop_processing_thread(self):
        self.stop_thread = True

    def fetch_task(self) -> Task:
        with self.queue_locks[self.current_queue]:  # Acquire the lock for the current queue
            if self.current_queue:
                if not self.current_task:
                    return self.current_queue.fetch_task()
                else:
                    return self.current_task

    def _process_task(self):
        total_elapsed_time = 0
        switch_time = 0
        switch_time += self.switch_time_period
        while not self.stop_thread:
            current_task = self.fetch_task()
            if current_task and current_task.arrival_time > total_elapsed_time:
                if current_task.arrival_time < switch_time:
                    idle_time = current_task.arrival_time - total_elapsed_time
                else:
                    idle_time = switch_time - total_elapsed_time
                    switch_time += self.switch_time_period
                    self.switch_queue()
                logging.info(
                    f"{self.name} (ID: {self.id}) is idle for {idle_time} ms")
                # time.sleep(idle_time)
                total_elapsed_time += idle_time

            elif current_task and current_task.arrival_time <= total_elapsed_time:
                # Get the lock for the current queue or use a default lock
                lock = self.queue_locks.get(self.current_queue, Lock())

                with lock:
                    if current_task.service_time <= switch_time - total_elapsed_time:
                        # Task is eligible for processing
                        current_task.start_execution_time = total_elapsed_time
                        run_time = current_task.service_time
                        total_elapsed_time += run_time
                        time.sleep(run_time)  # Simulating processing time
                        current_task.end_execution_time = total_elapsed_time
                        current_task.time_in_the_queue = current_task.start_execution_time - current_task.arrival_time
                        logging.info(
                            f"{self.name} (ID: {self.id})"
                            f"Processing task {current_task} for {run_time} ms")
                        self.current_queue.remove_task(current_task)
                        self.current_task = None
                    else:
                        current_task.start_execution_time = total_elapsed_time
                        run_time = (switch_time - total_elapsed_time)
                        total_elapsed_time += run_time

                        time.sleep(run_time)  # Simulating processing time
                        current_task.time_in_the_queue = current_task.start_execution_time - current_task.arrival_time

                        current_task.service_time -= run_time
                        logging.info(
                            f"{self.name} (ID: {self.id})"
                            f"Processing task {current_task} for {run_time} ms")
                        # Move the task to the end of the queue
                        if self.current_queue:
                            self.current_queue.remove_task(self.current_task)
                            self.current_queue.add_task(current_task)

                        self.current_task = None

                        # Update switch time and call switch_queue to change the queue
                        switch_time += self.switch_time_period
                        self.switch_queue()

    @abstractmethod
    def switch_queue(self):
        pass
