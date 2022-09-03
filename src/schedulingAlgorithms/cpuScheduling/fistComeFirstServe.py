def fcfs(queue):
    print("first in first serve")
    queue.sort(key = lambda x : x[1])
    complete = []
    wait = []
    tat = []
    time = queue[0][1]
    for process in queue:
    
        time+= process[2]
        complete.append(time)
        
    for i in range(len(queue)):
        tat.append(complete[i] - queue[i][1])
        wait.append(tat[i] - queue[i][2])
    print("process  arrival burst complete wait \t tat")
    for i in range(len(queue)):
        print(queue[i][0],'\t', queue[i][1],'\t', queue[i][2],'\t', complete[i],'\t', wait[i],'\t', tat[i])

    print("No of process is ", len(queue))
    print("average wait time is ", sum(wait)/len(wait))
    print("average tat is ", sum(tat)/len(tat))