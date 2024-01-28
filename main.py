import matplotlib.pyplot as plt

from ComplaintsQueue import ComplaintsQueue
from ReviewRequestQueue import ReviewRequestQueue


def simulate_queues(queue_instances, simulation_time):
    all_tasks = []

    for queue_instance in queue_instances:
        task_times = []
        task_number = 1

        while sum(task_times) < simulation_time:
            interarrival_time = queue_instance.generate_interarrival_time()
            task_times.append(interarrival_time)
            task_number += 1

        all_tasks.append((queue_instance.name, task_times))

    return all_tasks


def plot_tasks(all_tasks):
    plt.figure(figsize=(12, 8))

    for queue_name, task_times in all_tasks:
        plt.hist(task_times, bins=30, alpha=0.5, label=queue_name)

    plt.title("Distribution of Interarrival Times for Different Queues")
    plt.xlabel("Interarrival Time (minutes)")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # LCG parameters are set in constants.py ./constants.py

    # number_of_cores = int(input("Enter number of cores for each type :"))
    simulation_time = float(input("Enter the simulation time in seconds: "))

    review_queue = ReviewRequestQueue(name="ReviewQueue", entry_mean=40, entry_variance=36, output_unit=1,
                                      policy="FIFO")
    complaints_queue = ComplaintsQueue(name="ComplaintsQueue", output_unit=1, lambda_parameter=0.5, policy="FIFO")

    all_queues = [review_queue, complaints_queue]
    all_tasks = simulate_queues(all_queues, simulation_time)

    plot_tasks(all_tasks)
