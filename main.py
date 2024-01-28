import matplotlib.pyplot as plt

from ApplicationSubmissionQueue import ApplicationSubmissionQueue
from ComplaintsQueue import ComplaintsQueue
from DocumentVerificationQueue import DocumentVerificationQueue
from ReviewRequestQueue import ReviewRequestQueue
from WritingQueue import WritingQueue


def simulate_and_plot_queues(queue_instances, simulation_time):
    all_tasks = []

    for queue_instance in queue_instances:
        task_times = []
        task_number = 1

        while sum(task_times) < simulation_time:
            interarrival_time = queue_instance.generate_interarrival_time()
            task_times.append(interarrival_time)
            task_number += 1

        all_tasks.append((queue_instance.name, task_times))

    plot_interarrival_tasks(all_tasks)


def plot_interarrival_tasks(all_tasks):
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

    writing_queue = WritingQueue(entry_mean=40, entry_variance=36)
    complaints_queue = ComplaintsQueue(lambda_parameter=0.5)
    document_verification_queue = DocumentVerificationQueue(alpha=1, beta=2)
    application_submission_queue = ApplicationSubmissionQueue(lambda_parameter=0.06)
    review_queue = ReviewRequestQueue(entry_mean=15, entry_variance=36)
    # all_queues = [complaints_queue ,application_submission_queue]
    all_queues = [writing_queue, complaints_queue, document_verification_queue, application_submission_queue,
                  review_queue]
    simulate_and_plot_queues(all_queues, simulation_time)
