import os
import pygame

num_cores = os.cpu_count()
print("Number of CPU cores:", num_cores)


import threading

def thread_function(thread_num):
    print(f"Thread {thread_num} started.")
    # Do some work here...
    print(f"Thread {thread_num} finished.")
    pygame.mixer.init()
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play()
    pygame.time.delay(600)
    pygame.mixer.music.stop()

# Number of threads you want to create
num_threads = 20

# Create and start the threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=thread_function, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
"""for thread in threads:
    thread.join()"""

print("All threads have finished.")
