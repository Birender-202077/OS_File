# Define a function for Round Robin Scheduling algorithm
def round_robin(processes, quantum):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_time = [0] * n

    for i in range(n):
        remaining_time[i] = processes[i][1]

    t = 0
    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > quantum:
                    t += quantum
                    remaining_time[i] -= quantum
                else:
                    t += remaining_time[i]
                    waiting_time[i] = t - processes[i][1]
                    remaining_time[i] = 0
                    turnaround_time[i] = waiting_time[i] + processes[i][1]

        if done == True:
            break

    # Calculate average waiting time and turnaround time
    total_waiting_time = 0
    total_turnaround_time = 0
    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    # Print the results
    print("Round Robin Scheduling:")
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    print(f"Average waiting time = {avg_waiting_time:.2f}")
    print(f"Average turnaround time = {avg_turnaround_time:.2f}")

# Example usage
processes = [("P1", 10), ("P2", 5), ("P3", 8), ("P4", 7)]
quantum = 2
round_robin(processes, quantum)