

#Interval scheduling problem solution using the greedy algorithm.
# Input is eventlist, consisting of starting and finishing times of each event.
# i.e. [(1,2),(3,5),(1,4)....,(15,34)]


def interval_scheduler(eventlist):
    eventlist = sorted(eventlist,key=lambda x: x[1])
    execution = list()
    while len(eventlist)!=0:
       curr_start,curr_end= eventlist.pop(0)
       execution.append((curr_start,curr_end))
       while( len(eventlist)>0 and eventlist[0][0]<curr_end):
           eventlist.pop(0)
    return execution


