from Server import Server


if __name__ == "__main__":
    number_of_cores = int(input("Enter number of cores for each type: "))
    simulation_time = float(input("Enter the simulation time in seconds: "))
    server = Server(number_of_cores, simulation_time)
    server.start_server()
    # server.queues[1].generate_tasks(simulation_time)
    # server.queues[1].generate_plot_interarrival_tasks()


