n = int(input("Enter number of processes: "))
processes = []   # store (PID, Arrival Time, Burst Time)

# Taking input
for i in range(n):
    at = int(input(f"Enter Arrival Time for P{i+1}: "))
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    processes.append((i+1, at, bt))

# Sort by Arrival Time
processes.sort(key=lambda x: x[1])

wt = [0]*n    # Waiting Time
tat = [0]*n   # Turn Around Time
time = 0

# FCFS logic
for i in range(n):
    pid, at, bt = processes[i]
    
    if time < at:   # CPU idle case
        time = at
        
    wt[i] = time - at
    time += bt
    tat[i] = wt[i] + bt

# Display Table
print("\nProcess\tAT\tBT\tWT\tTAT")
for i in range(n):
    pid, at, bt = processes[i]
    print(f"P{pid}\t{at}\t{bt}\t{wt[i]}\t{tat[i]}")

# Averages
avg_wt = sum(wt)/n
avg_tat = sum(tat)/n

print("\nAverage WT =", avg_wt)
print("Average TAT =", avg_tat)
