total = 10
allocated = [4,3,1]
Max_need = [7,7,3]
n = len(Max_need)
need = [Max_need[i] - allocated[i] for i in range(n)]
available = total - sum(allocated)
finished = [False] * n
safe_sequence = []
while True: 
    did_allocate = False
    for i in range(n): 
        if not finished[i] and need[i] <= available: 
            did_allocate = True
            finished[i] = True
            available += allocated[i]
            need[i] -= allocated[i]
            safe_sequence.append(i+1)
    if not did_allocate: 
        break 
print("Safe sequence: ",safe_sequence)