def sjf(processes, preemptive=False):
    # Sort the processes by their burst time
    sorted_processes = sorted(processes, key=lambda process: process['burst_time'])

    # Initialize variables
    waiting_time = 0
    turnaround_time = 0
    current_time = 0

    # Run the algorithm
    for process in sorted_processes:
        if preemptive:
            # Find the process with the shortest remaining burst time
            shortest_process = min(sorted_processes, key=lambda p: p['burst_time'] if p['arrival_time'] <= current_time else float('inf'))
            if shortest_process['arrival_time'] > current_time:
                current_time = shortest_process['arrival_time']
            process = shortest_process

        waiting_time += current_time - process['arrival_time']
        turnaround_time += current_time + process['burst_time'] - process['arrival_time']
        current_time += process['burst_time']

    # Return the results
    return waiting_time, turnaround_time

processes = [{'process_id': 1, 'arrival_time': 0, 'burst_time': 10, 'priority': 3},    
             {'process_id': 2, 'arrival_time': 2, 'burst_time':5, 'priority':4}]

waiting_time, turnaround_time = sjf(processes)
print("Shortest Job First - Waiting Time:", waiting_time)
print("Shortest Job First - Turnaround Time:", turnaround_time)