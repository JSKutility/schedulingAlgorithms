def priority(queue):
    print("priority scheduling")
    queue.sort(key = lambda x : (x[1], x[3]))
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
        queue.sort(key = lambda x: (x[3],x[1]))
    for i in range(len(final)):
        tat.append(complete[i] - final[i][1])
        wait.append(tat[i] - final[i][2])
    print("process  arrival burst priority complete wait \t tat")
    for i in range(len(final)):
        print(final[i][0],'\t', final[i][1],'\t', final[i][2],'\t', final[i][3],'\t', complete[i],'\t', wait[i],'\t', tat[i])

    print("No of process is ", len(final))
    print("average wait time is ", sum(wait)/len(wait))
    print("average tat is ", sum(tat)/len(tat))