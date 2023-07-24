import psutil
"""
IDLE_PRIORITY_CLASS: 64
BELOW_NORMAL_PRIORITY_CLASS: 16384
NORMAL_PRIORITY_CLASS: 32
ABOVE_NORMAL_PRIORITY_CLASS: 32768
HIGH_PRIORITY_CLASS: 128
REALTIME_PRIORITY_CLASS: 256
"""
class prioritysetting():

    @staticmethod
    def set_process_priority(pid, priority):
        process = psutil.Process(pid)

        try:
            # Get the current process priority range for Windows (may vary on different systems)
            priority_range = range(psutil.NORMAL_PRIORITY_CLASS - 2, psutil.REALTIME_PRIORITY_CLASS + 1)

            # Check if the provided priority is within the valid range
            if priority in priority_range:
                # Set the process priority
                process.nice(priority)
                return True
            else:
                print("Error: Invalid priority value. Please choose a priority within the range:", priority_range)

        except psutil.NoSuchProcess:
            print("Error: No such process with PID:", pid)
        except psutil.AccessDenied:
            print("Error: Access denied. You may need to run the script as an administrator.")

        return False