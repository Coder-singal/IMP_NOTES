# Priority Scheduling (Non-Preemptive)
# Lower number = Higher priority

n = int(input("Enter number of processes: "))

processes = []   # [PID, AT, BT, Priority]

for i in range(n):
    at = int(input(f"Enter Arrival Time for P{i+1}: "))
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    pr = int(input(f"Enter Priority for P{i+1} (lower = higher priority): "))
    processes.append([i+1, at, bt, pr])

time = 0
completed = []        # list of completed PIDs
wt = [0] * n          # Waiting Time
tat = [0] * n         # Turnaround Time

while len(completed) < n:
    # Get all processes which have arrived and not completed
    ready = [p for p in processes if p[1] <= time and p[0] not in completed]

    if not ready:     # CPU idle
        time += 1
        continue

    # Choose process with highest priority (smallest priority number)
    current = min(ready, key=lambda x: x[3])
    pid, at, bt, pr = current
    idx = pid - 1

    wt[idx] = time - at
    time += bt
    tat[idx] = wt[idx] + bt
    completed.append(pid)

# Output
print("\nProcess\tAT\tBT\tPriority\tWT\tTAT")
for p in processes:
    pid, at, bt, pr = p
    print(f"P{pid}\t{at}\t{bt}\t{pr}\t\t{wt[pid-1]}\t{tat[pid-1]}")

print(f"\nAverage WT: {sum(wt)/n:.2f}")
print(f"Average TAT: {sum(tat)/n:.2f}")
