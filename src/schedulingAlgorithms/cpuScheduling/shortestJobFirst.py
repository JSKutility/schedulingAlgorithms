def sjf(queue):
    print("short job first")
    queue.sort(key = lambda x : (x[1], x[2]))
    complete = []
    wait = []
    tat = []
    time = queue[0][1]
    final =[]
    while(queue):
        process = queue.pop(0)
        time+= process[2]
        complete.append(time)
        final.append(process)
        queue.sort(key = lambda x: (x[2],x[1]))
    for i in range(len(final)):
        tat.append(complete[i] - final[i][1])
        wait.append(tat[i] - final[i][2])
    print("process  arrival burst complete wait \t tat")
    for i in range(len(final)):
        print(final[i][0],'\t', final[i][1],'\t', final[i][2],'\t', complete[i],'\t', wait[i],'\t', tat[i])

    print("No of process is ", len(final))
    print("average wait time is ", sum(wait)/len(wait))
    print("average tat is ", sum(tat)/len(tat))