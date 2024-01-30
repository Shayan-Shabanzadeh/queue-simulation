import sys
import time

from Core import Core
from Queue import Queue
from constants import QUEUE_TYPES, CORE_TYPES


class Server:
    def __init__(self, n_cores_per_type: int, simulation_time):
        self.cores = []
        self.queues = []
        self.generate_queues()
        self.generate_cores(n_cores_per_type)
        self.simulation_time = simulation_time
        self.start_time = None

    def start_server(self):
        print("Started Server!")
        # Generate tasks for all queues
        for queue in self.queues:
            print("Creating tasks for", queue.name)
            queue.generate_tasks(self.simulation_time)
            # queue.generate_plot_interarrival_tasks()
            # queue.generate_linechart_interarrival_times()
            # queue.generate_linechart_service_times()

        # Start the processing threads for all cores
        for core in self.cores:
            print("Start Core:", core.name, "ID:", core.id)
            core.start_processing_thread()

        # Set the start time for the simulation
        self.start_time = time.time()
        end_time = self.start_time + self.simulation_time

        # Wait for the simulation_time to elapse
        while time.time() < end_time:
            time.sleep(1)  # Sleep for 1 second
            # TODO remove this

        # Stop the server after the specified simulation_time
        self.stop_server()
        sys.exit(0)

    def stop_server(self):
        # Stop the processing threads for all cores
        for core in self.cores:
            core.stop_processing_thread()

    def add_core(self, core: Core):
        self.cores.append(core)

    def add_queue(self, queue: Queue):
        self.queues.append(queue)

    def generate_cores(self, n_cores_per_type: int):
        for core_type in CORE_TYPES:
            for _ in range(n_cores_per_type):
                # Create a new instance of the specified core type
                new_core = core_type(queues=self.queues)
                self.add_core(new_core)

    def generate_queues(self):
        # call the queue types classes' constructors and append them to Server.queues
        for queue_type in QUEUE_TYPES:
            self.queues.append(queue_type())
