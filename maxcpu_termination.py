import multiprocessing
import os
import signal
import time
import bigMatrixMultiplication
import prioritysetting

def consume_cpu(terminate_signal):

    pidSetting = prioritysetting.prioritysetting()

    print("pid is: ",int(os.getpid()))
    pidSetting.set_process_priority(int(os.getpid()), 256)

    while not terminate_signal.poll():
        matmul = bigMatrixMultiplication.bigmatmul()
        rows_matrix1 = 2500
        cols_matrix1 = 2500
        rows_matrix2 = 2500
        cols_matrix2 = 2500
        # Call the function to perform matrix multiplication
        result_matrix = matmul.large_matrix_multiplication(rows_matrix1, cols_matrix1, rows_matrix2, cols_matrix2)
        
    print(f"Process {os.getpid()} received termination signal and is exiting.")

def send_terminate_signal(pipe, num_cores):
    print("Sending termination signal to all processes...")
    for _ in range(num_cores):
        pipe.send(True)

if __name__ == "__main__":
    # Get the number of available CPU cores
    num_cores = multiprocessing.cpu_count()

    # Create a pipe for communication between the main process and worker processes
    parent_pipe, child_pipe = multiprocessing.Pipe()

    # Create a list to hold the worker processes
    processes = []

    # Start a worker process for each core
    for _ in range(num_cores):
        process = multiprocessing.Process(target=consume_cpu, args=(child_pipe,))
        process.start()
        processes.append(process)

    try:
        # Wait for some time before sending the termination signal (you can adjust the sleep time)
        time_to_run = 60  # seconds
        print(f"Waiting for {time_to_run} seconds before sending termination signal...")
        time.sleep(time_to_run)
        multiprocessing.Process(target=send_terminate_signal, args=(parent_pipe, num_cores)).start()

        # Join all the processes to wait for them to finish
        for process in processes:
            process.join()

    except KeyboardInterrupt:
        # Terminate the worker processes when the main process receives a KeyboardInterrupt (Ctrl+C)
        for process in processes:
            process.terminate()

    # Join all the processes to wait for them to finish
    for process in processes:
        process.join()
