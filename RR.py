n = int(input("Enter number of processes: "))
processes = []
arrival_time = []
burst_time = []
for i in range(n):
    at = int(input(f"Enter Arrival Time for Process {i+1}: "))
    bt = int(input(f"Enter Burst Time for Process {i+1}: "))
    processes.append(i + 1)
    arrival_time.append(at)
    burst_time.append(bt)
quantum = int(input("Enter Time Quantum: "))
remaining_bt = burst_time.copy()
wt = [0] * n
tat = [0] * n
time = 0
while True:
    done = True
    for i in range(n):
        if arrival_time[i] <= time and remaining_bt[i] > 0:
            done = False
            if remaining_bt[i] > quantum:
                time += quantum
                remaining_bt[i] -= quantum
            else:
                time += remaining_bt[i]
                wt[i] = time - arrival_time[i] - burst_time[i]
                remaining_bt[i] = 0
                tat[i] = wt[i] + burst_time[i]
    if done:
        break
print("\nProcess\tAT\tBT\tWT\tTAT")
for i in range(n):
    print(f"P{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{wt[i]}\t{tat[i]}")
print(f"\nAverage Waiting Time: {sum(wt)/n:.2f}")
print(f"Average Turnaround Time: {sum(tat)/n:.2f}")
