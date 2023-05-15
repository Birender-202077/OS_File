import queue

# Define function for Round Robin Scheduling Algorithm
def round_robin(processes, quantum):
    # Create a queue for the processes
    process_queue = queue.Queue()
    for process in processes:
        process_queue.put(process)

    # Initialize variables
    waiting_time = 0
    turnaround_time = 0
    current_time = 0

    # Run the algorithm
    while not process_queue.empty():
        process = process_queue.get()
        if process['burst_time'] > quantum:
            current_time += quantum
            process['burst_time'] -= quantum
            process_queue.put(process)
        else:
            current_time += process['burst_time']
            waiting_time += current_time - process['burst_time'] - process['arrival_time']
            turnaround_time += current_time - process['arrival_time']

    # Return the results
    return waiting_time, turnaround_time

processes = [{'process_id': 1, 'arrival_time': 0, 'burst_time': 10},    
             {'process_id': 2, 'arrival_time': 2, 'burst_time':5}]

quantum = 2
waiting_time, turnaround_time = round_robin(processes, quantum)
print("Round Robin - Waiting Time:", waiting_time)
print("Round Robin - Turnaround Time:", turnaround_time)

