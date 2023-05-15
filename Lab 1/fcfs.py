# Define function for First Come First Served Scheduling Algorithm
def fcfs(processes):
    # Sort the processes by their arrival time
    sorted_processes = sorted(processes, key=lambda process: process['arrival_time'])

    # Initialize variables
    waiting_time = 0
    turnaround_time = 0
    current_time = 0

    # Run the algorithm
    for process in sorted_processes:
        waiting_time += current_time - process['arrival_time']
        turnaround_time += current_time + process['burst_time'] - process['arrival_time']
        current_time += process['burst_time']

    # Return the results
    return waiting_time, turnaround_time

processes = [{'process_id': 1, 'arrival_time': 0, 'burst_time': 10, 'priority': 3},    
             {'process_id': 2, 'arrival_time': 2, 'burst_time':5, 'priority':4}]

waiting_time, turnaround_time = fcfs(processes)
print("First Come First Served: Waiting Time = ",waiting_time)
print("First Come First Served: Turn Around Time = ",turnaround_time)

