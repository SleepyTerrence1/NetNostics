#Calculate the results of measurements
from statistics import mean
list1 = [10.0, 20.0, 30.0]
list2 = [10.0, None, 30.0, None]
list3 = [None, None, None]

def AverageRTT(listThing):
    return mean(listThing)

def MinRTT(listThing):
    return min(listThing)

def MaxRTT(ListThing):
    return max(ListThing)

def PacketAnyalsis(listThing):
    sucessful_pings = [t for t in listThing if t is not None]

    total_sent = len(listThing)
    total_recieved = len(sucessful_pings)
    loss_percent = ((total_sent - total_recieved) / total_sent) * 100

    return total_sent, total_recieved, loss_percent

ListMOD = [t for t in list3 if t is not None]
Functions = [AverageRTT, MinRTT, MaxRTT, PacketAnyalsis]
