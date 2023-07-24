import multiprocessing

def consume_cpu():
    while True:
        pass

if __name__ == "__main__":
    # Get the number of available CPU cores
    num_cores = multiprocessing.cpu_count()

    # Create a list to hold the worker processes
    processes = []

    # Start a worker process for each core
    for _ in range(num_cores):
        process = multiprocessing.Process(target=consume_cpu)
        process.start()
        processes.append(process)

    try:
        # Keep the main process running while the worker processes consume CPU
        while True:
            continue
    except KeyboardInterrupt:
        # Terminate the worker processes when the main process receives a KeyboardInterrupt (Ctrl+C)
        for process in processes:
            process.terminate()
