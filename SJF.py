# Shortest Job First (Non-Preemptive)

n = int(input("Enter number of processes: "))

processes = []   # Store: [PID, Arrival Time, Burst Time]

# Input
for i in range(n):
    at = int(input(f"Enter Arrival Time for P{i+1}: "))
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    processes.append([i+1, at, bt])

wt = [0] * n
tat = [0] * n
completed = []
time = 0

# Scheduling
while len(completed) < n:

    # Get ready processes
    ready = [p for p in processes if p[1] <= time and p[0] not in completed]

    if not ready:      # If CPU is idle
        time += 1
        continue

    # Choose process with shortest burst time
    shortest = min(ready, key=lambda x: x[2])

    pid, at, bt = shortest
    index = pid - 1

    wt[index] = time - at
    time += bt
    tat[index] = wt[index] + bt

    completed.append(pid)

# Output
print("\nProcess\tAT\tBT\tWT\tTAT")
for p in processes:
    pid, at, bt = p
    print(f"P{pid}\t{at}\t{bt}\t{wt[pid-1]}\t{tat[pid-1]}")

# Average calculation
print(f"\nAverage WT = {sum(wt)/n:.2f}")
print(f"Average TAT = {sum(tat)/n:.2f}")
